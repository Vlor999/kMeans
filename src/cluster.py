from random import randint

class cluster:
    def __init__(self, color:int):
        self.color:int = color
        self.centroid: tuple[int, int] = None
        self.points:list[tuple[int,int]] = []
        self.length:int = 0

    def __str__(self):
        output = f"color : {self.color}, centroid : {self.centroid}, taille : {self.length}, points : \n"
        for point in self.points:
            output += f"point : {point}\n"
        return output

    def initCentroid(self, numberLine:int, numberCol:int):
        self.centroid = (randint(0, numberLine), randint(0, numberCol))

    def getLength(self):
        return self.length

    def addPoint(self, point):
        self.points.append(point)
        self.length += 1

    def updateCentroid(self):
        newX = 0
        newY = 0
        for point in self.points:
            newX += point[0]
            newY += point[1]
        self.centroid = (newX / self.length, newY / self.length)