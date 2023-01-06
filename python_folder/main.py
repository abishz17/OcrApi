from paddleocr import PaddleOCR

import os


def PaddleRun(paddle_img):
    print(os.getcwd())
    ocr = PaddleOCR(
        lang="ne", cls_model_dir="../inference/rec_crnn",  use_gpu=False)
    img_path = "./media/"+str(paddle_img)

    output = []
    output_text = ""

    result = ocr.ocr(img_path, rec=True)
    try:
        for line in result:
            for each in line:
                text = each[1][0]
                output.append(text)
                output_text += text + " "
        print("Text Area:", result)

    except IndexError:
        for line in result:
            text = each[0][0]
            output.append(text)
            output_text += text + " "
        print("Text Area:", output_text)
    return output_text
# print("Text Area:",result)
