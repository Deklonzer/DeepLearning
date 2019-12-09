from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import os

__THRESHOLD_VALUE__ = 200
__THRESHOLD_MASK__ = 160

if __name__ == '__main__':
    base_directory = './2017-IWT4S-HDR_LP-dataset/crop_h1'
    images = os.listdir(base_directory)

    for image in images:
        with Image.open(''.join([base_directory, '/', image])) as img:
            width, height = img.size
            print(width, height)

            monochrome_img = img.convert('L').point(
                lambda x: 255 if (x > __THRESHOLD_VALUE__) else 0, mode='1')

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
            plt.show()

            flip = np.asarray(composite)
            result = Image.fromarray(flip.reshape(height, width), '1')

            #plt.imshow(result)
            #plt.show()

            composite.save(image)

            #composite = composite.filter(ImageFilter.FIND_EDGES)
