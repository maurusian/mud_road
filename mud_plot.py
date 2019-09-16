import matplotlib.pyplot as plt
from math import log


def load_results(filename):
    results_x = []
    results_y = []
    with open(filename,'r') as f:
        for i,line in enumerate(f):
            split_line = line.strip().split()
            results_y.append(float(split_line[1]))
            results_x.append(int(split_line[0]))
            
    return results_x,results_y

if __name__=='__main__':
    filename = '.Results/results_solution1.txt'
    results_x,results_y = load_results(filename)
    results_x = results_x[4:]
    results_y = results_y[4:]
    print(results_x)
    print(results_y)
    plt.plot(results_x,results_y)

    plt.title('Time vs Matrix size')
    plt.yscale('log')
    plt.xscale('log')

    plt.show()
