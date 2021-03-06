# import the necessary packages
from imutils.video import VideoStream
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import threading
import imutils
import time
import cv2
from util.apiHelper import RequestsApi
import uvicorn
from multiprocessing import Process, Queue
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import numpy as np
from util import config, thread
from util.detection import detect_people
from imutils.video import VideoStream, FPS
from scipy.spatial import distance as dist
import numpy as np
import argparse, imutils, cv2, os, time, schedule

HTTP_PORT = 8003
lock = threading.Lock()
app = FastAPI()

SERVER_HOST = "http://0.0.0.0:8001/"
server = RequestsApi(base_url=SERVER_HOST)

manager = None
count_keep_alive = 0

#cors for FastAPI
origins = ["*"]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*']
)

# load the COCO class labels our YOLO model was trained on
labelsPath = os.path.sep.join([config.MODEL_PATH, "coco.names"])
LABELS = open(labelsPath).read().strip().split("\n")

# derive the paths to the YOLO weights and model configuration
weightsPath = os.path.sep.join([config.MODEL_PATH, "yolov3.weights"])
configPath = os.path.sep.join([config.MODEL_PATH, "yolov3.cfg"])

# load our YOLO object detector trained on COCO dataset (80 classes)
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

# check if we are going to use GPU
if config.USE_GPU:
	# set CUDA as the preferable backend and target
	print("")
	print("[INFO] Looking for GPU")
	net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
	net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

# determine only the *output* layer names that we need from YOLO
ln = net.getLayerNames()
ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

print("[INFO] Starting the live stream..")


def start_stream(url_rtsp, manager):
    global width
    global height

    # vs = VideoStream(url_rtsp).start()
    vs = cv2.VideoCapture(config.url)
    if config.Thread:
        cap = thread.ThreadingClass(config.url)
    
    time.sleep(2.0)

    writer = None
    # start the FPS counter
    fps = FPS().start()

    while True:
        # read the next frame from the file
        if config.Thread:
            frame = cap.read()

        else:
            (grabbed, frame) = vs.read()
		
        # if the frame was not grabbed, then we have reached the end of the stream
            if not grabbed:
                break
        
        # resize the frame and then detect people (and only people) in it
        frame = imutils.resize(frame, width=700)
        results = detect_people(frame, net, ln,
		    personIdx=LABELS.index("person"))

        # initialize the set of indexes that violate the max/min social distance limits
        serious = set()     
        abnormal = set()

        # ensure there are *at least* two people detections (required in
	    # order to compute our pairwise distance maps)
        if len(results) >= 2:
		    # extract all centroids from the results and compute the
		    # Euclidean distances between all pairs of the centroids
            centroids = np.array([r[2] for r in results])
            D = dist.cdist(centroids, centroids, metric="euclidean")

            n, _ = D.shape
            for i in range(0, n):
                for j in range(i + 1, n):
                    if D[i, j] < config.MAX_DISTANCE:
                        abnormal.add(i)
                        abnormal.add(j)

            for i in range(0, n):
                for j in range(0, n):
                    for k in range(0, n):
                        if i != j and j != k and i != k:
                            if D[i, j] < config.MAX_DISTANCE and D[j, k] < config.MAX_DISTANCE:
                                serious.add(i)
                                serious.add(j)
                                serious.add(k)

        # loop over the results
        for (i, (prob, bbox, centroid)) in enumerate(results):
		    # extract the bounding box and centroid coordinates, then
		    # initialize the color of the annotation
            (startX, startY, endX, endY) = bbox
            (cX, cY) = centroid
            color = (0, 255, 0)

		    # if the index pair exists within the violation/abnormal sets, then update the color
            if i in serious:
                color = (0, 0, 255)
            elif i in abnormal:
                color = (0, 255, 255) #orange = (0, 165, 255)
            

		    # draw (1) a bounding box around the person and (2) the
		    # centroid coordinates of the person,
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
            cv2.circle(frame, (cX, cY), 5, color, 2)

        # draw some of the parameters
        # Safe_Distance = "Safe distance: >{} px".format(config.MAX_DISTANCE) 
        # cv2.putText(frame, Safe_Distance, (470, frame.shape[0] - 25),
		#     cv2.FONT_HERSHEY_SIMPLEX, 0.60, (255, 0, 0), 2)
        # Threshold = "Threshold limit: {}".format(config.Threshold)
        # cv2.putText(frame, Threshold, (470, frame.shape[0] - 50),
		#     cv2.FONT_HERSHEY_SIMPLEX, 0.60, (255, 0, 0), 2)

        # draw the total number of social distancing violations on the output frame
        text = "Total group violations: {}".format(len(serious))
        cv2.putText(frame, text, (10, frame.shape[0] - 55),
            cv2.FONT_HERSHEY_SIMPLEX, 0.70, (0, 0, 255), 2)

        text1 = "Total distance violations: {}".format(len(abnormal))
        cv2.putText(frame, text1, (10, frame.shape[0] - 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.70, (0, 255, 255), 2)

        #------------------------------Alert function----------------------------------#
        if len(serious) >= config.Threshold:
            # cv2.putText(frame, "-ALERT: Violations over limit-", (10, frame.shape[0] - 80),
            #     cv2.FONT_HERSHEY_COMPLEX, 0.60, (0, 0, 255), 2)
            response = server.post('roomMonitor/setTask4Flag/true')
            
        if len(abnormal) >= config.Threshold:
            response = server.post('roomMonitor/setTask3Flag/true')

        # frame = vs.read()
        # frame = imutils.resize(frame, width=680)
        output_frame = frame.copy()

        if output_frame is None:
            continue
        (flag, encodedImage) = cv2.imencode(".jpg", output_frame)
        if not flag:
            continue
        manager.put(encodedImage)
        fps.update()


def manager_keep_alive(p):
    global count_keep_alive
    global manager
    while count_keep_alive:
        time.sleep(1)
        print(count_keep_alive)
        count_keep_alive -= 1
    p.kill()
    # time.sleep(.5)
    p.close()
    manager.close()
    manager = None

def streamer():
    try:
        while manager:
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                   bytearray(manager.get()) + b'\r\n')
    except GeneratorExit:
        print("cancelled")


@app.get("/")
async def video_feed():
    return StreamingResponse(streamer(), media_type="multipart/x-mixed-replace;boundary=frame")


@app.get("/keep-alive")
def keep_alive():
    global manager
    global count_keep_alive
    count_keep_alive = 100000000
    if not manager:
        manager = Queue()
        p = Process(target=start_stream, args=(config.url, manager,))
        p.start()
        threading.Thread(target=manager_keep_alive, args=(p,)).start()


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=HTTP_PORT, access_log=False)
