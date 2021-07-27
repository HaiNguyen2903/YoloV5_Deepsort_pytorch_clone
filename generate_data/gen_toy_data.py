import os 

src_frames_dir = '/data.local/hangd/data_vtx/frames_data/train/NVR-CH01_S20210607-095007_E20210607-095126/'
src_labels_dir = '/data.local/hangd/data_vtx/detection_dataset/labels/train_gt/NVR-CH01_S20210607-095007_E20210607-095126/'

toy_imgs = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/images/val/'

toy_labels = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/labels/val'

for img in os.listdir(src_frames_dir):
    os.symlink(os.path.join(src_frames_dir, img), os.path.join(toy_imgs, img[:-3] + 'jpg'))

for label in os.listdir(src_labels_dir):
    os.symlink(os.path.join(src_labels_dir, label), os.path.join(toy_labels, label))

assert len(os.listdir(toy_imgs)) == len(os.listdir(toy_labels))

print('Length toy dataset:', len(os.listdir(toy_imgs)))

