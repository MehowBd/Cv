# Michał Badura, 407049

from typing import List, Tuple

def quicksort(tab) -> None:
    new_tab = tab.copy()
    def quicksort_inplace(new_tab, start = 0, stop = len(tab) - 1):
        i = start
        j = stop
        pivot = new_tab[(i+j) // 2]

        while i < j:
            while new_tab[i] < pivot:
                i += 1
            while new_tab[j] > pivot:
                j -= 1
            if i <= j:
                new_tab[j], new_tab[i] = new_tab[i], new_tab[j]
                i += 1
                j -= 1
            if start < j:
                quicksort_inplace(new_tab, start, j)
            if i < stop:
                quicksort_inplace(new_tab, i, stop)
            return new_tab
    return quicksort_inplace(new_tab)


def bubblesort(tab) -> Tuple[List[int], int]:
    new_tab = tab.copy()
    n = len(new_tab)
    swap = 1
    i = 0
    while swap:
        swap = 0
        for j in range (1,n):
            i += 1
            if new_tab[j-1] > new_tab[j]:
                new_tab[j-1], new_tab[j] = new_tab[j], new_tab[j-1]
                swap = 1
        n -= 1
    return new_tab,i


