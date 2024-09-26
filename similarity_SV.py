import csv
import itertools
import numpy as np
from dtw import accelerated_dtw
from scipy.spatial.distance import cosine
import matplotlib.pyplot as plt

def distance(x,y):
    return cosine(x,y)

def readfile_streetmap(rfile1):
    rf1 = open(rfile1, 'r')
    reader = csv.reader(rf1)
    newstreet={}
    for row in reader:
        newstreet[row[0]] = []
        for i in range(1, len(row)):
            if row[i] == '':
                break
            partten = np.fromstring(row[i][1:-1], dtype=float, sep=' ')
            newstreet[row[0]].append(partten)
    rf1.close()
    return newstreet

def similar_SV():
    rfile1 = 'F:\\街道的相似性\\new1\\景观序列.csv'
    wf1 = open('F:\\街道的相似性\\new1\\distance_SV.txt', 'w', encoding='utf-8')
    print('road1', 'road2', 'similarity', file=wf1,sep=',')
    newstreet1 = readfile_streetmap(rfile1)
    print("read!")
    print(len(newstreet1))
    couples = list(itertools.combinations(newstreet1, 2))
    print("couples!")
    print(len(couples))
    for cou in couples:
        x = newstreet1[cou[0]]
        y = newstreet1[cou[1]]   

        dmax=len(x)+len(y)-1
        dtw_distance, cost, acc, path = accelerated_dtw(x, y, dist=distance)
        dist=1-dtw_distance/dmax
        print(cou[0], cou[1],dist,file=wf1,sep=',')
    wf1.close()

if __name__ == "__main__":
    similar_SV()
   

  
