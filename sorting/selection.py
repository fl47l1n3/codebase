import sys


def sort(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return array


if __name__ == '__main__':
    values = list(map(int, open(sys.argv[1], 'r').read().split()))
    print(sort(values))
