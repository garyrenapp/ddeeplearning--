

# 图像旋转
```python
"""
在图像中画一个矩形，旋转图像的同时，点跟着旋转
"""
import cv2
import numpy as np 
import matplotlib.pyplot as plt 

(h,w) = 500,500

img = np.ones((h,w,3),np.uint8) * 255

# (pt1,pt2)
rect = [(100,100),(200,400)]
img = cv2.rectangle(img,rect[0],rect[1],color=(255,0,0),thickness=-1)
img_1 = np.copy(img)
for r in rect:
    cv2.circle(img_1,r,2,(0,0,255),thickness=3)
plt.imshow(img_1)

img_2 = np.copy(img)
M  = cv2.getRotationMatrix2D((w/2,h/2),-10,1.0)
img_2 = cv2.warpAffine(img_2,M,(w,h),borderValue=(255,255,255))
#注意这里
#https://stackoverflow.com/questions/44378098/trouble-getting-cv-transform-to-work
r_rect = cv2.transform(np.array([rect]),M)[0]
for r in r_rect:
    print(r)
    cv2.circle(img_2,tuple(r),2,(0,0,255),thickness=3)
plt.imshow(img_2)
```
![](imgs/rotate.png)

## 像素坐标矩阵变换
### 平移
$$
x = x_{0} + ax \\
y = y_{0} + ay
$$
$$
\begin{bmatrix}
    x\\
    y\\
    z
\end{bmatrix} =
\begin{bmatrix}
    1&0&ax\\
    0&1&ay\\
    0&0&1
\end{bmatrix}
\begin{bmatrix}
    x_{0}\\
    y_{0}\\
    1
\end{bmatrix}
$$

### 旋转
![](imgs/rotate1.png)
$$
x_{0} = r\cos\alpha\\
y_{0} = r\sin\alpha\\
x = r\cos(\alpha+\theta) = r\cos\alpha \cos\theta - r\sin\alpha sin\theta = x_{0}\cos\theta - y_{0}\sin\theta\\
y = r\sin(\alpha + \theta) = r\sin\alpha \cos\theta + r\cos\alpha\sin\theta = y_{0}\cos\theta + x_{0}\sin\theta
$$
$$
\begin{bmatrix}
    x\\
    y\\
    1
\end{bmatrix} =
\begin{bmatrix}
    \cos\theta&-\sin\theta&0\\
    \sin\theta&\cos\theta&0\\
    0&0&1
\end{bmatrix}
\begin{bmatrix}
    x_{0}\\
    y_{0}\\
    1
\end{bmatrix}
$$

### 缩放
$$
x = k1 * x_{0}\\
y = k2 * y_{0}
$$
$$
\begin{bmatrix}
    x\\y\\1
\end{bmatrix} = 
\begin{bmatrix}
   k1&0&0\\
   0&k2&0\\
   0&0&1 
\end{bmatrix}
\begin{bmatrix}
    x_{0}\\y_{0}\\1
\end{bmatrix}
$$

## 原理推导 
getRotationMatrix2D
https://charlesnord.github.io/2017/04/01/rotation/

![](imgs/rotate2.jpg)

# 边缘检测算子
## sobel 
![](imgs/edge-1.png)

## prewitt
![](imgs/edge-2.jpg)

## laplacian
![](imgs/edge-3.jpg)

https://zhuanlan.zhihu.com/p/32269942


# 图像颜色空间
## RGB
```python
'''
各通道取不同的阈值二值化
'''
strawberry = cv2.imread('s.jpg')
lower = np.array([0,0,100])
upper = np.array([40,40,255])
bin = cv2.inRange(strawberry,lower,upper)
```

因为在比较暗的地方，整张图的 RGB 的数值都很低，在比较亮的地方，数值又比较高。 RGB 三个通道的数值都很容易随着光照的改变而改变，无法在复杂的环境中得到自己需要的特定区域

