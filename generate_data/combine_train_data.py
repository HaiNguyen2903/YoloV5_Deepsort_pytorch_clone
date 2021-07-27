import os 

'''
This file combine frames data from multi folders to generate 1 unique training dataset
'''

root_dir = '/data.local/hangd/data_vtx/frames_data/train'
combine_dir = ''

train_vid_order = [
    'NVR-CH01_S20210607-094253_E20210607-094856',
    'NVR-CH02_S20210607-112840_E20210607-120113',
    'NVR-CH01_S20210607-095007_E20210607-095126',
    'NVR-CH07_S20210609-112939_E20210609-113836',
    'NVR-CH01_S20210607-113251_E20210607-120452'
]

vid2gt = {
1:3
}

total_frame = 0

for i in range(len(train_vid_order)):
    length = len(os.listdir(os.path.join(root_dir, train_vid_order[i])))
    total_frame += length

print('Total frames:', total_frame)

current_frame = 0

'''
Unnote to create symlink
'''
for i in range(len(train_vid_order)):
    length = len(os.listdir(os.path.join(train_vid_order[i])))

    for img in os.listdir(os.path.join(root_dir, train_vid_order[i])):
        id = int(img[6:12]) + current_frame
        os.symlink(os.path.join(root_dir, train_vid_order[i], img), os.path.join(combine_dir, 'frame_{:06d}.jpg'.format(id)))

    for label in 
    current_frame += length+1

assert len(os.listdir(combine_dir)) == total_frame

