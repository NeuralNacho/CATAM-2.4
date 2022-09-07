import matplotlib.pyplot as plt

def get_data():
    file = open('autocorrelation.dat.txt', 'r')

    data_point = ''
    data_set = []

    for character in file.read():
        if character == ',': 
            data_point = float(data_point)
            data_set.append(data_point)
            data_point = ''
        else:
            data_point += character
    data_point = float(data_point)
    data_set.append(data_point)  # Adding the last data point in

    return data_set

if __name__ == '__main__':
    data_set = get_data()

    data_set_x = data_set.copy()  
    data_set_x.pop(-1) # the x_n values
    data_set_y = data_set.copy()
    data_set_y.pop(0) # the y_n values

    plt.rc('font', size = 16)
    plt.grid(linestyle = '--', linewidth = 0.5)
    plt.scatter(data_set_x, data_set_y, s = 7)
    plt.xlabel('$x_{n}$')
    plt.ylabel('$x_{n+1}$')
    plt.show()

    print(len(data_set))


