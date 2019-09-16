from   time       import time
from   datetime   import datetime,timedelta
from   mud_road   import *
import matplotlib as     mp


def run_sim(reps,max_value,max_dim):
    tests = []
    
    for n in range(2,max_dim+1):
        time_sum = 0
        matrix,line = build_random_map(n,n,max_value)
        begin = time()
        for i in range(reps): #to get a good average time over multiple repetitions
            block = False
            
            #we can safely remove n-1 nodes with the highest cost without blocking all passages
            for x in range(n-1):
                m     = black_hole(matrix,line)
            #as long as there's a passage, remove nodes where the price is the highest
            while not block:
                m     = black_hole(matrix,line)
                #check if there's still a path
                block = all_blocked(matrix)
                
        end = time()
        time_sum+=(end-begin)*1000/reps
        
        tests.append((n,time_sum))
        print(str(n).rjust(len(str(max_dimension)),' ')+'      '+str(time_sum))
    return tests


if __name__ == '__main__':

    repetitions   = 1000
    max_price     = 10000
    max_dimension = 100
    tests = run_sim(repetitions,max_price,max_dimension)
    
    print(tests)

    with open('./Results/results.txt','w') as f:
        for result in tests:
            f.write(str(result[0]).rjust(len(str(max_dimension)),' ')+'      '+str(result[1])+'\n')
