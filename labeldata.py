import cv2 as cv
import time
import argparse

prev_x = 0
prev_y = 0


def mouse_capture(event, x, y, flags, param):
    global prev_x
    global prev_y
    if event == cv.EVENT_MOUSEMOVE:
        prev_x = x
        prev_y = y


def parse_frames(video, label_file, delay=.01666):
    cap = cv.VideoCapture(video)
    cv.namedWindow('Capture')
    cv.setMouseCallback('Capture', mouse_capture)
    time.sleep(1)
    with open(label_file, 'w') as out_file:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv.imshow("Capture", frame)
            time.sleep(delay)
            if cv.waitKey(10) & 0xFF == ord('q'):
                break
            img_name = str(prev_x)
            out_file.write(img_name + "\n")

    cap.release()
    cv.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(
        description='This will help you label a video.',
        epilog='You\'re going to have to provide arguments.')

    parser.add_argument('video', type=str, default=None, help='the relative path to your video file.')
    parser.add_argument('out_file', type=str, default="labels.txt", help='The name of the output file')
    parser.add_argument('frame_delay', type=float, default=.01666, help='Use this number to label faster or slower.')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == "__main__":
    main()