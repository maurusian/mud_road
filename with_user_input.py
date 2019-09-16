from mud_road import *


if __name__ == '__main__':
    #user input
    r,c = (int(x) for x in input().split())
    matrix = []
    line   = []
    for i in range(r):
        matrix.append([int(x) for x in input().split()])
        line+=matrix[-1]

    block = False
    
    while not block:
        m     = black_hole(matrix,line)
        #check if there's still a path
        block = all_blocked(matrix)
        print_matrix(matrix)  #the printing instructions can be commented out
        print('------------') #if only the result matters

    print(m)
