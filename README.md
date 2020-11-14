# cv-picture-in-picture-window
OpenCVでピクチャーインピクチャーのように表示するサンプルです。<br>
![bu19j-mplzq](https://user-images.githubusercontent.com/37477845/99147752-c70f9780-26c6-11eb-8bf5-4f9bc73d8dc5.gif)

# Requirement 
* OpenCV 3.4.2 or later

# Demo
デモの実行方法は以下です。
```bash
python sample.py
```

# How to use
以下の流れで呼び出してください。
CvWPictureInPictrueWindowクラス作成時には、ウィンドウ名、スライダー上のライン色、ライン太さ、小窓の比率(元画像比)、小窓位置(X座標、Y座標それぞれの割合)を指定出来ます。<br>
省略した場合は、それぞれ'debug'、(255, 255, 255)、1、0.4、(0.55, 0.55)になります。

```python
from cv_picture_in_picture_window import CvWPictureInPictrueWindow

cvwindow = CvWPictureInPictrueWindow(
    window_name='debug',
    line_color=(255, 255, 255),
    line_thickness=1,
    pip_ratio=0.4,
    pip_position=(0.55, 0.55)
)

# [省略]

while True:
    cvwindow.imshow(image, pip_image)
    key = cv.waitKey(1)
```

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
cv-picture-in-picture-window is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
