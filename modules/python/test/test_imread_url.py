import os
import sys
import urllib.error
import pytest
import cv2 as cv

# ensure sample utilities are on path
SAMPLES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../samples/python'))
if SAMPLES_DIR not in sys.path:
    sys.path.insert(0, SAMPLES_DIR)
from common import imread_url


def test_imread_url():
    url = 'https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg'
    try:
        img = imread_url(url, cv.IMREAD_GRAYSCALE)
    except urllib.error.URLError:
        pytest.skip('No internet access to fetch test image')
    assert img is not None
    assert img.ndim == 2
    h, w = img.shape[:2]
    assert h > 0 and w > 0
