# -*- coding: utf-8 -*-            
# @Time : 2022/12/1 10:52
# @Author:CHR
# @FileName: videoDetect.py
# @Software: PyCharm
import os
import re
import cv2
from tqdm import tqdm
import shutil
import time

# 创建文件夹
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        shutil.rmtree(path) # 清空文件夹
        os.makedirs(path)

# 遍历指定文件夹
def getFiles(path):
    for root, dirs, files in os.walk(path):return root, dirs, files

# 获取视频文件总时长
def get_video_duration(filename):
    cap = cv2.VideoCapture(filename)
    if cap.isOpened():
        rate = cap.get(5)
        frame_num = cap.get(7)
        duration = frame_num/rate
        return duration
    return -1

def main(path):
    mkdir('new')
    parttern = re.compile('black_duration:(.*)')
    root, dir_list, files_list = getFiles(path)
    for file in tqdm(files_list):
        if file.endswith('.mp4'):
            os.system(f'ffmpeg -loglevel info -i "{"".join([root, os.sep, file])}" -vf blackdetect=d=0.5:pic_th=0.75 -f null - > tmp.txt 2>&1')
            time.sleep(1)
            with open("tmp.txt",'r',encoding='utf8')as f:
                lines = f.readlines()
                timeLast = re.findall(parttern,lines[-3])
                if timeLast:
                    totalDuration = get_video_duration("".join([root, os.sep, file]))
                    stopTime = int(float(totalDuration)-float(timeLast[-1]))
                    m, s = divmod(stopTime, 60)
                    h, m = divmod(m, 60)
                    s -= 3
                    os.system(f'ffmpeg -i "{"".join([root, os.sep, file])}" -ss 00:00:00 -to "{h:02}:{m:02}:{s:02}" ".//new//{file}"')
                else: print("正则匹配失败")
    return 1

if __name__=="__main__":
    res = main(r"/Users/chenhanrui/Downloads/downie下载/Multivariable Calculus")
    if res == 1: print("任务顺利结束")

