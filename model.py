from PIL import Image
import numpy as np
from pprint import pprint


def get_image(path):
    input_set = Image.open(path)
    input_set = input_set.convert('1')
    return input_set


def slice_(image):
    images = {}
    for i in range(1, 11):
        images[i] = []

    for i in range(1, 11):
        for j in range(1, 11):
            tile = image.crop(((i - 1) * 40, (j - 1) * 40, i * 40,  j * 40))
            resized_tile = resize_image(tile)
            np_img = np.array(resized_tile)
            images[i].append(np_img)

    return images


def resize_image(img):
    x1, y1, x2, y2 = 0, 0, 0, 0
    b = False

    for i in range(40):
        for j in range(40):
            if img.getpixel((i, j)) == 0:
                x1 = i
                b = True
                break
        if b:
            break

    b = False

    for i in range(40):
        for j in range(40):
            if img.getpixel((39-i, 39-j)) == 0:
                x2 = 39-i
                b = True
                break
        if b:
            break

    b = False

    for i in range(40):
        for j in range(40):
            if img.getpixel((j, i)) == 0:
                y1 = i
                b = True
                break
        if b:
            break

    b = False

    for i in range(40):
        for j in range(40):
            if img.getpixel((39-j, 39-i)) == 0:
                y2 = 39-i
                b = True
                break
        if b:
            break
    cropped = img.crop((x1, y1, x2, y2)).copy()
    resized = cropped.resize((40, 40))

    return resized

def pot_and_sum(diff):
    sums = []

    for i in sorted(diff.keys()):
        sum = 0
        for j in diff[i]:
            sum += 1000000 / (1 + j*j)
        sums.append(sum)
    return sums


def compare(imgs, in_img):
    diff = {}
    for i in range(1, 11):
        diff[i] = []
    for i in imgs.keys():
        for j in imgs[i]:
            diff[i].append(np.count_nonzero(j ^ in_img))
    return diff


if __name__ == '__main__':
    pprint(pot_and_sum(compare(slice_(get_image("learn/input/all.bmp")), resize_image(get_image("learn/input/2.bmp")))))





