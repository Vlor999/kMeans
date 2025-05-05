from src.kMeans import showMap, creationMap, kMeans

def main():
    map = creationMap(100, 100)
    kMeans(map, 7)
    showMap(map)

if __name__ == "__main__":
    main()

