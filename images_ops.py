#!/usr/bin/python3

import cv2
# importing computer vision buold in c++ lang
# read image data

read_ops=[i for i in dir (cv2) if 'read' in i]
print(read_ops)
