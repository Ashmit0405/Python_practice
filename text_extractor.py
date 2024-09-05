from pdf2image import convert_from_path as cfp
from PIL import Image
import pytesseract as pt
import os

folder_path="./temp"
contents=os.listdir(folder_path)

files=[f for f in contents if os.path.isfile(os.path.join(folder_path,f))]

for f in files:
    f_name,ex=os.path.splitext(f)
    file_path=os.path.join(folder_path,f)
    
    if(ex=='.png'):
        img=Image.open(file_path)
        text=pt.image_to_string(img,lang='eng')
        print(text)
    
    elif(ex==".pdf"):
        pages=cfp(file_path)#one image per page
        for i,page in enumerate(pages):
            text=pt.image_to_string(page)
            print(f"Text from page {i+1}: \n",text)