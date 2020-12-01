import cv2
import numpy as np

def main():
    image = cv2.imread('Lenna.png')
    #converting image to gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #convert image to binary
    (threshold,binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    filter = np.array([(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1),(1,1,1,1,1,1,1)])
    #shape of image
    shape = binary.shape
    #shape of filter
    filter_shape = filter.shape
    #converting image range from 0 to 255 to 0 to 1
    binary = binary/255
    rows = shape[0]+filter_shape[0]-1
    cols = shape[1]+filter_shape[1]-1
    new_arr = np.zeros((rows,cols))

    for i in range(shape[0]):
        for j in range(shape[1]):
            #filling the new zero array with the image/padding image
            new_arr[i+np.int((filter_shape[0]-1)/2),j+np.int((filter_shape[1]-1)/2)] = binary[i,j]

    for i in range(shape[0]):
        for j in range(shape[1]):
            #select a 7x7 window from the padded  image
            window = new_arr[i:i+filter_shape[0],j:j+filter_shape[1]]
            result = (window==filter)
            final = np.all(result==True)
            if final:
                binary[i,j]=1
            else:
                binary[i,j]=0

    cv2.imshow('final image', binary)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()

