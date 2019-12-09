from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import os

__THRESHOLD_VALUE__ = 220
__THRESHOLD_MASK__ = 160

if __name__=='__main__':
    arr = os.listdir("./2017-IWT4S-HDR_LP-dataset/crop_h1")
    print(arr)

with Image.open('./2017-IWT4S-HDR_LP-dataset/crop_h1/I00010.png') as img:
    monochrome_img = img.conver('L').point(
        lambda x: 255 if (x > __THRESHOLD_VALUE__) else 0, mode='1')
    #mask_result_0 = np.asarray(mask_0, dtype=np.int).flatten()

    mask = img.convert('L').point(
        lambda x: 255 if x > __THRESHOLD_MASK__ else 0, mode='1')

    white_img = Image.new('1', monochrome_img.size, 0)

    composite = Image.composite(monochrome_img, white_img, mask)
    '''
    mask_result_1 = np.asarray(mask_1, dtype=np.int).flatten()

    print(img.size)

    for index in range(mask_result_0.size):
        if (not mask_result_0[index]) and (not mask_result_1[index]):
            pass
            
    result = Image.fromarray(mask_result_1.reshape(129, 348), 'L')
    '''
    plt.imshow(composite)
    #plt.show()

    #composite = composite.filter(ImageFilter.FIND_EDGES)
    composite.save('aaa.png')
