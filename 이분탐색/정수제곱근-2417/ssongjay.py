import sys

input_ = sys.stdin.readline


def binary_search(N, start, end):
    if start > end:
        return start
    mid = (start + end) // 2
    if mid * mid < N:
        return binary_search(N, mid + 1, end)
    else:
        return binary_search(N, start, mid - 1)


N = int(input_())

print(binary_search(N, 0, N))
