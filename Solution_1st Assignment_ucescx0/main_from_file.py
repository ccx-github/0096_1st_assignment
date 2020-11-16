from numpy import sort   # for sorting
from plotter import Plotter
import matplotlib.pyplot as plt


def main():
    plotter = Plotter()

    print("read polygon.csv")
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
    plt.fill(plgnx, plgny, 'lightgrey')  # fill the polygon

    print("read input.csv")
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
    lt = []
    # import sort to make the code easier

    def get_extremum(lt):  # get extremum of a list
        lt = sort(lt)  # sort from small to big
        lt_max = lt[len(lt) - 1]  # get the maximum
        lt_min = lt[0]  # get the minimum
        return lt_max, lt_min
    ''' # this method is complex
    def get_max(lt):  # get maximum of a list
        for k in range(len(lt)-1):
            if lt[k] >= lt[k + 1]:
                lt_max = lt[k]
                lt[k + 1] = lt_max
            else:
                lt_max = lt[k + 1]
        return lt_max

    def get_min(lt):  # get minimum  of a list
        for t in range(len(lt)-1):
            if lt[t] <= lt[t + 1]:
                lt[t+1]=lt[t]
                lt_min = lt[t+1]
            else:
                lt_min = lt[t+1]
        # print(plgnx_min)
        return lt_min
    '''

    def mbr_1(p, pn_max, pn_min):  # MBR execute
        if p > pn_max or p < pn_min:
            return 'outside'
        else:
            return ''

    print('''Do you want to use which method to judge PIP?
       if MBR,input the number :1
       if RCA,input the number :2''')  # start the code
    n_input = int(input('The number you put:'))
    l = 0
    x_max, x_min = get_extremum(plgnx)  # get maximum/minimum x coordinate of vertexes in polygon
    y_max, y_min = get_extremum(plgny)  # get maximum/minimum y coordinate of vertexes in polygon
    # this method change the value of processing, make error
    #  x_max = get_max(plgnx)  # get maximum x coordinate of vertexes in polygon
    # x_min = get_min(plgnx)  # get minimum x coordinate of vertexes in polygon
    # y_max = get_max(plgny)  # get maximum y coordinate of vertexes in polygon
    # y_min = get_min(plgny)  # get minimum y coordinate of vertexes in polygon
    plt.plot([x_max,x_max,x_min,x_min,x_max],[y_max,y_min,y_min,y_max,y_max])# plot the mbr
    if n_input == 1:
        for l in range(len(px)):
            res1 = mbr_1(px[l], x_max, x_min)
            res2 = mbr_1(py[l], y_max, y_min)
            if res1 == 'outside' or res2 == 'outside':
                plotter.add_point(px[l], py[l], 'outside')
            else:
                plotter.add_point(px[l], py[l], '')
        plotter.add_polygon(plgnx, plgny)
        plt.fill(plgnx, plgny,'lightgrey')

    # elif n_input==2:
    else:
        print('The number that you have input is worry.please input again after reading carefully!')
    print("write output.csv")
    print("plot polygon and points")
    plotter.show()


if __name__ == "__main__":
    main()

