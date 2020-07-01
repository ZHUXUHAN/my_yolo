# my_yolo

coco的验证集和训练集的标签 用data/get_coco_dataset.sh来获得。
因为用自己的代码生成的标签精度不对.

wget -c https://pjreddie.com/media/files/coco/5k.part
wget -c https://pjreddie.com/media/files/coco/trainvalno5k.part

然后将两个文件分别放到 coco数据集文件夹的目录下。

paste <(awk "{print \"$PWD\"}" <5k.part) 5k.part | tr -d '\t' > 5k.txt

paste <(awk "{print \"$PWD\"}" <trainvalno5k.part) trainvalno5k.part | tr -d '\t' > trainvalno5k.txt

这样就会在当前文件夹下生成label的 文本txt，再放置在labels文件夹下就行

![image](https://github.com/ZHUXUHAN/my_yolo/blob/master/assets/giraffe.png)
