# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:39:29 2021

@author: wayne
count person speak workd number
tip: 前3 n[:3]=0~2、中間2~4 n[2:4]、結尾 n[-2:]
"""
   
def read_file (filename):
    lines = [] #宣告清單
    with open (filename , 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())    #strip del /n
    return lines

def convert(lines):
    person = None
    Allen_count = 0
    Allen_Sticker_count = 0
    Allen_img_count = 0
    Viki_count = 0
    Viki_Sticker_count = 0
    Viki_img_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] =='貼圖':
                Allen_Sticker_count += 1
            elif s[2] == '圖片':
                Allen_img_count += 1
            else:
                for m in s[2:]:
                    Allen_count += len(m)
        elif name == 'Viki':
            if s[2] =='貼圖':
                Viki_Sticker_count += 1
            elif s[2] == '圖片':
                Viki_img_count += 1
            else:
                for m in s[2:]:
                    Viki_count += len(m)
    print('Allen說了', Allen_count ,'字，傳了', Allen_Sticker_count, '個貼圖，傳了',Allen_img_count, '張圖片' )
    print('Viki說了', Viki_count,'字，傳了', Viki_Sticker_count, '個貼圖，傳了', Viki_img_count, '張圖片' )
    
def write_file(filename, lines):
    with open (filename , 'w')as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output.txt',lines)
    
main()