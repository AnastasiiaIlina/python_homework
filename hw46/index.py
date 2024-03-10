import random
import time

# selection sort
test_data = [random.randint(0,100000) for _ in range(1000)] 

def sort_by_selection_method(array):
    for i in range(len(array)): 
        min_index = i 
        for j in range(i+1, len(array)): 
            if array[min_index] > array[j]: 
                min_index = j 
                    
        array[i], array[min_index] = array[min_index], array[i] 

    return array

def sort_by_merge_method(array):
    if len(array) > 1:

        mid = len(array)//2

        L = array[:mid]
        R = array[mid:]

        sort_by_merge_method(L)
        sort_by_merge_method(R)
 
        i = j = k = 0
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    return array
 
 
if __name__ == '__main__':
    selection_start_time = time.time()
    selection_sort_array = sort_by_selection_method(test_data)
    selection_end_time = time.time()

    merge_start_time = time.time()
    merge_sort_array = sort_by_merge_method(test_data)
    merge_end_time = time.time()

    print("Execution time for selection sort:", selection_end_time-selection_start_time, "seconds")
    print("Execution time for merge sort:", merge_end_time-merge_start_time, "seconds")


# result:
# Execution time for selection sort: 0.02332592010498047 seconds
# Execution time for merge sort: 0.0013699531555175781 seconds
    
# На великих наборах данних сортування злиттям буде працювати
# швидше аніж сортування вставкою. Сотрування вставкою слід використовувати
# для невеликих наборів данних



 
  

