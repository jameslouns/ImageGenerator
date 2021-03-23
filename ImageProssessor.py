import os
import numpy as np
from PIL import Image
from google_images_download import google_images_download
import NeuralNetwork
from matplotlib import cm


def download_pics(keyword, limit):
    ImageSearch = google_images_download.googleimagesdownload()
    SearchArgs = {"keywords": keyword, "limit": limit, "format": "jpg"}
    ImageSearch.download(SearchArgs)
    return


def format_files(width, height, keyword):
    pictures_data = []
    i = 0
    for file_name in os.listdir("./downloads/" + keyword):
        file_name = "./downloads/" + keyword + "/" + file_name
        img = Image.open(file_name)
        img = img.resize((width, height))
        data = np.asarray(img)
        data = data.flatten()
        pictures_data.append(data)
        i = i+1
    return i, np.array(pictures_data)


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
    limit, Ttrain = format_files(width, height, keyword)
    Xtrain = []
    for i in range(int(limit)):
        Xtrain.append(np.full(width, i).flatten())
    Xtrain = np.asarray(Xtrain)
    network = NeuralNetwork.NeuralNetwork(Xtrain.shape[1], [1000, 1000, 10000, 1000], Ttrain.shape[1])
    network.train(Xtrain, Ttrain, 500, .01, method='adam')
    '''
    for i in range(int(limit)):
        generated_pic_data = network.use(Xtrain[i])
        generated_pic_data = generated_pic_data.reshape(width, height, 3)
        generated_pic = Image.fromarray(np.uint8(generated_pic_data))
        generated_pic.save(keyword+str(i)+"_Cursed.jpg")
    '''
    for i in range(5):
        test = network.use(np.random.randint(0, limit, size=width).flatten())
        print(test)
        test = test.reshape(width, height, 3)
        test_img = Image.fromarray(np.uint8(test))
        test_img.save("/Output/"+keyword+str(i)+".jpg")


if __name__ == "__main__":
    main()
