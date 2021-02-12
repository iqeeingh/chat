# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:35:31 2021

@author: wayne
"""


   
def read_file (filename):
    lines = [] #宣告清單
    with open (filename , 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())    #strip del /n
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person ='Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new
    
def write_file(filename, lines):
    with open (filename , 'w')as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt',lines)
    
main()