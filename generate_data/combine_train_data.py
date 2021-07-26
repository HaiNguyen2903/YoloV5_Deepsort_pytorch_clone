import os 
import sys
'''
This file combine frames data from multi folders to generate 1 unique training dataset
'''

root_dir = '/data.local/hangd/data_vtx/frames_data/train'
gt_dir = '/data.local/hangd/data_vtx/detection_dataset/labels/train_gt/'

combine_frame_dir = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/images/train'
combine_gt_dir = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/labels/train'

train_vid_order = [
    'NVR-CH01_S20210607-094253_E20210607-094856',
    'NVR-CH02_S20210607-112840_E20210607-120113',
    'NVR-CH01_S20210607-095007_E20210607-095126',
    'NVR-CH07_S20210609-112939_E20210609-113836',
    'NVR-CH01_S20210607-113251_E20210607-120452'
]

current_frame = 0

# '''
# Unnote to create symlink
# '''
count = 0
exception = []

for i in range(len(train_vid_order)):
    length = len(os.listdir(os.path.join(root_dir, train_vid_order[i])))

    for img in os.listdir(os.path.join(root_dir, train_vid_order[i])):
        id = int(img[6:12]) + current_frame
        print(id)
        os.symlink(os.path.join(root_dir, train_vid_order[i], img), os.path.join(combine_frame_dir, 'frame_{:06d}.jpg'.format(id)))

    for label in os.listdir(os.path.join(gt_dir, train_vid_order[i])):
        # print('id', id)
        try:
            id = int(label[6:12]) + current_frame
            os.symlink(os.path.join(gt_dir, train_vid_order[i], label), os.path.join(combine_gt_dir, 'frame_{:06d}.txt'.format(id)))

            print('Gen frame {}'.format(id))
        except:
            print(os.path.join(gt_dir, train_vid_order[i], label))
            exception.append(os.path.join(gt_dir, train_vid_order[i], label))
            os.remove(os.path.join(gt_dir, train_vid_order[i], label))
            count += 1
            # exit()

#     print('current_frame', current_frame)
    current_frame += length+1

total_frame = 0

for i in range(len(train_vid_order)):
    length = len(os.listdir(os.path.join(root_dir, train_vid_order[i])))
    total_frame += length

print('Total frames:', total_frame)
assert len(os.listdir(combine_frame_dir)) == combine_gt_dir == total_frame

print(len(os.listdir(combine_frame_dir)), len(os.listdir(combine_gt_dir)), count)
print(exception)

print('Successed')

