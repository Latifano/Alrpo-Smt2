#import numpy as np

#a = np.array([1, 2, 3, 4])
#b = np.array([5, 6, 7, 8])
# print(a+b)


from PIL import Image

im = Image.open("romi.jpeg")
print('Format File :' + im.format)
print('Ukurang File :' + str(im.format))
print('Mode File :' + im.mode)

im.show()
