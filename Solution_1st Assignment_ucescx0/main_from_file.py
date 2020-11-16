from plotter import Plotter


def main():
    plotter = Plotter()
    # print("read polygon.csv")
    plgnx = []
    plgny = []
    ind1 = []
    j = 0

    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/polygon.csv', 'r') as f: # read polygon.csv
        line1 = f.readline()
        while line1:  # extract every row in the CSV
            line1 = f.readline()
            plgn = line1.split(',')  # split strings with comma
            if line1 != '':
                ind1.insert(j, plgn[0])
                plgnx.insert(j, float(plgn[1]))  # get x coordinate lists of vertexes
                plgny.insert(j, float(plgn[2]))  # get y coordinate lists of vertexes
                j = j + 1
    # print("read input.csv")
    px = []
    py = []
    ind2 = []
    i = 0
    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/input.csv', 'r') as f: # read input.csv
        line = f.readline()
        while line: # extract every row in the CSV
            line = f.readline()
            pt = line.split(',') # split strings with comma
            if line != '':
                ind2.insert(i, pt[0])
                px.insert(i, float(pt[1])) # get x coordinate lists of inputs
                py.insert(i, float(pt[2])) # get y coordinate lists of inputs
                i = i + 1
    print("categorize points")

    def getx_max():  # get maximum x coordinate of vertexes in polygon
        for k in range(len(plgnx)-1):
            if plgnx[k]>plgnx[k+1]:
                plgnx_max=plgnx[k]
                plgnx[k+1]=plgnx_max
            else:
                plgnx_max=plgnx[k+1]
        return plgnx_max

    def getx_min():  # get minimum x coordinate of vertexes in polygon
        for k in range(len(plgnx) - 1):
            if plgnx[k] > plgnx[k + 1]:
                plgnx_min = plgnx[k + 1]
            else:
                plgnx_min = plgnx[k]
                plgnx[k + 1] = plgnx_min
        return plgnx_min

    def gety_max():  # get maximum y coordinate of vertexes in polygon
        for k in range(len(plgny)-1):
            if plgny[k]>plgny[k+1]:
                plgny_max=plgny[k]
                plgny[k+1]=plgny_max
            else:
                plgny_max=plgny[k+1]
        return plgny_max

    def gety_min():  # get minimum y coordinate of vertexes in polygon
        for k in range(len(plgny) - 1):
            if plgny[k]>plgny[k+1]:
                plgny_min=plgny[k+1]
            else:
                plgny_min=plgny[k]
                plgny[k + 1] = plgny_min
        return plgny_min

    def mbr_1(p,pn_max,pn_min):  # MBR execute
        if p>pn_max or p<pn_min:
            return 'outside'
        else:
            return 'inside'

    print('''Do you want to use which algorithem to judge PIP?
       if MBR,input the number :1
       if RCA,input the number :2''')  # start
    n_input = int(input('The number you put:'))
    if n_input == 1:
        for l in range(len(px)):
            res1 = mbr_1(px[l], getx_max(), gety_min())
            plotter.add_point(px[l], py[l], res1)  # add points by x coordinate to the plotter
            res2 = mbr_1(py[l], gety_max(), gety_min())
            plotter.add_point(px[l], py[l], res2)  # add points by y coordinate to the plotter
        for m in range(len(plgnx)):
            plotter.add_polygon(plgnx, plgny)
    # elif n_input==2:
    else:
        print('The number that you have input is worry.please input again after reading carefully!')
    print("write output.csv")
    # print("plot polygon and points")
    plotter.show()


if __name__ == "__main__":
    main()
