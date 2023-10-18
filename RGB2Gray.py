import glob
import os
from PIL import Image
from tqdm import tqdm

def gettAllImage(img_dir):
    extensions = ('*.bmp','*.dib','*.png','*.jpeg','*.pbm','*.pgm','*.ppm','*.tif','*.tiff','*.npy')
    imgAll = glob.glob(os.path.join(img_dir, '*.jpg'))
    for ext in extensions:
        imgAll.extend((glob.glob(os.path.join(img_dir,ext))))
    return imgAll

def main(docDir):
    parentDir = os.path.dirname(docDir)
    GrayDir = os.path.join(parentDir,'Gray')
    if not os.path.exists(GrayDir):
        os.mkdir(GrayDir)
    imgs = gettAllImage(docDir)
    for i in tqdm(range(len(imgs))):
        img_gray= Image.open(imgs[i]).convert('L')
        img_gray.save(os.path.join(GrayDir,imgs[i].split(os.sep)[-1]))

if __name__ == '__main__':
    main('E:\pycharmProjects\pytorch-deeplab-xception\dataset\msrs\JPEGImages')
