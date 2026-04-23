arr = [45,34,24,31,3,4]

def quick_sort(arr, low, high): 
    if low < high: 
        key = partition(arr, low, high)

        print("Step:", arr)

        quick_sort(arr, low, key-1) 
        quick_sort(arr, key+1, high)

    return arr

def partition(arr, low, high): 
    pivot = arr[high]
     
    i = low - 1

    for j in range(low, high): 
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # pivot ko correct location pr daalna 
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


print("Initial:", arr)
quick_sort(arr, 0, len(arr) - 1)
print("Final:", arr)