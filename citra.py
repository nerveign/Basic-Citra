import numpy as np
import cv2 as cv

# Import gambar
image_path = 'frame_1.png'
citra = cv.imread(image_path)

# Panjang dan lebar ukuran gambar (dalam pixel)
rows = len(citra)
cols = len(citra[0])

# Fungsi untuk mengambil matriks warna blue, green, red dari sebuah gambar
def getColors(image):
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]
    return [b,g,r]

# Fungsi untuk mengubah sebuah gambar menjadi filter grayscale
def grayScale(image, rows, cols):
    b, g, r = getColors(image)
    get_grayscale = np.zeros((rows,cols))

    for i in range(rows):
        for j in range(cols):
            get_grayscale[i,j] = 0.299 * r[i,j] + 0.587 * g[i,j] + 0.114 * b[i,j]

    return get_grayscale.astype(np.uint8)


citra_grayscale = grayScale(citra, rows, cols)
cv.imshow("Soseo Grayscale", citra_grayscale)
cv.waitKey()