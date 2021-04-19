import numpy as np
import cv2
import time

import os
os.chdir(os.path.dirname(os.path.abspath( __file__ )))

IN_PATH = 'amongus.gif' # your original media file
OUT_PATH = 'array_data' # output file
gif = cv2.VideoCapture(PATH)

ret, frame = gif.read()

width = 32
height = 16
dim = (width, height)

f = open(OUT_PATH,"w")

while ret:
    try:
        ret, frame = gif.read()
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        for i in range(0,16):
            for j in range(0,32):
                for k in range(0,3):
                    f.write(str(img[i][j][k])+' ')
    except:
        pass
f.close()