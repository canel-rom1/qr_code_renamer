#!/usr/bin/env python3

import cv2


def qr_code_value(img):
    """
    Return a string. Value is QR-code content
    Parameter img : path to image
    """
    image = cv2.imread(str(img))
    qr_code_detector = cv2.QRCodeDetector()
    decoded_text, points, matrix = qr_code_detector.detectAndDecode(image)
    return decoded_text
