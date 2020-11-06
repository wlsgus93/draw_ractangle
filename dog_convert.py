import cv2
import os
import time
# path="/home/ubuntu/pythonProject/opencv4/data/lena.jpg"
def act(actResize,actRotate,actBlur,actCrop,path):
    src = cv2.imread(path)
    if actResize:
        size = (256, 256)
        src = cv2.resize(src, dsize=size, interpolation=cv2.INTER_AREA)
        print("resize succeed")
    else:
        pass
    if actRotate:
        height, width, channel = src.shape
        # 회전 중심, 회전각, scale
        matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
        src = cv2.warpAffine(src, matrix, (width, height))
        print("rotate succeed")
    else:
        pass
    if actBlur:
        src = cv2.blur(src, (4, 4), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
        print("Blur succeed")
    else:
        pass
    if actCrop:
        src = src[100:600, 200:700]
        print("actCrop succeed")
    else:
        pass


    return src
    # cv2.imshow("src", src)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

if __name__=="__main__":

    path = "/home/ubuntu/pythonProject/opencv4/dogs"
    fileList = os.listdir(path)
    counter=0
    new_dir_path = './convert_dogs{}'.format(time.strftime('%H_%M'))
    os.mkdir(new_dir_path)
    for filename in fileList:

        srcpath = os.path.join(path, filename)
        convert_file=act(1, 0, 0, 0, srcpath) #적용 1 미적용 0 (앞에부터 resize rotate blur crop)

        cv2.imwrite("./convert_dogs/dog{}.jpg".format(counter), convert_file)
        counter = counter + 1
