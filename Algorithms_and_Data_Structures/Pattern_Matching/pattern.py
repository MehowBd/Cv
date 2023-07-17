#skończone
import time

def naive_method(S, W):
    m = 0    
    num_comparisons = 0
    num = []
    
    while m < len(S):
        num_comparisons += 1
        if S[m: len(W)+m] == W:
            num.append(m)
        m += 1
        
    return len(num), num_comparisons
    
def hash(word, d=256, q=101):
    hw = 0
    for i in range(len(word)): 
        hw = (hw*d + ord(word[i])) % q
    return hw

def rabin_karp(S, W):
    collisions = 0
    hW = hash(W)
    num_comparisons = 0
    num = []
    M = len(S)
    N = len(W)
    
    for m in range(0, M-N+1):
        num_comparisons += 1
        hS = hash(S[m:m+N])
        if hS == hW:
            if S[m: m+N] == W:
                num.append(m)
            else:
                collisions += 1
    return len(num), num_comparisons, collisions

def rabin_karp_rolling(S, W, d = 256, q = 101):
    collisions = 0
    M = len(S)
    N = len(W)
    hW = hash(W)
    hS = hash(S[0:N])
    num_comparisons = 0
    num = []
    
    h = 1
    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q 

    for m in range(0, M-N+1):
        num_comparisons += 1
        hS = hash(S[m:m+N])
        if hS == hW:
            if S[m: m+N] == W:
                num.append(m)
            else:
                collisions += 1
        if m+N == M:
            break
        hS = (d*(hS - ord(S[m])*h) + ord(S[m+N])) % q
        
        if hS < 0:
            hS += q
    return len(num), num_comparisons, collisions

def kmp_search(S, W):
    num_comparisons = 0
    P = [0 for i in range(len(S))]
    nP = 0
    
    m = 0
    i = 0
    T = kmp_table(W)
    
    while m < len(S):
        num_comparisons += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            
            if i == len(W):
                P[nP] = m-i
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i<0 :
                m += 1
                i += 1    
    return nP, num_comparisons

def kmp_table(W):
    pos = 1
    cnd = 0
    T = [0 for i in range(len(W)+1)]
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    
    return T    
    
def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
        
    S = ' '.join(text).lower()
    
    W = "time."
    
    
 #  t_start = time.perf_counter()
    test = naive_method(S, W)
    print(test[0], ";", test[1])
 #  t_stop = time.perf_counter()
 #  print("Czas obliczeń dla Metody Naiwnej:", "{:.7f}".format(t_stop - t_start))
    
 #  t_start = time.perf_counter()
    test2 = rabin_karp(S, W)
    print(test2[0], ";", test2[1], ";", test2[2])
 #  t_stop = time.perf_counter()
 #  print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    
 #  t_start = time.perf_counter()
    test3 = kmp_search(S, W)
    print(test3[0], ";", test3[1])
 #  t_stop = time.perf_counter()
 #  print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    
    
if __name__ == "__main__":
    main()