#!/usr/bin/env python

import cv2 as cv
from tests_common import NewOpenCVTests


class imread_rgb_test(NewOpenCVTests):
    def test_imread_rgb(self):
        path = self.extraTestDataPath + '/cv/shared/lena.png'
        bgr = cv.imread(path)
        rgb = cv.imread_rgb(path)
        self.assertEqual(bgr.shape, rgb.shape)
        bgr2rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
        self.assertEqual(cv.norm(rgb, bgr2rgb, cv.NORM_INF), 0.0)


if __name__ == '__main__':
    NewOpenCVTests.bootstrap()
