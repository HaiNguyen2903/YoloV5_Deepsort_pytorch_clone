import os
from shutil import copyfile

ratio = 0.1

train_images_path = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/images/train'
train_labels_path = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/labels/train'

val_images_path = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/images/val'
val_labels_path = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/combine_dataset/labels/val'

len_all = len(os.listdir(train_images_path))

size = int(len_all * ratio)
count = 0

for img in os.listdir(train_images_path):
    if count <= size:
        print('splitting {}'.format(img))
        count += 1

        assert os.path.join(train_images_path, img)
        assert os.path.join(train_labels_path, img[:-3] + 'txt')

        copyfile(os.path.join(train_images_path, img), os.path.join(val_images_path, img))
        copyfile(os.path.join(train_labels_path, img[:-3] + 'txt'), os.path.join(val_labels_path, img[:-3] + 'txt'))
        
        os.remove(os.path.join(train_images_path, img))
        os.remove(os.path.join(train_labels_path, img[:-3] + 'txt'))

assert len(os.listdir(val_images_path)) == len(os.listdir(val_labels_path))

print('success splitting')