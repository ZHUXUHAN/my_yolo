# -*- coding: utf-8 -*-
import os

if __name__ == '__main__':
    datasetname = 'train'
    path1 = "/train/trainset/1/mscoco2017/{}2017".format(datasetname) // 图片的文件夹
    namepath = "/home/Yolo/PyTorch-YOLOv3/data/coco/labels/{}2017".format(datasetname)
    txtpath = "/Users/zhangzhenghao/Desktop/test/val_coco" + "{}.txt".format(datasetname) // 放入的txt文件
    with open(txtpath, 'a+') as fp:
        for name in allfile1:
            newpath = os.path.join(namepath, name)
            fp.write("".join(newpath) + "\n")

