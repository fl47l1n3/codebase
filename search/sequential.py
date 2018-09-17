import sys


def search_simple(val, array):
    result = False, 0

    for i in range(len(array)):
        if val == array[i]:
            result = True, i

    return result


def search_optimized(val, array):
    result = False, 0

    for i in range(len(array)):
        if val == array[i]:
            result = True, i
        elif val < array[i]:
            break

    return result


search = search_optimized


if __name__ == '__main__':
    values = list(map(int, open(sys.argv[1], 'r').read().split()))
    val = int(sys.argv[2])
    print(search(val, sorted(values)))
