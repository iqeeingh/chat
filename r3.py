# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:13:54 2021

@author: wayne
"""

lines = []
with open ('3.txt', 'r' , encoding = 'UTF-8-sig')as f:
    for line in f:
        lines.append(line.strip())
        
for line in lines:
    s = line.split(' ')
    time = s[0][:5] #清單分割
    person = s[0][5:]
    
    print(time,person)