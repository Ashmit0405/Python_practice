from PIL import Image
import pytesseract as pt

img=Image.open('./eg.png')
text=pt.image_to_string(img,lang='eng')
print(text)