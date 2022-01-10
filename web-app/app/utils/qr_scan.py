from imutils.video import VideoStream
from pyzbar import pyzbar
import cv2
from threading import Timer

VALID_QR = "negative with covid"

width = 1280
height = 720

def scan_qr_code(stream_origin):
	stop_flag = False

    # cap = VideoStream(usePiCamera=True).start()
	cap = cv2.VideoCapture(stream_origin)

	if not cap.isOpened():
		raise IOError("Cannot open webcam")

	while True:
		ret, frame = cap.read()
		frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
		barcodes = pyzbar.decode(frame)
		for barcode in barcodes:
			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
			barcodeData = barcode.data.decode("utf-8")
			barcodeType = barcode.type
			text = "{} ({})".format(barcodeData, barcodeType)
			
			# Check the barcode is valid or not
			if barcodeData == VALID_QR:
				cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
				cap.release()
				stop_flag = True
				# cap.stop()
				cv2.destroyAllWindows()
				return True
			else:
				cv2.putText(frame, "Invalid QR. Please try again.", 
							(x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
				cap.release()
				cv2.destroyAllWindows()
				return False
		
		# show the output frame
		cv2.imshow("Barcode Scanner", frame)
		key = cv2.waitKey(1) & 0xFF
		
		(flag, encodedImage) = cv2.imencode(".jpg", frame)
		if not flag:
			continue


		if stop_flag:
			t = Timer(5, cv2.destroyAllWindows())
			t.start()
			break

		# if the `q` key was pressed, break from the loop
		# if key == ord("q"):
		# 	break

	cap.release()
	cv2.destroyAllWindows()
	return True


if __name__ == "__main__":
    scan_qr_code(0)