# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    datasetname = 'val'
    year = '2017'
    path1 = "/train/trainset/1/mscoco{}/{}{}".format(year, datasetname, year) #图片的文件夹
    namepath = "/home/Yolo/yolov3/data/coco{}/images/{}{}".format(year, datasetname, year)
    txtpath = "/home/Yolo/yolov3/data/coco{}/".format(year) + "{}.txt".format(datasetname) #放入的txt文件
    allfile1 = os.listdir(path1)
    with open(txtpath, 'a+') as fp:
        for name in allfile1:
            newpath = os.path.join(namepath, name)
            fp.write("".join(newpath) + "\n")

