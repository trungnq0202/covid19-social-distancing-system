from entry_exit_detection import detect
from environmental_sensors import scan
import thread

if __name__ == '__main__':
	thread.start_new_thread(detect())
	thread.start_new_thread(scan())