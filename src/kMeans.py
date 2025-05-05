import matplotlib.pyplot as plt
from random import randint
import numpy as np
from src.cluster import cluster


def creationMap(numberLine:int, numberCol:int) -> np.ndarray:
    map = np.ones((numberLine, numberCol, 3))
    for l in range(numberLine):
        for c in range(numberCol):
            if randint(0,10) > 8:
                map[l][c] = (0, 0, 0)
    return map

def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def kMeans(map:np.ndarray, k:int):
    colors = [(i / k, 170 / 255 * i / k, 85 / 255 * i / k) for i in range(1, k + 1)]
    clusters = []
    numberLine, numberCol = len(map), len(map[0])
    for i in range(k):
        clu = cluster(colors[i])
        clusters.append(clu)
        clu.initCentroid(numberLine, numberCol)
    for l in range(numberLine):
        for c in range(numberCol):
            if map[l][c][0] == 0 and map[l][c][1] == 0 and map[l][c][2] == 0:
                minDistance = float("inf")
                bestClu = None
                for clu in clusters:
                    dist = distance(clu.centroid, (l, c))
                    if dist < minDistance:
                        minDistance = dist
                        bestClu = clu
                if bestClu != None:
                    bestClu.addPoint((l,c))
                    bestClu.updateCentroid()
                    map[l][c] = bestClu.color

def showMap(map:np.ndarray):
    plt.imshow(map, interpolation='nearest')
    plt.show()