## HSV
色相（Hue) 饱和度(Saturation) 亮度(Value)
H 代表色彩，S 代表颜色的深浅，V 代表着颜色的明暗程度。
在 OpenCV 视觉库中，HSV 的数值被做了一些小的修改， H 的范围调整为 0~180，S 和 V 的范围为 0~255。
当我们采用 HSV 的图像阈值得到某一种颜色时，可以参考颜色分布表，先将 H 通道对应的颜色找到。表格中，每种颜色都对应了一个区间。
即使明度取值 255 也不会变为全白，因为这时，这个取值是指蓝色的亮度，而不是像 RGB 一样表示颜色。饱和度同理。

```python
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #RGB 转为 HSV
H, S, V = cv2.split(HSV)    #分离 HSV 三通道
Lowerred0 = np.array([155,43,35])
Upperred0 = np.array([180,255,255])
mask1 = cv2.inRange(HSV, Lowerred0, Upperred0) 
Lowerred1 = np.array([0,43,35])
Upperred1 = np.array([11,255,255])
mask2 = cv2.inRange(HSV, Lowerred1, Upperred1)    #将红色区域部分归为全白，其他区域归为全黑
Apple = mask1 +mask2
```


## YUV
YUV 色彩空间实际上是把一幅彩色的图片分成了一个表示暗亮程度的亮度信号(Luminance)Y，和两个表示颜色的色度信号(Chrominance)U 和 V。U，V通道分别是蓝色通道和红色通道，Y 通道表示亮度信息。

U 通道数值越高，颜色就越接近蓝色，V 通道数值越高，颜色就越接近红色,Y 通道数值越高，图片则越亮。

为什么会有这种颜色通道呢？其实这是被欧洲的电视系统采用的一种颜色编码方式，主要是为了让信号支持新的彩色电视，但也继续支持黑白电视。如果是黑白电视，只使用 Y 通道信号就足够了

即使是光线发生了很大的改变，V 通道还是能很好的体现出红色来。所以当我们要识别红蓝色物体时，使用 YUV 通道就会有较好的效果。
```python
fruit = cv2.imread("fruits.jpg")
fruit = cv2.cvtColor(fruit,cv2.COLOR_BGR2YUV)
Y,U,V = cv2.split(fruit)
Blueberry = cv2.inRange(U,130,255)
Strawberry = cv2.inRange(V,170,255)
cv2.imshow("blueberry",Blueberry)
cv2.imshow("strawberry",Strawberry)
cv2.waitKey(0)
```

## CMYK
CMYK 色彩空间中，C（cyan）代表青色，M（magenta）代表洋红色，Y（yellow）代表黄色，K（black）代表黑色。

CMYK 主要使用在印刷方面，比如喷墨打印机一般都是使用这四种颜色的墨盒。在 RGB 色彩空间里红色，绿色和蓝色叠加起来的时候是白色，但在 CMYK 色彩空间中，青色，洋红色，黄色叠加起来是黑色。

但是实际情况中，颜色叠加起来会是褐色，所以还是会加上单独的黑色。相比于 RGB，CMYK 更加实用于在白色的介质上打印图像。

# 特征点匹配
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_feature_homography/py_feature_homography.html#py-feature-homography

```python
import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10

img1 = cv2.imread('box.png',0)          # queryImage
img2 = cv2.imread('box_in_scene.png',0) # trainImage

# Initiate SIFT detector
#cv2.SIFT(100) 保留100个特征点
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des1,des2,k=2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
```

接下来透视变换
![](imgs/sift1.png)
```python
if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

else:
    print "Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT)
    matchesMask = None
```
接下来透视变换把图抠出来
```python
pts = pts.reshape(4,2)
w = pts[1][0] - pts[0][0]
h = pts[2][1] - pts[1][1]
pt2 = np.array([[0,0],[w,0],[w,h],[0,h]],dtype='float32')
pt1 = pt1.astype('float32')
M = cv2.getPerspectiveTransform(pt1,pt2)
perspective = cv2.warpPerspective(dst,M,(w,h),cv2.INTER_LINEAR) 
```

