from random import randint
    

def get_zipped_matrix_list(line,c):
    zipped_list = []
    for x in range(len(line)):
        zipped_list.append([line[x],(x//c,x%c)])

    zipped_list = sorted(zipped_list,key=lambda x:x[0],reverse=True)
    return zipped_list

def get_line_max_index(line):
    m = max(line)
    m_index = line.index(m)
            
    return m_index

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

def newest_black_hole(zipped_list,matrix):
    el = zipped_list.pop(0)
    i,j = el[1]
    matrix[i][j] = -1
    return el[0]
            
def get_children(matrix,i,j,forward):
    children = []
    if j==len(matrix[0])-1 or matrix[i][j]==-1:
        return None
    else:
        if matrix[i][j+1]!=-1:
            children.append((i,j+1))
            if j==len(matrix[0])-2:
                return children
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

def all_blocked(matrix):
    for i in range(len(matrix)):
        walk_tree = build_walk_tree(matrix,i)
        #print(walk_tree) for debugging
        if walk_tree is not None:
            for children in walk_tree.values():
            #last_walk_tree_children = list(walk_tree.values())[-1] #the end of the path is not always on the last dictionary element children
                for child in children:
                    if child[1] == len(matrix[0])-1:
                        return False
    return True

def new_all_blocked(matrix,checked):
    for i in range(len(matrix)):
        checked.append((i,0))
        if matrix[i][1]==-1:
            checked.append((i,1))
            matrix[i][0]=-1
            pass
        elif  matrix[start][0]==-1:
            pass
        else:
            children = get_children(matrix,i,1,True)
            if children is None:
                pass
            else:
                for child in children:
                    checked.append(child)
                    if child not in checked:
                        next_children = get_children(matrix,child[0],child[1],False)
                        if next_children is not None:
                            dictionary[child] = next_children
                parents = list(dictionary.keys())
                i+=1
                    
        #print(walk_tree) for debugging
        if walk_tree is not None:
            for children in walk_tree.values():
            #last_walk_tree_children = list(walk_tree.values())[-1] #the end of the path is not always on the last dictionary element children
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

    #randomly built map
    r,c = (int(x) for x in input("Map dimensions: ").split())
    max_value = int(input("Maximum price: "))
    matrix,line = build_random_map(r,c,max_value)
    print_matrix(matrix)
    zipped_list = get_zipped_matrix_list(line,c)
    print('------------')
    #as long as there's a passage, remove nodes where the price is the highest
    block = False
    
    
    for i in range(r-1):
        m     = newest_black_hole(zipped_list,matrix)
    
    
    while not block:
        m     = newest_black_hole(zipped_list,matrix)
        #check if there's still a path
        block = all_blocked(matrix)
        #print(block)
        print_matrix(matrix)
        print('------------')

    print(m)
