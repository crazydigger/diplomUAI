import subprocess,os
subprocess.call('python', 'yolov5\train.py','--img 500', '--batch 16', '--epochs 10')