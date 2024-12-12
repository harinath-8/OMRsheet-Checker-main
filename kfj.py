import cv2
import numpy as np
import os
# def load_images_from_folder(folder):
#     images=[]
#     for filename in os.listdir(folder):
#         img = cv2.imread(os.path.join(folder,filename))
#         print(os.path.join(folder, filename))
#         if img is not None:
#             images.append(img)
#     return images
# images = load_images_from_folder('answerSheet')
# for i in range(len(images)):
#     cv2.imshow('tusha',f'answerSheet/{str(i+1)}.jpg')
#     cv2.waitKey(2000)
# print(len(images))
# for img in images:
#     cv2.imshow('tshar',img)
#     cv2.waitKey(1000)
#     #
from glob import glob

# img_mask = 'answerSheet/*.jpg'
# img_names = glob(img_mask)
# for fn in img_names:
#     print('processing %s...' % fn, )
#     img = cv2.imread(fn, 0)
#     cv2.imshow('tus',img)
#     cv2.waitKey(2000)



for i in range(3):
    p = 'answerSheet/' + str(i + 1) + '.jpg'
    img = cv2.imread(p)
    cv2.imshow('tu',img)
    cv2.waitKey(1000)