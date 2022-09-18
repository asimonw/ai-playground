def binary_search(a: list, x: any, pos=0):
    if len(a) == 0:
        return -1
    
    mid = len(a) // 2
    guess = a[mid]
    if guess == x:
        return pos + mid
    if guess < x:
        return binary_search(a[mid+1:], x, pos + mid + 1)
    else:
        return binary_search(a[:mid], x, pos)


if __name__ == '__main__':
    a = [1,3,4,7,9]
    print(binary_search(a, 0))
    print(binary_search(a, 1))
    print(binary_search(a, 2))
    print(binary_search(a, 3))
    print(binary_search(a, 4))
    print(binary_search(a, 5))
    print(binary_search(a, 6))
    print(binary_search(a, 7))
    print(binary_search(a, 8))
    print(binary_search(a, 9))
    print(binary_search(a, 10))