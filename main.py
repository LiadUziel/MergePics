
from PIL import Image

PICS_NUM = 32


def merge_width(image1, image2):
    new_width = Image.new("RGB", (image1.width + image2.width, image1.height))

    new_width.paste(image1, (0, 0))
    new_width.paste(image2, (image1.width, 0))

    return new_width


def merge_height(image1, image2):
    new_height = Image.new("RGB", (image1.width, image1.height + image2.height))

    new_height.paste(image1, (0, 0))
    new_height.paste(image2, (0, image1.height))

    return new_height


def merge_pics():
    new_image = None
    temp_line = Image.open("Pics/image_1_1.jpeg");
    lines = []
    for row in range(1, PICS_NUM + 1):
        temp_line = Image.open("Pics/image_" + str(row) + "_1.jpeg");
        for col in range(2, PICS_NUM + 1):
            print("image_" + str(row) + "_" + str(col) + ".jpeg")
            temp_line = merge_width(temp_line, Image.open("Pics/image_" + str(row) + "_" + str(col) + ".jpeg"))
        lines.insert(row, temp_line)

    new_image = lines[0]
    for i in range(1, len(lines) - 1):
        new_image = merge_height(new_image, lines[i])

    new_image.save("new_image.jpeg")
    new_image.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    merge_pics()

