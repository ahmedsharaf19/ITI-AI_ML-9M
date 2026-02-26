def merge_sort(arr, start_index, end_index):
    if start_index < end_index:
        middle_index = (start_index + end_index) // 2
        merge_sort(arr, start_index, middle_index)
        merge_sort(arr, middle_index + 1, end_index)
        merge(arr, start_index, middle_index, end_index)

def merge(arr, start_index, middle_index, end_index):
    temp = []
    list1 = start_index
    list2 = middle_index + 1

    while list1 <= middle_index and list2 <= end_index:
        if arr[list1] <= arr[list2]:
            temp.append(arr[list1])
            list1 += 1
        else:
            temp.append(arr[list2])
            list2 += 1
    
    while list1 <= middle_index:
        temp.append(arr[list1])
        list1 += 1
    
    while list2 <= end_index:
        temp.append(arr[list2])
        list2 += 1
    
    i = start_index
    while  i <= end_index:
        arr[i] = temp[i - start_index]
        i += 1


if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", array)
    merge_sort(array, 0, len(array) - 1)
    print("Sorted array:", array)