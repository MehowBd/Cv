from timeit import timeit

def time_test():
    if __name__ == '__main__':
        time1_bubble = timeit("from __init__ import List1", "from sort import bubblesort", number = 1000)
        time2_bubble = timeit("from __init__ import List2", "from sort import bubblesort", number=1000)
        time3_bubble = timeit("from __init__ import List3", "from sort import bubblesort", number=1000)
        time4_bubble = timeit("from __init__ import List4", "from sort import bubblesort", number=1000)
        time1_quicksort = timeit("from __init__ import List1", "from sort import quicksort", number=1000)
        time2_quicksort = timeit("from __init__ import List2", "from sort import quicksort", number=1000)
        time3_quicksort = timeit("from __init__ import List3", "from sort import quicksort", number=1000)
        time4_quicksort = timeit("from __init__ import List4", "from sort import quicksort", number=1000)
        return time1_bubble, time2_bubble, time3_bubble, time4_bubble, time1_quicksort, time2_quicksort, time3_quicksort, time4_quicksort
print(time_test())