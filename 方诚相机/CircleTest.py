# -*- coding: utf-8 -*-

# image process
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time
import os, sys

import ReadImage as RI



ncount = RI.Camera.InitManager()
if ncount < 1:
    print('没有找到相机')
    exit(2)

camera = RI.Camera()
camera.startCamera()

index = 0

while (index < 5):
    camera.grabImage()

    image = Image.frombuffer('L', (camera.nWidth, camera.nHeight), camera.raw_memory)
    image.show()
    del image
    
    # draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype("arial.ttf",14)
    # draw.text((0, 220), "This is a test11", font=font)
    # draw = ImageDraw.Draw(image)


    # img = Image.open("fairsion.bmp")
    # img.show()
    # del img # 释放图片，不然会占用着，图片不能更新
    
    # os.remove("fairsion.bmp")
    index += 1
    time.sleep(1)
    

camera.CloseCamera()

RI.Camera.ReleaseManager()

