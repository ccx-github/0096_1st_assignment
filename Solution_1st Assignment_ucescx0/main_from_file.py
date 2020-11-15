from plotter import Plotter


def main():
    plotter = Plotter()
    print("read polygon.csv")



    print("read input.csv")

    px = []
    py = []
    i = 0
    ind = []
    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/input.csv', 'r') as f:
        line = f.readline()
        while line:
            # print(line)
            line = f.readline()
            pt = line.split(',')
            # print(pt)
            if line != '':
                ind.insert(i, pt[0])
                px.insert(i, float(pt[1]))
                py.insert(i, float(pt[2]))
                i = i + 1
    print("categorize points")

    print("write output.csv")

    print("plot polygon and points")
    plotter.show()


if __name__ == "__main__":
    main()
