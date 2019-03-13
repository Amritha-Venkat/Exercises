def array_reverse(arr):
    print(" ".join(map(str,arr[::-1])))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    array_reverse(arr)