from PIL import Image
import numpy as np


def lsb_image(input_image_path, output_image_path):
    original_image = Image.open(input_image_path)
    img_array = np.array(original_image)
    lsb_img_array = np.bitwise_and(img_array, 1)
    lsb_img = Image.fromarray(lsb_img_array.astype('uint8') * 255, 'RGB')
    lsb_img.save(output_image_path)


if __name__ == '__main__':
    lsb_image('output_test_stegged_image.bmp', 'output_lsb_image_2.png')
