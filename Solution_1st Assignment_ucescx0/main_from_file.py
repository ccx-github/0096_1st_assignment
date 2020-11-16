from numpy import sort   # for sorting quickly,but I don't know if it is a module,sorry!
import csv
from plotter import Plotter
import matplotlib.pyplot as plt
# This is a program about how to judge whether a list of points is in a polygon. First read data from csv files,
# and define the data as list type. And write program to get the MBR(Minimum Bounding Rectangle),then use the ray
# casting algorithm to get the correct judgment and output a csv file.

def main():
    plotter = Plotter()

    print("read polygon.csv")
    plgnx = []  # define a list for x coordinate of vertexes
    plgny = []  # define a list for x coordinate of vertexes
    ind1 = []  # define a list for the id column from the csv
    j = 0  # used for the while loop

    # read polygon.csv
    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/polygon.csv', 'r') as f:
        line1 = f.readline()  # read the first line from the polygon csv
        while line1:  # extract every row in the CSV
            line1 = f.readline()
            plgn = line1.split(',')  # split strings with comma
            if line1 != '':  # an empty string will be read at last while looping
                ind1.insert(j, plgn[0])  # get id lists
                plgnx.insert(j, float(plgn[1]))  # get x coordinate lists of vertexes
                plgny.insert(j, float(plgn[2]))  # get y coordinate lists of vertexes
                j = j + 1
    plt.fill(plgnx, plgny, 'lightgrey')  # fill the polygon

    print("read input.csv")
    px = []  # define a list for x coordinate of points
    py = []  # define a list for x coordinate of points
    ind2 = []  # define a list for the id column from the csv
    i = 0  # used for the while loop

    # read input.csv
    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/input.csv', 'r') as f:
        line = f.readline()  # as above
        while line:  # extract every row in the CSV
            line = f.readline()
            pt = line.split(',')  # split strings with comma
            if line != '':
                ind2.insert(i, pt[0])  # as above
                px.insert(i, float(pt[1]))  # get x coordinate lists of inputs
                py.insert(i, float(pt[2]))  # get y coordinate lists of inputs
                i = i + 1

    print("categorize points")
    lt = []  # define a list

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

    def mbr_1(p, pn_max, pn_min):  # define an method to judge the position
        if p > pn_max or p < pn_min:  # larger than the maximum and less than the minimum
            return 'outside'
        else:
            return ''

    # start the code
    print('''would you like to use which method to judge PIP?
    if MBR,it's not exactly correct.Please input the number :1
    if RCA,an output file about their positions will be written.Please input the number :2''')
    n_input = int(input('The number you put:'))
    x_max, x_min = get_extremum(plgnx)  # get maximum/minimum x coordinate of vertexes in polygon
    y_max, y_min = get_extremum(plgny)  # get maximum/minimum y coordinate of vertexes in polygon
    # this method change the value of processing, make error
    #  x_max = get_max(plgnx)  # get maximum x coordinate of vertexes in polygon
    # x_min = get_min(plgnx)  # get minimum x coordinate of vertexes in polygon
    # y_max = get_max(plgny)  # get maximum y coordinate of vertexes in polygon
    # y_min = get_min(plgny)  # get minimum y coordinate of vertexes in polygon
    plt.plot([x_max, x_max, x_min, x_min, x_max], [y_max, y_min, y_min, y_max, y_max])  # plot the mbr
    if n_input == 1:  # choose MBR
        for l in range(len(px)):
            res1 = mbr_1(px[l], x_max, x_min)  # get x state of each point
            res2 = mbr_1(py[l], y_max, y_min)  # get y state of each point
            if res1 == 'outside' or res2 == 'outside':  # any of them is outside,then the result is outside
                plotter.add_point(px[l], py[l], 'outside')  # class object call a method from Class Plotter
            else:
                plotter.add_point(px[l], py[l], '')
        plotter.add_polygon(plgnx, plgny)

    elif n_input==2:  # choose RCA
        with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/output.csv', 'w',newline='') \
                as csvfile:
            writer=csv.writer(csvfile,delimiter=' ')
            writer.writerows()
        for l in range(len(px)):  # judge each point
            res1 = mbr_1(px[l], x_max, x_min)  # use the MBR to save time and space
            res2 = mbr_1(py[l], y_max, y_min)
            if res1 == 'outside' or res2 == 'outside':
                plotter.add_point(px[l], py[l], 'outside')
            else:
                count=0
                for q in range(len(plgnx) - 1):
                    # judge whether the two ends of the line segment are on both sides of the ray.
                    # if not,they must not intersect.
                    if (plgny[q] < py[l] <= plgny[q + 1]) or (plgny[q] >= py[l] > plgny[q + 1]):
                        # point is on line or not,just the relationship of slope
                        line2 = plgnx[q + 1] - (plgny[q + 1] - py[l]) * (plgnx[q + 1] - plgnx[q]) / (
                                plgny[q + 1] - plgny[q])
                        if line2 < px[l]:  # point is not on line
                            count += 1  # the ray and the line intersect,point add.
                if count > 0 and count % 2 != 0:  # judge whether outside or (inside and boundary)
                    plotter.add_point(px[l], py[l], 'inside')  # green points include inside and boundary
                else:
                    plotter.add_point(px[l], py[l], 'outside')  # red point
                for q in range(len(plgnx) - 1):  # amend some inside point into boundary
                    if px[l] == plgnx[q] and py[l] == plgny[q]:
                        plotter.add_point(px[l], py[l], 'boundary')  # blue point
                    if (plgny[q] < py[l] <= plgny[q + 1]) or (plgny[q] >= py[l] > plgny[q + 1]):
                        line2 = plgnx[q + 1] - (plgny[q + 1] - py[l]) * (plgnx[q + 1] - plgnx[q]) / (
                                plgny[q + 1] - plgny[q])  # as above
                        if line2 == px[l] and plgny[q + 1] != plgny[q]:  # points coincide with vertexes
                            plotter.add_point(px[l], py[l], 'boundary') # blue point
                    elif (plgnx[q] < px[l] <= plgnx[q + 1]) or (plgnx[q] >= px[l] > plgnx[q + 1]):
                        # judge the same y coordinate and point on line
                        if plgny[q] - py[l] == 0 and plgny[q + 1] - py[l] == 0:
                            plotter.add_point(px[l], py[l], 'boundary')  # blue point

    else:
        print('The number that you have input is worry.please input again after reading carefully!')


    print("write output.csv")

    print("plot polygon and points")
    plotter.show()


if __name__ == "__main__":
    main()

