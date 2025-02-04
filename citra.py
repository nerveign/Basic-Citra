import numpy as np
import cv2 as cv

image_path = 'frame_2.png'
citra = cv.imread(image_path)

# Ambil warna RGB dari gambar
def getColors(image):
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]
    return [b,g,r]

# ubah gambar menjadi filter grayscale
def grayScale(image):
    rows = len(image)
    cols = len(image[0])
    b, g, r = getColors(image)
    grayscale = np.zeros((rows,cols))

    for i in range(rows):
        for j in range(cols):
            grayscale[i,j] = 0.299 * r[i,j] + 0.587 * g[i,j] + 0.114 * b[i,j]

    return grayscale.astype(np.uint8)


# ubah gambar Grayscale menjadi Black and White
def blackWhiteFilter(image, treshold=128):
    rows = len(image)
    cols = len(image[0])
    grayscale = grayScale(image)    
    blackwhite = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            blackwhite[i,j] = 255 if grayscale[i,j] >= treshold else 0
    
    return blackwhite.astype(np.uint8)


citra_grayscale = grayScale(citra)
citra_blackwhite = blackWhiteFilter(citra, 98)

cv.imshow("Grayscale", citra_grayscale)
cv.waitKey()