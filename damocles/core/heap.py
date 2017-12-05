def heapify(lst, start, end):
    father = start
    child = father * 2 + 1

    while child <= end:
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1

        if lst[father] >= lst[child]:
            break
        else:
            lst[father], lst[child] = lst[child], lst[father]
            father = child
            child = father * 2 + 1


def heap_sort(lst):
    length = len(lst)

    for i in range(length // 2 - 1, -1, -1):
        heapify(lst, i, length - 1)

    for i in range(length - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, 0, i - 1)


if __name__ == '__main__':
    test_lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    heap_sort(test_lst)
    print(test_lst)
