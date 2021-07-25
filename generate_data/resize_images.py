from PIL import Image
import os

data_root = '/data.local/all/hainp/yolov5_deep_sort/YoloV5_Deepsort_pytorch_clone/dataset2/images'
train_imgs = os.path.join(data_root, 'train')
val_imgs = os.path.join(data_root, 'val')

shape = (1920, 1080)

for img in os.listdir(train_imgs): 
    with Image.open(os.path.join(train_imgs, img)) as im:

        # Provide the target width and height of the image
        (width, height) = shape
        im_resized = im.resize((width, height))
        im_resized.save(os.path.join(train_imgs, img))
        print('Resize image {}'.format(os.path.join(train_imgs, img)))

for img in os.listdir(val_imgs): 
    with Image.open(os.path.join(val_imgs, img)) as im:

        # Provide the target width and height of the image
        width, height = shape
        im_resized = im.resize((width, height))
        im_resized.save(os.path.join(val_imgs, img))
        print('Resize image {}'.format(os.path.join(train_imgs, img)))

print('Done.')



