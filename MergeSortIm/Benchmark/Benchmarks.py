import random
from csv import writer
import time

from MergeSortIm.MergeSort import mergeSort


def test_merge_sort(dataset):
    t1 = time.time()
    mergeSort(dataset)
    t2 = time.time()
    return "%.8f" % (t2 - t1)


def merge_sort_bench(iteration):
    n = 100
    for i in range(iteration):
        dataset = [random.randint(1, 10000) for i in range(n)]
        mergeSort(dataset)
        with open('Datasets/mergeSort.csv', 'a') as case:
            write_line = writer(case)
            write_line.writerow([len(dataset)] + [test_merge_sort(dataset)])
        n += 100

merge_sort_bench(500)
