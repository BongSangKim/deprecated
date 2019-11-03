import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    control_set = np.loadtxt('BSposition.csv', delimiter=',')
    control_X = control_set[0,:]
    control_Y = control_set[1,:]
    control_data = ['BS 0','BS 1','BS 2','BS 3','BS 4','BS 5','BS 6','BS 7']

    plt.scatter(control_X,control_Y,marker = 's')
    plt.grid()
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.legend(['control BS'])
    plt.title('BS position')
    for i, txt in enumerate(control_data):
        plt.annotate(txt,(control_X[i],control_Y[i]))
    plt.show()