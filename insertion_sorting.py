arr = [9,6,4,2,5,1]

def insertation_sort(arr):
    for i in range(1, len(arr)): 
        key = arr [i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j-=1

        arr[j + 1] = key 
        print(f"Step {i}:", arr)

    return arr

print(insertation_sort(arr)) 

