import os
import cv2
import numpy as np
import shutil
#from skimage.filters import threshold_sauvola
from paddleocr import PaddleOCR
def extract_words( orig_img_path):
  # new_direcory = "preprocess_output/words/"


  #orig_img_path = 'final_images/8_crop.jpg'

  # # Parsing the image_number for folder name
  # filename = os.path.basename(orig_img_path)
  # file_num, ext = os.path.splitext(filename)

  # new_dir = new_directory+file_num+"/"
  # print(new_dir)

  new_dir = "/home/nepaliocr/apps/backend/python_folder/preprocess_output/words/"

  #deleting directory for words
  if os.path.exists(new_dir):
    shutil.rmtree(new_dir)

  #creating directory for words
  if not(os.path.exists(new_dir)):
      os.makedirs(new_dir) 

  img_path2 = orig_img_path
  image = cv2.imread(img_path2)

  image = orig_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  # Create a blank image
  blank = np.zeros(image.shape, dtype='uint8')
  # cv2.imshow('Blank', blank)

  # Grayscale the image
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # cv2.imshow('Gray', gray)
  # plt.imshow(gray)

  # Blurring the image
  blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
  # plt.imshow(blur)


  # Using PaddleOCR
  ocr=PaddleOCR(lang='ne')
  result = ocr.ocr(blur)

  # Extracting the boxes, texts and scores from results
  lines = []
  for all_words in result:
    for word in all_words:
      lines.append(word)
  print(len(lines))

  # save_ocr(img_path, out_path, result, font)

  # Do this not for the single word image 
  if len(lines)==0:
    pass # call the function for text recognition

  else:
    boxes = []
    txts = []
    scores = []


    # Checking if it is multiple line or Single line

    # For multiple lines, its array has one more dimension
    if len(lines)>1:
      for all_lines in result:
        for line in all_lines:
          boxes.append(line[0])
          txts.append(line[1][0])
          scores.append(line[1][1])

    # For single line, its array has one less dimension
    else:
      for line in lines:
        boxes.append(line[0])
        txts.append(line[1][0])
        scores.append(line[1][1])

    print(txts)
    # Highlighting the texts in the image
    for count, box in enumerate(boxes):
      box = np.reshape(np.array(box), [-1, 1, 2]).astype(np.int64)
      image = cv2.polylines(np.array(image), [box], True, (0, 0, 255), 10)


      # Cropping each word with the loop

      # first finding the coordinates of a box
      for first, second, third, fourth in zip(box[::4], box[1::4], box[2::4], box[3::4]):
        # print(first, second, third, fourth, "\n")
        coords = [(first[0][0], first[0][1]), (second[0][0], second[0][1]), (third[0][0], third[0][1]), (fourth[0][0], fourth[0][1])]
        # coords = [(3612, 2186), (3758, 2186), (3758, 2271), (3612, 2271)]
        # print(coords, "\n")

        # create a mask
        mask = np.zeros_like(orig_image[:,:,0])
        # Draw the irregular shape on the mask image
        cv2.fillPoly(mask, np.array([coords]), color=1)
        # Apply the mask to the original image using the "bitwise_and" function
        masked_img = cv2.bitwise_and(orig_image, orig_image, mask=mask)
        # Cropping the image
        x1 = min(coords[0][0], coords[1][0], coords[2][0], coords[3][0])
        x2 = max(coords[0][0], coords[1][0], coords[2][0], coords[3][0])
        y1 = min(coords[0][1], coords[1][1], coords[2][1], coords[3][1])
        y2 = max(coords[0][1], coords[1][1], coords[2][1], coords[3][1])

        new_img = masked_img[y1:y2, x1:x2]
        cv2.resize(new_img,(320,32),interpolation=cv2.INTER_AREA)
        cv2.imwrite(new_dir+str(count)+".jpg", new_img)
        # files.download(file_num+str(count)+".jpg") 
        # plt.imshow(masked_img)

    # Draw the read picture
    #plt.figure(figsize=(10, 10))
    #plt.axis('off')
    #plt.imshow(image)

    # call the function for text recognition using loop for all images
