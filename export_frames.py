import cv2
import uuid
import os
import argparse


def export_frames(video, label_file, save_path):
    if video or save_path is None:
        raise Exception("Video or save_path need to be supplied!")
    cap = cv2.VideoCapture(video)
    with open(label_file, 'r') as f:
        labels = f.readlines()
        for x in labels:
            ret, frame = cap.read()
            if not ret:
                break
            img_name = f'{save_path}/{x.strip()}_0_{str(uuid.uuid4())}.jpg'
            cv2.imwrite(img_name, frame)

    cap.release()
    cv2.destroyAllWindows()


def main():
    parser = argparse.ArgumentParser(
        description='This will help you label a video.',
        epilog='You\'re going to have to provide arguments.')

    parser.add_argument('video', type=str, default=None, help='the relative path to your video file.')
    parser.add_argument('labels', type=str, default="labels.txt", help='The name of the output file')
    parser.add_argument('save_path', type=float, default=None, help='Use this number to label faster or slower.')

    args = parser.parse_args()
    save_path = args.save_path
    os.mkdirs(save_path, exist_ok=True)
    export_frames(args.video, args.out_file, args.frame_delay)


if __name__ == "__main__":
    main()
