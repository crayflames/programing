#! /usr/bin/python3.5
from PIL import Image
# 若要把 Lenna 的臉部模糊, 可用 pillow 的濾鏡功能
from PIL import ImageFilter

lenna = Image.open(r'/home/roger/Downloads/lenna_sharp.jpg')
print(lenna.size)
#box = (160, 51, 406, 512)
#cropLenna = lenna.crop(box)
# 將截取的部分用濾鏡模糊
lennaBlurred = lenna.filter(ImageFilter.BLUR)
lennaBlurred.save(r'/home/roger/Downloads/lenna_sharp.jpg')
# 若模糊的效果不夠，可用 for loop 把同樣的濾鏡套用很多次
for i in range(10):
    lennaBlurred = lennaBlurred.filter(ImageFilter.BLUR)
lennaBlurred.save(r'/home/roger/Downloads/lenna_sharp.jpg')
box = (160, 51, 406, 512)
# 用 .paste() 將模糊後的部分貼囘原本的影像（用 box tuple 指定原圖要被貼上的位置）
lenna.paste(lennaBlurred, box)
lenna.save(r'/home/roger/Desktop/Lenna_sharp.jpg')