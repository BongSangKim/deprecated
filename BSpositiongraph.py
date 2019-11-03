import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    control_set = np.loadtxt('BSposition.csv', delimiter=',')
    control_X = control_set[0,:]
    control_Y = control_set[1,:]
    control_data = ['BS 0','BS 1','BS 2','BS 3','BS 4','BS 5','BS 6','BS 7']

    interference_set = np.loadtxt('InterferenceBSposition.csv', delimiter=',')
    interference_X =interference_set[0,:]
    interference_Y = interference_set[1,:]
    plt.scatter(control_X,control_Y,marker = 's')
    plt.scatter(interference_X,interference_Y)
    plt.grid()
    plt.xlim(-100,200)
    plt.ylim(-100,200)
    plt.legend(['control BS','Interference BS'])
    plt.title('BS position')
    for i, txt in enumerate(control_data):
        plt.annotate(txt,(control_X[i],control_Y[i]))
    plt.show()