import cv2
import os
from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--vid_path", default = 1, help="path to video need to extract")
parser.add_argument("--save_dir", default = 2, help="path to extract dir")

def extract_frame(vid_path, save_folder):
    assert os.path.isfile(vid_path)
    assert os.path.isdir(save_folder)

    cap= cv2.VideoCapture(vid_path)
    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite(os.path.join(save_folder, 'frame_{:06d}.jpg'.format(i)), frame)
        print('Extracting frame {}'.format(i))
        i+=1

    print('Finish extracting.')

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    args = parser.parse_args()

    extract_frame(args.vid_path, args.save_dir)