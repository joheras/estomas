# Program to generate the dataset of images from the annotated images.
# For each image, we will create a set of patches of size 128x128 and
# their masks. We suppose that the images are annotated using the PASCAL-VOC
# format.

import cv2
from generateMask import generateMask
from imutils import paths
import os
from extractPatches import extractPatches
from tqdm import tqdm

IMAGES_PATH = "../images/"
DATASET_PATH = "../dataset/"
DATASET_IMAGES_PATH = DATASET_PATH+ "images/"
DATASET_LABELS_PATH = DATASET_PATH+ "labels/"
PATCHSIZE = (128,128)
STEP = (128,128)

imagesPaths = list(paths.list_files(IMAGES_PATH,validExts=(".tif",".jpg")))
print imagesPaths

for imagePath in imagesPaths:
    imageName = name = imagePath.split(os.path.sep)[-1]
    image = cv2.imread(imagePath)
    label = generateMask(imagePath)

    patches_image = extractPatches(image,PATCHSIZE,STEP)
    patches_label = extractPatches(label, PATCHSIZE, STEP)

    for (i,(im,lab)) in tqdm(enumerate(zip(patches_image,patches_label))):
        cv2.imwrite(DATASET_IMAGES_PATH+str(i)+"_"+imageName,im)
        cv2.imwrite(DATASET_LABELS_PATH + str(i) + "_" + imageName, lab)








