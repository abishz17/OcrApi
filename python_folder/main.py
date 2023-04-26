from paddleocr import PaddleOCR

import os


def PaddleRun(paddle_img):

    ocr = PaddleOCR(lang="ne", rec_model_dir="./inference/rec_crnn",
                    use_gpu=False, cls_model_dir=None)
    img_path = "/home/nepaliocr/apps/media/"+str(paddle_img)

    output = []
    output_text = ""

    result = ocr.ocr(img_path, rec=True)

    lines = []
    for all_lines in result:
        for line in all_lines:
            lines.append(line)
         #   print(len(lines))
    boxes = []
    txts = []
    scores = []
    if len(lines)>1:
        for all_lines in result:
            for line in all_lines:
                boxes.append(line[0])
                txts.append(line[1][0])
                scores.append(line[1][1])
    else:
        for line in line:
            boxes.append(line[0])
            txts.append(line[1][0])
            scores.append(line[1][1])
    print("Text Area:", txts)
    return txts
    # print("Text Area:",result)
