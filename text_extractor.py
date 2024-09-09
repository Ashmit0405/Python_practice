from pdf2image import convert_from_path as cfp
from PIL import Image
import pytesseract as pt
import os

folder_path="./temp"
contents=os.listdir(folder_path)
custom_config = r'--psm 6'
files=[f for f in contents if os.path.isfile(os.path.join(folder_path,f))]

for f in files:
    f_name,ex=os.path.splitext(f)
    file_path=os.path.join(folder_path,f)
    
    if(ex=='.png' or ex=='.jpeg'):
        print(file_path)
        print("Change Line:\n")
        img=Image.open(file_path)
        text=pt.image_to_string(img, lang='tel+eng', config='--psm 6')
        print(text)
    
    elif(ex==".pdf"):
        pages=cfp(file_path)#one image per page
        for i,page in enumerate(pages):
            text=pt.image_to_string(page,config=custom_config)
            print(f"Text from page {i+1}: \n",text)