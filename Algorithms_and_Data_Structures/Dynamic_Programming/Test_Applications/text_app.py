import numpy as np

def string_compare(P, T, i, j):
    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])
    
    swap = string_compare(P, T, i-1, j-1) + (P[i-1] != T[j-1])
    insert = string_compare(P, T, i, j-1) + 1
    delete = string_compare(P, T, i-1, j) + 1
    
    smallest_cost = min(swap, insert, delete)
    
    return smallest_cost


def pd_compare(P, T, i, j):
    D = np.zeros((i, j))
    
    for i_inx in range(1, i):
        D[i_inx][0] = i_inx
    for j_inx in range(1, j):
        D[0][j_inx] = j_inx

    parents = np.array([["X" for i_inx in range(j)] for j_inx in range(i)])
    
    for i_inx in range(i):
        parents[i_inx][0] = "D"
    for j_inx in range(j):
        parents[0][j_inx] = "I"  
              
    parents[0][0] = "X"

    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])

    for i_inx in range(1, i):
        for j_inx in range(1, j):
            swap = D[i_inx-1][j_inx-1] + (P[i_inx]!=T[j_inx])
            insert = D[i_inx][j_inx-1] + 1
            delete = D[i_inx-1][j_inx] + 1

            smallest_cost = min(swap, insert, delete)
       
            D[i_inx][j_inx] += smallest_cost
            
            
            if swap == smallest_cost:
                if P[i_inx]!=T[j_inx]:
                    parents[i_inx][j_inx] = "S"
                else:
                    parents[i_inx][j_inx] = "M"
            elif insert == smallest_cost:
                parents[i_inx][j_inx] = "I"
            elif delete == smallest_cost:
                parents[i_inx][j_inx] = "D"
            
    return int(D[-1, -1]), parents

def repeat(P, T, i, j):
    parents = pd_compare(P, T, i, j)[1]
    path = [] 
    i -= 1
    j -= 1
       
    while parents[i][j] != "X":
        
        if parents[i][j] == "M" or parents[i][j] == "S":
            path.append(parents[i][j])
            i -= 1
            j -= 1
        elif parents[i][j] == "D":
            path.append(parents[i][j])
            i -= 1
        elif parents[i][j] == "I":
            path.append(parents[i][j])
            j -= 1
                
    pr = ""
    for w in path:
        pr += w
    
    return pr[::-1]

def matching(P, T, i, j):
    D = np.zeros((i, j))
    
    for i_inx in range(1, i):
        D[i_inx][0] = i_inx

    parents = np.array([["X" for i_inx in range(j)] for j_inx in range(i)])
    
    for i_inx in range(1, i):
        parents[i_inx][0] = "D"
              
    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])

    for i_inx in range(1, i):
        for j_inx in range(1, j):
            swap = D[i_inx-1][j_inx-1] + (P[i_inx]!=T[j_inx])
            insert = D[i_inx][j_inx-1] + 1
            delete = D[i_inx-1][j_inx] + 1

            smallest_cost = min(swap, insert, delete)
       
            D[i_inx][j_inx] += smallest_cost
            
            
            if swap == smallest_cost:
                if P[i_inx]!=T[j_inx]:
                    parents[i_inx][j_inx] = "S"
                else:
                    parents[i_inx][j_inx] = "M"
            elif insert == smallest_cost:
                parents[i_inx][j_inx] = "I"
            elif delete == smallest_cost:
                parents[i_inx][j_inx] = "D"
            
    return np.argmin(D[-1][:]) - i + 2

def longest_seq(P, T, i , j):
    D = np.zeros((i, j))
    
    for i_inx in range(1, i):
        D[i_inx][0] = i_inx
    for j_inx in range(j):
        D[0][j_inx] = j_inx

    parents = np.array([["X" for i_inx in range(j)] for j_inx in range(i)])
    
    for i_inx in range(i):
        parents[i_inx][0] = "D"
    for j_inx in range(j):
        parents[0][j_inx] = "D"  
              
    parents[0][0] = "X"

    if i == 0:
        return len(T[:j])
    if j == 0:
        return len(P[:i])

    for i_inx in range(1, i):
        for j_inx in range(1, j):
            if P[i_inx]!=T[j_inx]:
                swap = D[i_inx-1][j_inx-1] + 250
            else:
                swap = D[i_inx-1][j_inx-1]
            insert = D[i_inx][j_inx-1] + 1
            delete = D[i_inx-1][j_inx] + 1

            smallest_cost = min(swap, insert, delete)
       
            D[i_inx][j_inx] += smallest_cost
            
            
            if swap == smallest_cost:
                if P[i_inx]!=T[j_inx]:
                    parents[i_inx][j_inx] = "S"
                else:
                    parents[i_inx][j_inx] = "M"
            elif insert == smallest_cost:
                parents[i_inx][j_inx] = "I"
            elif delete == smallest_cost:
                parents[i_inx][j_inx] = "D"
                
    pr = ""
    i -= 1
    j -= 1
    
    while parents[i][j] != "X":
        
        if parents[i][j] == "M":
            pr += P[i]
            i -= 1
            j -= 1
        elif parents[i][j] == "S":
            j -= 1
            i -= 1
        elif parents[i][j] == "D":
            i -= 1
        elif parents[i][j] == "I":
            j -= 1
            
    return pr[::-1]
    

def main():
    P1 = ' kot'
    T1 = ' pies'

    print(string_compare(P1, T1, len(P1), len(T1)))
    
    P2 = ' biały autobus'
    T2 = ' czarny autokar'
    print(pd_compare(P2, T2, len(P2), len(T2))[0])
    
    P3 = ' thou shalt not'
    T3 = ' you should not'
    print(repeat(P3, T3, len(T3), len(P3)))
    
    
    P4 = ' ban'
    T4 = ' mokeyssbanana'
    
    print(matching(P4, T4, len(P4), len(T4)))
    
    P5 = ' democrat'
    T5 = ' republican'
    
    print(longest_seq(P5, T5, len(P5), len(T5)))
    
    T6 = ' 243517698'
    P6 = ''.join(sorted(T6))
    
    print(longest_seq(P6, T6, len(P6), len(T6)))
    
if __name__ == "__main__":
    main()