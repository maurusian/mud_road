from random import randint

def get_line_max_index(line):
    m = max(line)
    return line.index(m)

def index_to_coord(index,c):
    j = index%c
    i = index//c

    return i,j


def black_hole(matrix,line):
    index = get_line_max_index(line)
    i,j   = index_to_coord(index,len(matrix[0]))
    m     = line[index]
    #print((i,j))
    line[index]  = -1
    matrix[i][j] = -1
    return m

#not used
def new_black_hole(matrix):
    i_max = len(matrix)-1
    j_max = len(matrix[0])-1
    if matrix[i_max][j_max-1]==-1:
        matrix[i_max][j_max]=-1
    if matrix[0][j_max-1]==-1:
        matrix[0][j_max]=-1
    for i in range(len(matrix)):
        if matrix[i][1]==-1:
            matrix[i][0]=-1
    for i in range(1,i_max):
        if matrix[i][j_max-1]==-1 and (matrix[i-1][j_max]==-1 or matrix[i+1][j_max]==-1):
            matrix[i][j_max]=-1

#not used
def get_values(matrix,coord):
    return matrix[coord[0]][coord[1]]

#not used
def get_list_values(matrix,coords):
    value_list = []
    for coord in coords:
        value_list.append(get_values(matrix,coord))
    return value_list

#not used
def propagate_values(matrix):
    for i in range(len(matrix)):
        if matrix[i][0]!=-1:
            dictionary = build_walk_tree(matrix,i)
            if dictionary is not None:
                for parent,children in dictionary.items():
                    children_values = get_list_values(matrix,children)
                    if get_values(matrix,parent)<min(children_values):
                        matrix[parent[0]][parent[1]]=min(children_values)
                        print('change')
            
def get_children(matrix,i,j,forward):
    children = []
    if j==len(matrix[0])-1 or matrix[i][j]==-1:
        return None
    else:
        if matrix[i][j+1]!=-1:
            children.append((i,j+1))
        if i>0 and matrix[i-1][j]!=-1:
            children.append((i-1,j))
        if i<len(matrix)-1 and matrix[i+1][j]!=-1:
            children.append((i+1,j))
        if j>0 and matrix[i][j-1]!=-1:
            children.append((i,j-1))
    return children

def build_walk_tree(matrix,start):
    if matrix[start][1]==-1:
        matrix[start][0]=-1
        return None
    elif  matrix[start][0]==-1:
        return None
    else:
        dictionary = {(start,0):[(start,1)]}
        children = get_children(matrix,start,1,True)
        if children is not None:
            dictionary[(start,1)] = children
            parents = list(dictionary.keys())
            i = 0
            while i < len(parents):
                for child in dictionary[parents[i]]:
                    if child not in dictionary.keys():
                        next_children = get_children(matrix,child[0],child[1],False)
                        if next_children is not None:
                            dictionary[child] = next_children
                parents = list(dictionary.keys())
                i+=1
    return dictionary

#not used
def is_walled(matrix):
    for j in range(len(matrix[0])):
        wall = True
        for i in range(len(matrix)):
            if matrix[i][j]!=-1:
                wall = False
                break
        if wall:
            break
         
    return wall

#not used
def reevaluate_cell(matrix,i,j):
    if i not in (0,len(matrix)-1) and j not in (0,len(matrix[0])-1):
        lis = sorted([matrix[i+1][j],matrix[i][j+1],matrix[i-1][j],matrix[i][j-1]])
    elif i==0 and j not in (0,len(matrix[0])-1):
        lis = sorted([matrix[i+1][j],matrix[i][j+1],matrix[i][j-1]])
    elif i not in (0,len(matrix)-1) and j==0:
        lis = sorted([matrix[i+1][j],matrix[i][j+1],matrix[i-1][j]])
    elif i==len(matrix)-1 and j not in (0,len(matrix[0])-1):
        lis = sorted([matrix[i-1][j],matrix[i][j+1],matrix[i][j-1]])
    elif i not in (0,len(matrix)-1) and j == len(matrix[0])-1:
        lis = sorted([matrix[i-1][j],matrix[i+1][j],matrix[i][j-1]])
    elif i == 0 and j == len(matrix[0])-1:
        lis = sorted([matrix[i+1][j],matrix[i][j-1]])
    elif i==len(matrix)-1 and j == 0:
        lis = sorted([matrix[i-1][j],matrix[i][j+1]])
    elif i==len(matrix)-1 and j == len(matrix[0])-1:
        lis = sorted([matrix[i-1][j],matrix[i][j-1]])
    else: # i==0 and j==0
        lis = sorted([matrix[i+1][j],matrix[i][j+1]])

    length = len(lis)
    k=0
    while k<len(lis):
        if lis[k] == -1:
            del lis[k]
        else:
            k+=1
    if len(lis)>0:
        if matrix[i][j]<lis[0]:
            matrix[i][j]=lis[0]
    else:
        matrix[i][j]=-1

    if length == 4 and len(lis)==1:
        matrix[i][j]=-1

#not used
def reevaluate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!=-1:
                reevaluate_cell(matrix,i,j)
    return matrix


def all_blocked(matrix):
    for i in range(len(matrix)):
        walk_tree = build_walk_tree(matrix,i)
        #print(walk_tree)
        if walk_tree is not None:
            for children in walk_tree.values():
                for child in children:
                    if child[1] == len(matrix[0])-1:
                        return False
    return True

def print_matrix(matrix):
    for m in matrix:
        for x in m:
            print(str(x).rjust(7,' '),end='')
        print()

def build_random_map(r,c,max_value):
    mtx = []
    lin = []
    for i in range(r):
        mtx.append([])
        for j in range(c):
            value = randint(1,max_value)
            mtx[i].append(value)
            lin.append(value)
    return mtx,lin

if __name__=='__main__':
    """
    #user input
    r,c = (int(x) for x in input().split())
    matrix = []
    line   = []
    for i in range(r):
        matrix.append([int(x) for x in input().split()])
        line+=matrix[-1]
    
    walled = False
    while not walled:
        #print(line)
        m = black_hole(matrix,line)
        walled = is_walled(matrix)
        #print(walled)


    print(m)
    """

    #randomly built map
    r,c = (int(x) for x in input("Map dimensions: ").split())
    max_value = int(input("Maximum price: "))
    matrix,line = build_random_map(r,c,max_value)
    print_matrix(matrix)
    print('------------')
    #as long as there's a passage, remove nodes where the price is the highest
    block = False
    #m     = black_hole(matrix,line)
    #print(all_blocked(matrix))
    
    while not block:
        m     = black_hole(matrix,line)
        #check if there's still a path
        block = all_blocked(matrix)
        #print(block)
        print_matrix(matrix)
        print('------------')

    print(m)

    """
    new_black_hole(matrix)
    print_matrix(matrix)

    #print(sorted([1,2,4,-1]))
    
    #reevaluate_matrix(matrix)

    xm = []
    old_m = [[]]
    while xm!=old_m:
        old_m = xm
        if xm!=[]:
            print_matrix(xm)
        xm = reevaluate_matrix(matrix)
        print('------------')
        
    #print(get_children(matrix,3,2,True))
    
    #print(build_walk_tree(matrix,1))

    propagate_values(matrix)

    print_matrix(matrix)
    """
