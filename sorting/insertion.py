import sys


def sort_while(array):
    i = 0
    while i < len(array):

        j = i
        while j > 0:
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break
            j -= 1

        i += 1

    return array


def sort_forloop(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
            else:
                break
    return array


sort = sort_forloop


if __name__ == '__main__':
    values = list(map(int, open(sys.argv[1], 'r').read().split()))
    print(sort(values))
