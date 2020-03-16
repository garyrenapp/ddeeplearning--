http://www.voidcn.com/article/p-wefishkl-brm.html

https://www.bilibili.com/video/av91598533?p=6

https://towardsdatascience.com/faster-r-cnn-object-detection-implemented-by-keras-for-custom-data-from-googles-open-images-125f62b9141a

https://github.com/bubbliiiing/faster-rcnn-keras
https://github.com/jinfagang/keras_frcnn

## 样本生成阶段
* 正负样本的问题：
1. anchor 与 gtbox的 iou 大于0.7 保留 ，0.3 - 0.7 忽略。 0.3 是副样本。这样会得到大量的候选框，选取256个（128正 + 128 负）

## 训练阶段
rpn 后 用nms 选300个。 算iou 0.1 到 0.5 的算负的 大于0.5 算正的 。 随机选出32个组成一个batch。给classfier。
测试的阶段 这300个要 切成n个32的片 依次classfier