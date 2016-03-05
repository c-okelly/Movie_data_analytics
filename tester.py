import cv2
import time


def convert_video_and_ouput_x_frame():

    curent_time = time.time()
    cap = cv2.VideoCapture("1Trailer.mp4")
    count = 0

    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Test frame opend
        if ret == True:
            # Only every x frame
            if count % 15 == 0:
                cv2.imwrite("frame%d.jpg" % count, frame)

            count += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the capture
    cap.release()

    finish_time = time.time()
    print("The run time was %f seconds " % (finish_time-curent_time))

def compare_images():

if __name__ == '__main__':
    convert_video_and_ouput_x_frame()