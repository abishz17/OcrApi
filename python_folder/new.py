import subprocess
import sys
import re
import os
import shutil
import cv2
sys.path.append('/home/nepaliocr/apps/backend/python_folder/')
import numpy as np
import image_processing


def PaddleRun(paddle_img):
    image_path = "/home/nepaliocr/apps/media/"+str(paddle_img)
    script_path = "/home/nepaliocr/apps/backend/python_folder/script.sh"
    #print(image_path)
    #subprocess.check_call(["/home/nepaliocr/apps/backend/python_folder/script.sh", image_path])
    #os.system(' /home/nepaliocr/apps/backend/python_folder/script.sh {}' .format(str(image_path)))
    image_processing.extract_words(image_path)

    copy_image_path = '/home/nepaliocr/apps/backend/python_folder/preprocess_output/copy_image.png'
    print(copy_image_path)
    if os.path.isfile(copy_image_path):
        os.remove(copy_image_path)
    shutil.copyfile(image_path, copy_image_path)
      
    output_final=[]
    for each in os.listdir('/home/nepaliocr/apps/backend/python_folder/preprocess_output/words'):
        each_image='/home/nepaliocr/apps/backend/python_folder/preprocess_output/words/'+each
        
        #image = cv2.imread(image_path)
        # Create a blank image
        #blank = np.zeros(image.shape, dtype='uint8')
        # cv2.imshow('Blank', blank)

        # Grayscale the image
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # plt.figure(figsize=(10, 10))
        # plt.axis('off')
        # plt.imshow(gray)

        # Blurring the image
        #blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
        # plt.imshow(blur)

        # Adaptive Thresholding
        #adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10)
        # threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        #plt.figure(figsize=(10, 10))
        #plt.axis('off')
        #plt.imshow(adaptive_thresh)
        #thresh_img_path='/home/nepaliocr/apps/backend/python_folder/preprocess_output/words/thresh.jpg'
        #if (os.path.isfile(thresh_img_path)):
         #   os.remove(thresh_img_path)
        #cv2.resize(adaptive_thresh,(320,32),interpolation=cv2.INTER_AREA)
        #cv2.imwrite('/home/nepaliocr/apps/backend/python_folder/preprocess_output/words/thresh.jpg',adaptive_thresh)
        
        #new_image_path = cv2.imread(thresh_img_path)
        # plt.imshow(thresh)
        # new_image_path = thresh


        os.system(' /home/nepaliocr/apps/backend/python_folder/script.sh {}' .format(str(each_image)))    


        #os.system(' /path/shellscriptfile.sh {} {}' .format(str(var1), str(var2)) 
        with open("/home/nepaliocr/apps/backend/python_folder/output.txt","r") as file:
            line=file.read()
            each=line.split(' ')
            for (index,item) in enumerate(each):
                if item == 'result:':
                    new=each[index+1].split('\t')[0]+'\n'
                    print(new)
                    output_final.append(new)

    
    return output_final

