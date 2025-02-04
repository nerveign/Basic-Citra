import numpy as np
import cv2 as cv

image_path = 'frame_1.png'
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
    get_grayscale = np.zeros((rows,cols))

    for i in range(rows):
        for j in range(cols):
            get_grayscale[i,j] = 0.299 * r[i,j] + 0.587 * g[i,j] + 0.114 * b[i,j]

    return get_grayscale.astype(np.uint8)


# ubah gambar Grayscale menjadi Black and White
def blackWhiteFilter(image, treshold=128):
    rows = len(image)
    cols = len(image[0])

    grayscale = grayScale(image)    
    get_blackwhite = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            if grayscale[i,j] >= treshold:
                get_blackwhite[i,j] = 255
            else:
                get_blackwhite[i,j] = 0
    
    return get_blackwhite.astype(np.uint8)


citra_grayscale = grayScale(citra)
citra_blackwhite = blackWhiteFilter(citra)

cv.imshow("Soseo Black and White", citra_blackwhite)
cv.imwrite("frame1_GrayScale.png", citra_grayscale)
cv.imwrite("frame1_BlackWhite.png", citra_blackwhite)
cv.waitKey()