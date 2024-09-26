import numpy as np
from dtw import dtw
import sys
import csv
import itertools
import matplotlib.pyplot as plt
max_diff=54.72439321-19.32992872

def absdis(x, y):
    diff=abs(x-y)/(max_diff)
    return diff

def readfile_safe(rfile1):
    rf1 = open(rfile1, 'r')
    reader = csv.reader(rf1)
    newstreet = {}
    for row in reader:
        newstreet[row[0]] = []
        for i in range(1, len(row)):
            if row[i] == '':
                break
            newstreet[row[0]].append(float(row[i]))
    rf1.close()
    return newstreet

def similar_safe():

    rfile='F:\\街道的相似性\\new1\\安全性感知序列.csv'
    wf=open('F:\\街道的相似性\\new1\\distance_safe2.txt','w', encoding='utf-8')
    print('road1', 'road2', 'similarity', file=wf,sep=',')
    newstreet =readfile_safe(rfile)

    print("read!")
    print(len(newstreet))

    couples=list(itertools.combinations(newstreet, 2))
    print("couples!")
    print(len(couples))

    for cou in couples:
        x = newstreet[cou[0]]
        y = newstreet[cou[1]] 
        dmax=len(x)+len(y)-1
        try:
            dtw_distance, cost, acc, path= dtw(x, y, dist=absdis)
            dist=1-dtw_distance/dmax
        except ValueError as e:
            print(e)
            print(cou[0], cou[1],x,y,sep='\n')
            exit()
        print(cou[0], cou[1],dist,file=wf,sep=',')

    wf.close()


if __name__ == "__main__":
    similar_safe()


