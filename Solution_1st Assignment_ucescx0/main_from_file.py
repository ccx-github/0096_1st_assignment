from plotter import Plotter


def main():
    plotter = Plotter()
    print("read polygon.csv")
    plgnx = []
    plgny = []
    ind1 = []
    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/polygon.csv', 'r') as f: # read polygon.csv
        line1 = f.readline()
        while line1:  # extract every row in the CSV
            line1 = f.readline()
            plgn = line1.split(',')  # split strings with comma
            if line1 != '':
                ind1.insert(j, plgn[0])
                plgnx.insert(j, float(plgn[1]))  # get x cooridinate lists
                plgny.insert(j, float(plgn[2]))  # get y cooridinate lists
                j = j + 1


    print("read input.csv")

    px = []
    py = []
    ind2 = []
    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/input.csv', 'r') as f: # read input.csv
        line = f.readline()
        while line: # extract every row in the CSV
            line = f.readline()
            pt = line.split(',') # split strings with comma
            if line != '':
                ind2.insert(i, pt[0])
                px.insert(i, float(pt[1])) # get x cooridinate lists
                py.insert(i, float(pt[2])) # get y cooridinate lists
                i = i + 1
    print("categorize points")

    print("write output.csv")

    print("plot polygon and points")
    plotter.show()


if __name__ == "__main__":
    main()
