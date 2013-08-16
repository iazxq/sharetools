# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
import Image




def create_small_pic(image,dst_w,dst_h,quality,dst_img):
    '''从文件创建小图片，指定图片宽度，高度，保存文件名
       需要对图片进行压缩和剪切，保证最优质量
    '''
    result = True

    #try:
    path,filename = os.path.split(dst_img)
    if not os.path.exists(path):
        os.makedirs(path)


    ori_w,ori_h = image.size
    if (ori_w<dst_w):
        dst_w = ori_w
    if ori_h < dst_h:
        dst_h = ori_h


    dst_scale = float(dst_h) / dst_w #目标高宽比
    ori_scale = float(ori_h) / ori_w #原高宽比

    if ori_scale >= dst_scale:
        #过高
        width = ori_w
        height = int(width*dst_scale)

        x = 0
        y = (ori_h - height) / 3

    else:
        #过宽
        height = ori_h
        width = int(height/dst_scale)

        x = (ori_w - width) / 2
        y = 0


    #裁剪
    box = (x,y,width+x,height+y)
    #这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
    #所包围的图像，crop方法与php中的imagecopy方法大为不一样
    newIm = image.crop(box)
    im = None

    #压缩
    ratio = float(dst_w) / width
    newWidth = int(width * ratio)
    newHeight = int(height * ratio)
    newIm.resize((newWidth,newHeight),Image.ANTIALIAS).save(dst_img,quality=quality)

def create_small_pic_from_file(file,dst_w,dst_h,quality,dst_img):
    '''从文件创建小图片，指定图片宽度，高度，保存文件名
       需要对图片进行压缩和剪切，保证最优质量
    '''
    result = True

    #try:
    path,filename = os.path.split(dst_img)
    if not os.path.exists(path):
        os.makedirs(path)

    im = Image.open(file)
    create_small_pic(im,dst_w,dst_h,quality,dst_img)


if __name__ == '__main__':
    create_small_pic('d:/1.jpg',156,180,100,'d:/m1.jpg')
