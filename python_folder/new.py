import subprocess
import sys
import re
import os

def PaddleRun(paddle_img):
    image_path = "/home/nepaliocr/apps/media/"+str(paddle_img)
    script_path = "/home/nepaliocr/apps/backend/python_folder/script.sh"
    #print(image_path)
    #subprocess.check_call(["/home/nepaliocr/apps/backend/python_folder/script.sh", image_path])
    os.system(' /home/nepaliocr/apps/backend/python_folder/script.sh {}' .format(str(image_path)))
    #os.system(' /path/shellscriptfile.sh {} {}' .format(str(var1), str(var2)) 
    with open("/home/nepaliocr/apps/backend/python_folder/output.txt","r") as file:
        content = file.readlines()
        content = str(content).split(' ')
        #print(content)
        output_final = "empty"
        for count, text in enumerate(content):
            #print(text)
            if text=="result:":
                output_final = str(content[count+1])
                print(output_final)
    
    

    
    return output_final

