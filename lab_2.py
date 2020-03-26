from lab1 import bubble_sort, quick_sort

def onsets(list,function,threshold):
    counter = 3
    results = []
    numbers = []
    n = len(list)
    for i in range(n):
        while len(results) < counter:
            if list[i] > threshold:
                results.append(i)
                numbers.append(list[i])
                i += 1

            else:
                i += 1

    function(numbers)
    for j in range(len(numbers)):
        print(list.index(numbers[j]))



onsets([3,6,2,9,5,6],bubble_sort,3)
onsets([3,6,2,9,5,6],quick_sort,3)



