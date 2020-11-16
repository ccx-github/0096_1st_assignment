from numpy import sort   # for sorting quickly,but I don't know if it is a module,sorry!
from plotter import Plotter
import matplotlib.pyplot as plt

def main():
    plotter = Plotter()
    print("read polygon.csv")
    plgnx = []  # define a list for x coordinate of vertexes
    plgny = []  # define a list for x coordinate of vertexes
    ind1 = []  # define a list for the id column from the csv
    j = 0  # used for the while loop

    with open('E:/0096_1st_assignment/Solution_1st Assignment_ucescx0/polygon.csv', 'r') as f:  # read polygon.csv
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

    print("Insert point information")
    x = float(input("x coordinate: "))
    y = float(input("y coordinate: "))
    print("categorize point")

    def get_extremum(lt):  # get extremum of a list
        lt = sort(lt)  # sort from small to big
        lt_max = lt[len(lt) - 1]  # get the maximum
        lt_min = lt[0]  # get the minimum
        return lt_max, lt_min
    '''# this method is complex
    def get_max(lt):  # get maximum of a list
        for k in range(len(lt) - 1):
            if lt[k] >= lt[k + 1]:
                lt_max = lt[k]
                lt[k + 1] = lt_max
            else:
                lt_max = lt[k + 1]
        return lt_max

    def get_min(lt):  # get minimum  of a list
        for t in range(len(lt) - 1):
            if lt[t] <= lt[t + 1]:
                lt[t + 1] = lt[t]
                lt_min = lt[t + 1]
            else:
                lt_min = lt[t + 1]
        # print(plgnx_min)
        return lt_min
    '''
    def mbr_1(p, pn_max, pn_min):  # MBR execute
        if p > pn_max or p < pn_min:
            return 'outside'
        else:
            return ''

    print('''would you like to use which method to judge PIP?
    if MBR,it's not exactly correct.Please input the number :1
    if RCA,an output file about their positions will be written.Please input the number :2''')  # start
    n_input = int(input('The number you put:'))
    l = 0
    x_max, x_min = get_extremum(plgnx)  # get maximum/minimum x coordinate of vertexes in polygon
    y_max, y_min = get_extremum(plgny)  # get maximum/minimum y coordinate of vertexes in polygon
    '''
    x_max = get_max(plgnx)  # get maximum x coordinate of vertexes in polygon
    x_min = get_min(plgnx)  # get minimum x coordinate of vertexes in polygon
    y_max = get_max(plgny)  # get maximum y coordinate of vertexes in polygon
    y_min = get_min(plgny)  # get minimum y coordinate of vertexes in polygon
    '''
    plt.plot([x_max, x_max, x_min, x_min, x_max], [y_max, y_min, y_min, y_max, y_max])
    if n_input == 1:
        res1 = mbr_1(x, x_max, x_min)
        res2 = mbr_1(y, y_max, y_min)
        if res1 == 'outside' or res2 == 'outside':
            plotter.add_point(x, y, 'outside')
        else:
            plotter.add_point(x, y, '')
        plotter.add_polygon(plgnx, plgny)
        plt.fill(plgnx, plgny, 'lightgrey')
    elif n_input == 2:

        res1 = mbr_1(x, x_max, x_min)  # use the MBR to save time and space
        res2 = mbr_1(y, y_max, y_min)
        if res1 == 'outside' or res2 == 'outside':
            plotter.add_point(x, y, 'outside')
        else:
            count = 0

            for q in range(len(plgnx) - 1):
                # judge whether the two ends of the line segment are on both sides of the ray.
                # if not,they must not intersect.
                # amend some inside point into boundary
                if x == plgnx[q] and y == plgny[q]:
                    plotter.add_point(x, y, 'boundary')  # blue point
                if (plgny[q] < y <= plgny[q + 1]) or (plgny[q] >= y > plgny[q + 1]):
                    line2 = plgnx[q + 1] - (plgny[q + 1] - y) * (plgnx[q + 1] - plgnx[q]) / (
                            plgny[q + 1] - plgny[q])  # as above
                    if line2 == x and plgny[q + 1] != plgny[q]:  # points coincide with vertexes
                        plotter.add_point(x, y, 'boundary')  # blue point
                    if line2 < x:  # point is not on line
                        count += 1  # the ray and the line intersect,point add.
                elif (plgnx[q] < x <= plgnx[q + 1]) or (plgnx[q] >= x > plgnx[q + 1]):
                    # judge the same y coordinate and point on line
                    if plgny[q] - y == 0 and plgny[q + 1] - y == 0:
                        plotter.add_point(x, y, 'boundary')  # blue point

            if count % 2 != 0:  # judge whether outside or (inside and boundary)
                plotter.add_point(x, y, 'inside')  # green points include inside and boundary
            else:
                plotter.add_point(x, y, 'outside')  # red point

    else:
        print('The number that you have input is worry.please input again after reading carefully!')
    print("plot polygon and point")
    plotter.show()


if __name__ == "__main__":
    main()
