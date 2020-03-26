def bubble_sort(list):
    n = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if list[i] < list[i + 1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swapped = True


def partition(list,low,high):
    middle = list[(low + high)//2]
    i = low-1
    j = high+1
    while True:
        i += 1
        while list[i] > middle:
            i += 1
        j -= 1
        while list[j] < middle:
            j -= 1
        if i >= j:
            return j

        temp = list[i]
        list[i] = list[j]
        list[j] = temp


def quick_sort(list):
    N = len(list)
    def quick(num,low,high):
        if low < high:
            split_index = partition(num, low, high)
            quick(num, low, split_index)
            quick(num, split_index + 1, high)

    quick(list, 0, N-1)

