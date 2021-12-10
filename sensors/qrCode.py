#from imutils.video import VideoStream
from fastapi.applications import FastAPI
from pyzbar import pyzbar
import argparse
import datetime
#import imutils
import time
import cv2

import threading

from starlette.responses import StreamingResponse
import time
import uvicorn
from multiprocessing import Process, Queue
import numpy as np
from threading import Timer

from lcd16x2 import display_message

VALID_QR = "negative with covid"

HTTP_PORT = 6064
lock = threading.Lock()
app = FastAPI()

manager = None

width = 1280
height = 720

def generator():
	try:
		while manager:
			yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                   bytearray(manager.get()) + b'\r\n')
	except GeneratorExit:
		print('Cancelled')

def turn_on_qr_reader():
	counter = 0
	stop_flag = False

	# cap = VideoStream(usePiCamera=True).start()
	cap = cv2.VideoCapture(0)

	# Check if the webcam is opened correctly
	if not cap.isOpened():
		raise IOError("Cannot open webcam")

	#time.sleep(2.0)


	# loop over the frames from the video stream
	while True:
		# grab the frame from the threaded video stream and resize it to
		# have a maximum width of 400 pixels
		ret, frame = cap.read()
		frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
		# frame = imutils.resize(frame, width=400)
		# find the barcodes in the frame and decode each of the barcodes
		barcodes = pyzbar.decode(frame)
			# loop over the detected barcodes
		for barcode in barcodes:
			# extract the bounding box location of the barcode and draw
			# the bounding box surrounding the barcode on the image
			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
			# the barcode data is a bytes object so if we want to draw it
			# on our output image we need to convert it to a string first
			barcodeData = barcode.data.decode("utf-8")
			barcodeType = barcode.type
			# draw the barcode data and barcode type on the image
			text = "{} ({})".format(barcodeData, barcodeType)
			
			# Check the barcode 
			if barcodeData == VALID_QR:
				cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
				display_message("Welcome")
				cap.release()
				stop_flag = True
				#cap.stop()
				# cv2.destroyAllWindows()
				# return True
			else:
				cv2.putText(frame, "Invalid QR. Please try again." + str(3 - counter)	 + " times remaining.", 
							(x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
				display_message("Invalid QRcode")
				cap.release()
				# cv2.destroyAllWindows()
				# return False
		
		# show the output frame
		cv2.imshow("Barcode Scanner", frame)
		key = cv2.waitKey(1) & 0xFF
		
		(flag, encodedImage) = cv2.imdecode(".jpg", frame)
		if not flag:
			continue

		manager.put(encodedImage)

		if stop_flag:
			t = Timer(5, cv2.destroyAllWindows())
			t.start()
			break

		# if the `q` key was pressed, break from the loop
		# if key == ord("q"):
		# 	break

	cap.release()
	cv2.destroyAllWindows()
	return
	

@app.get('/video-feed')
async def video_feed():
	return StreamingResponse(generator(), media_type='multipart/x-mixed-replace;boundary=frame')


if __name__ == "__main__":
	# status = turn_on_qr_reader()
	# print(status)
	turn_on_qr_reader()
	uvicorn.run(app, host="0.0.0.0", port=HTTP_PORT, access_log=True)