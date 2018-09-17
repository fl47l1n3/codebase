import sys


def search_recursive(val, array):
    mid = len(array) / 2

    if val == array[mid]:
        return True, array.index(val)
    elif len(array) <= 1:
        return False, 0

    if val < array[mid]:
        return search_recursive(val, array[:mid])
    elif val > array[mid]:
        return search_recursive(val, array[mid:])


def search_loop(val, array):
    lo = 0
    hi = len(array)

    while lo != hi:
        mid = (lo + hi) / 2
        if val == array[mid]:
            return True, array.index(val)
        elif val < array[mid]:
            hi = mid - 1
        elif val > array[mid]:
            lo = mid + 1

    return False, 0


search = search_loop


if __name__ == '__main__':
    values = list(map(int, open(sys.argv[1], 'r').read().split()))
    val = int(sys.argv[2])
    print(search(val, sorted(values)))
