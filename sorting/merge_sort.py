import math

def merge(sorted_left, sorted_right):
    sorted = []
    l_idx = 0
    r_idx = 0

    while l_idx < len(sorted_left) and r_idx < len(sorted_right):
        if sorted_left[l_idx] < sorted_right[r_idx]:
            sorted.append(sorted_left[l_idx])
            l_idx += 1
        else:
            sorted.append(sorted_right[r_idx])
            r_idx += 1

    while l_idx < len(sorted_left):
        sorted.append(sorted_left[l_idx])
        l_idx += 1

    while r_idx < len(sorted_right):
        sorted.append(sorted_right[r_idx])
        r_idx +=1

    return sorted

def merge_sort(items):
    if len(items) == 1:
        return items
    
    middle = math.floor(len(items) / 2)

    left = merge_sort(items[0:middle])
    right = merge_sort(items[middle:])

    return merge(left, right)


if __name__ == "__main__":

    arr = [7,3,9,4,2]

    sorted = merge_sort(arr)

    if sorted != [2,3,4,7,9]:
        print("ERROR! Expected sorted [7,3,9,4,2] to equal [2,3,4,7,9]")
        print(f"Instead got: {sorted}")