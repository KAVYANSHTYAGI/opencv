#!/usr/bin/env python
"""Sample demonstrating how to load an image from a web URL with OpenCV."""

import sys
import cv2 as cv
from common import imread_url


def main():
    if len(sys.argv) < 2:
        print("Usage: imread_url.py <image_url>")
        return
    url = sys.argv[1]
    img = imread_url(url)
    if img is None:
        print("Failed to load image from", url)
        return
    print("Loaded image shape:", img.shape)
    cv.imshow('URL image', img)
    cv.waitKey(0)


if __name__ == "__main__":
    main()
