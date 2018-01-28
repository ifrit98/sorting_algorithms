def bubbleSortv1(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def bubbleSortv2(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1


def selectionSort(list):
    for fillslot in range(len(list)-1, 0, -1):
        positionOfMax = 0

        for location in range(1, fillslot+1):
            if list[location] > list[positionOfMax]:
                positionOfMax = location
        # Swap list at fillslot with list at positionOfMax
        temp = list[fillslot]
        list[fillslot] = list[positionOfMax]
        list[positionOfMax] = temp


# Always maintains a sorted sublist at the front
def insertionsSort(list):
    for index in range(1, len(list)):
        current = list[index]
        position = index

        while position > 0 and list[position-1] > current:
            list[position] = list[position-1]
            position = position-1

        list[position] = current


def mergeSort(list):
# Recurse down to list of size 1
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        mergeSort(left)
        mergeSort(right)
# Merge both sorted halves
        i, j , k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

# Recursive quicksort implementation
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False

   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark

def main():
    alist = [46, 23, 75, 35, 94, 24, 66, 12, 34, 21, 67, 89, 1]
    quickSort(alist)
    print('quickSort: ' + str(alist))
    alist = [46, 23, 75, 35, 94, 24, 66, 12, 34, 21, 67, 89, 1]
    mergeSort(alist)
    print('mergeSort: ' + str(alist))
    alist = [46, 23, 75, 35, 94, 24, 66, 12, 34, 21, 67, 89, 1]
    bubbleSortv1(alist)
    print('bubbleSortv1: ' + str(alist))
    alist = [46, 23, 75, 35, 94, 24, 66, 12, 34, 21, 67, 89, 1]
    bubbleSortv2(alist)
    print('bubbleSortv2: ' + str(alist))
    alist = [46, 23, 75, 35, 94, 24, 66, 12, 34, 21, 67, 89, 1]
    selectionSort(alist)
    print('selectionSort: ' + str(alist))
    alist = [46, 23, 75, 35, 94, 24, 66, 12, 34, 21, 67, 89, 1]
    insertionsSort(alist)
    print('insertionSort: ' + str(alist))

if __name__ == '__main__':
    main()