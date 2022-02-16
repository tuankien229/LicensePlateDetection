# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 22:08:01 2022

@author: tuank
"""
#%% 1. Import Library
import os
import time
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd
import albumentations as A

os.chdir('D:/')
#%% 2. Visualize Data
path = 'D:/Spyder/Image/Bien_so_xe_full/'
data_path = 'GreenParking/'
save_path = 'Save_image/'
location = 'location.txt'
data_df = pd.read_csv(os.path.join(path + data_path, location), header=None)
image_paths = []
for i, data in enumerate(data_df[0]):
    image_name = data.split(" ")[0]
    image_path = os.path.join(path + data_path, image_name)
    image_paths.append(image_path)
# Visualize Image
image = cv2.imread(image_paths[1])
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
plt.imshow(image)
plt.show()
    
#%% 3.Augmentaion Image Data
class AugmentationsImage():
    def __init__(self, image_paths):
        self.image_paths = image_paths
    
    def __getitem__(self,index):
        image = cv2.imread(self.image_paths[index])
        image = self.augmentations(image)
        return image
    
    def augmentations(self, image):
        list_aug = [A.RandomBrightness(),
                    A.Rotate(limit = 30, p = 0.5)
                    ]
        augmentation = A.Compose(list_aug)
        image_augmented = augmentation(image=image)
        image = image_augmented['image']
        return image
if __name__ == '__main__':
    augmentation = AugmentationsImage(image_paths)
    image_augmented = augmentation[1]
    image_augmented = np.array(image_augmented, np.uint8)
    plt.imshow(image_augmented)
    
#%% 4. Save Image Augmentation
for i in range(len(image_paths)):
    augmentaion = AugmentationsImage(image_paths)
    image_augmented = augmentaion[i]
    image_path = os.path.join(path + save_path, str(i)+'.jpg')
    cv2.imwrite(image_path, image_augmented)
    

    
    