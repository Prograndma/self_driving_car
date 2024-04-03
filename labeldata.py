import cv2
import uuid
import time

prev_x = 0
prev_y = 0

def mouseCapture(event, x, y, flags, param):
    global prev_x
    global prev_y
    if event == cv2.EVENT_MOUSEMOVE:
        prev_x = x
        prev_y = y


def main():
    cap = cv2.VideoCapture("figure8traindata.mkv")
    cv2.namedWindow('Capture')
    cv2.setMouseCallback('Capture', mouseCapture)
    time.sleep(1)
    count = 0
    with open("lane_labels.txt", 'w') as out_file:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Capture", frame)
            # Modify this line to adjust how fast the video plays back
            time.sleep(0.01666)
            count += 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            #img_name = f'lane_following/{prev_x}_0_{count}.jpg'
            img_name = str(prev_x)
            #cv2.imwrite(img_name, frame)
            #print(img_name)
            out_file.write(img_name+"\n")


    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()