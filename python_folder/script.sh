#!/bin/bash
arg=$1
echo $arg
source /home/nepaliocr/apps/env/bin/activate
cd /home/nepaliocr/apps/backend/PaddleOCR
python3 tools/infer_rec.py -c configs/rec/multi_language/rec_devanagari_lite_train.yml -o Global.infer_img=$arg | grep result > /home/nepaliocr/apps/backend/python_folder/output.txt
cd /home/nepaliocr/apps/backend
