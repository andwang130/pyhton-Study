from PIL import Image

im=Image.open('new.jpg')#打开一个图像，返回的是一个pil的对象
w,h=im.size  #size可以获得图像的大小
def image_joint(imgefiles,rank_num):
    list_num=len(imgefiles)
    width,height=imgefiles[0].size
    if list_num%rank_num!=0:
        new_height_max=(list_num//rank_num)*height+height
    else:
        new_height_max = (list_num // rank_num) * height
    target = Image.new('RGB', (width * rank_num, new_height_max)) #生成新的图片
    print(target.size)
    letf=0
    right=width
    height_seiz=0
    height_seiz_r=height
    num=1
    for i in imgefiles:

        target.paste(i,(letf,height_seiz,right,height_seiz_r))#在新的图片不同位置插入图片，形成拼接
        print(letf,right)
        letf +=width
        right+= width
        if num%rank_num==0:
            height_seiz+=height
            height_seiz_r+=height
            letf=0
            right = width
        num += 1
    target.show()
imgefiles=[im for i in range(14)]
image_joint(imgefiles,3)
# target.paste(im, (0, 0, w, h))
# target.paste(im, (w, 0, w * 2, h))
# target.paste(im, (w * 2, 0, w * 3, h))
# target.paste(im, (w * 3, 0, w * 4, h))
# target.paste(im, (0, h, w, h * 2))
# target.paste(im, (w, h, w * 2, h * 2))
# target.paste(im, (w * 2, h, w * 3, h * 2))
# target.paste(im, (w * 3, h, w * 4, h * 2))