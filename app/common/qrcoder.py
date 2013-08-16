# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import qrcode

def CreateQrcode(data,saveFile,boxSize=6,border=2):
    qr = qrcode.QRCode(box_size=boxSize,border=border)
    qr.add_data(data)
    qr.make()
    img = qr.make_image()
    img.save(saveFile)
    return True


if __name__=='__main__':
    CreateQrcode(u'http://www.bandao.cn','c:/1.jpg')