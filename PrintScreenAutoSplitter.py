# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:00:00 2020

@author: Matheus Ruggeri
"""

import cv2
import os

# Put your PrintScreen directory from Dropbox, Google Drive, OneDrive...
path = "C:\\Users\Matheus\Dropbox\Capturas de tela"

# Get all the files or directories in this path
files = os.listdir(path)

for f in files:
    # Check if the element in 'files' is a file or a directory
    if os.path.isfile(path + "\\" + f):
        nameWithoutExtention = os.path.splitext(f)[0]
        img = cv2.imread(path + "\\" + f)
        height = img.shape[0]
        width = img.shape[1]
        
        # I have 2 Full HD monitors, so I check if the width is higher than 1920
        if width > 1920:
            print(f)
            
            # Set the limits to cut in the middle
            width_cutoff = width // 2
            s1 = img[:, :width_cutoff]
            s2 = img[:, width_cutoff:]
            
            # Exports the files as xxx_1.png and xxx_2.png
            cv2.imwrite(path + "\\" + nameWithoutExtention + "_1.png", s1)
            cv2.imwrite(path + "\\" + nameWithoutExtention + "_2.png", s2)
            os.remove(os.path.join(path,f))
