A bunch of sorts implemented in python. Timed for performance benchmarks.

Everything is a Sort object. To sort some data, create a new instance of Sort:

new_sort = Sort(data_here)

To perform a sort, call one of the object's sort methods:

new_sort.mergeSort()

Implemented sorts so far:

-Merge sort

-Bubble sort

-Selection sort

-Insertion sort

-Comb sort

-Shell sort

To time a sort, call the timedRun method. Pass it one of the object's own sort methods:

new_sort.timedRun(new_sort.mergeSort())

TODO:

-Clean up

-Implement more sorts
