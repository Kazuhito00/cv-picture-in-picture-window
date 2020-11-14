import numpy as np
import cv2 as cv


class CvWPictureInPictrueWindow(object):
    def __init__(
            self,
            window_name='debug',
            line_color=(255, 255, 255),
            line_thickness=0,
            pip_ratio=0.4,
            pip_position=(0.55, 0.55),
    ):
        self.window_name = window_name
        self.line_color = line_color
        self.line_thickness = line_thickness
        self.pip_ratio = pip_ratio
        self.pip_position = pip_position

        cv.namedWindow(self.window_name)

    def imshow(self, image1, image2):
        image1_height, image1_width = image1.shape[0], image1.shape[1]
        image2_height = int(image1_height * self.pip_ratio)
        image2_width = int(image1_width * self.pip_ratio)

        image2 = cv.resize(image2, (image2_width, image2_height))

        image2_x = int(image1_width * self.pip_position[0])
        if image2_x + image2_width > image1_width:
            image2_width = image1_width - image2_x
        image2_y = int(image1_height * self.pip_position[1])
        if image2_y + image2_height > image1_height:
            image2_height = image1_height - image2_y

        image1[image2_y:image2_height + image2_y,
               image2_x:image2_width + image2_x] = image2[0:image2_height,
                                                          0:image2_width]

        if self.line_thickness > 0:
            cv.rectangle(image1, (image2_x, image2_y),
                         (image2_x + image2_width, image2_y + image2_height),
                         self.line_color, self.line_thickness)

        cv.imshow(self.window_name, image1)

        return
