# -*- coding: utf-8 -*-
"""IPCV_Lab9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CtxuXZQIrCZZoLXMnrsE3tN2O6WdLTkI
"""

import cv2
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
import numpy as np
import math
import random

img = cv2.imread('/content/WhatsApp Image 2023-04-09 at 10.54.13.jpg')

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

img.shape

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

F = np.fft.fft2(img)
Fshift = np.fft.fftshift(F)
M,N = img.shape
H = np.zeros((M,N), dtype=np.float32)

D0 = 50
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H[u,v] = np.exp(-(D**2)/(2*(D0**2)))

plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()

Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()

"""## High pass filter"""

H = 1 - H
plt.imshow(H, cmap='gray')
plt.axis('off')
plt.show()
Gshift = Fshift * H
G = np.fft.ifftshift(Gshift)
g = np.abs(np.fft.ifft2(G))
plt.imshow(g, cmap='gray')
plt.axis('off')
plt.show()

"""**Conclusion**-A low pass Gaussian filter smooths an image by removing high-frequency information, while a high pass Gaussian filter enhances edges and other high-frequency features by suppressing low-frequency information."""

