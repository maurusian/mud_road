from mud_road import *
from time     import time

if __name__=='__main__':
    #randomly built map
    r,c = (int(x) for x in input("Map dimensions: ").split())
    max_value = int(input("Maximum price: "))
    matrix,line = build_random_map(r,c,max_value)
    
    print_matrix(matrix)  #to see what map the machine made for us
    print('------------')
    
    block = False
    begin = time()
    #as long as there's a passage, remove nodes where the price is the highest
    while not block:
        m     = black_hole(matrix,line)
        #check if there's still a path
        block = all_blocked(matrix)
        print_matrix(matrix)   #remove if not interested to see each step
        print('------------')

    print(m)
    end = time()

    print(end-begin)
