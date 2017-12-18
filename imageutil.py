from PIL import Image

def openimg(path):
    """
    This function returns the pixel values.
    The imput is a png file location.
    """
    file_name = path  # 导入自己 的图片地址
    # in terminal 'mogrify -format png *.jpg' convert jpg to png
    img = Image.open(file_name).convert('L')

    # resize to 28x28
    if img.size[0] != 28 or img.size[1] != 28:
        img = img.resize((28, 28))

    img.save("C:/Users/hp/Downloads/tensorflow/mni/sample.png")

    tv = list(img.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    # print(tva)
    return tva


if __name__ == "__main__":
    a = openimg("C:/Users/hp/Downloads/tensorflow/mni/333.jpg")
    print(a.__len__())