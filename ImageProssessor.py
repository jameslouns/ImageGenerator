import glob
import os
import numpy
from PIL import Image
from google_images_download import google_images_download


def download_pics(keyword, limit):
    ImageSearch = google_images_download.googleimagesdownload()
    SearchArgs = {"keywords": keyword, "limit": limit, "format": "jpg"}
    ImageSearch.download(SearchArgs)
    return


def format_files(width, height, keyword):
    for file_name in os.listdir("./downloads/" + keyword):
        file_name = "./downloads/" + keyword + "/" + file_name
        img = Image.open(file_name)
        img = img.resize((width, height))
        data = numpy.asarray(img)
        print(data.shape)
    return


def main():
    keyword = input("Input Keyword: ")
    limit = input("Input Number of Pictures: ")
    try:
        int(limit)
    except ValueError:
        print("Must Input a Number for limit")
        return limit
    width = input("Input Picture Width: ")
    height = input("Input Picture Height: ")
    try:
        width = int(width)
        height = int(height)
    except ValueError:
        print("Width and Height must be integer numbers")
        return width, height
    download_pics(keyword, limit)
    format_files(width, height, keyword)


if __name__ == "__main__":
    main()