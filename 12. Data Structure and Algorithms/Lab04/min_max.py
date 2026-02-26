def min_max(arr, start_index, end_index):
    if start_index == end_index:
        min = max = arr[start_index]
        return min, max
    elif end_index - start_index == 1:
        if arr[start_index] > arr[end_index]:
            min = arr[end_index]
            max = arr[start_index]
        else :
            min = arr[start_index]
            max = arr[end_index]
        
        return min, max
    else :
        middle_index = (start_index + end_index) // 2
        min1, max1 = min_max(arr, start_index, middle_index)
        min, max = min_max(arr, middle_index+1, end_index)
        if max1 > max: 
            max = max1
        if min1 < min :
            min = min1
        return min, max


if __name__ == "__main__":
    array = [-5, 100, -1, 10, 0, 5000]
    min, max = min_max(array, 0, len(array)-1)
    print(f"Min = {min}")
    print(f"Max = {max}")