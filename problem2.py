def min_operations(arr, k):
    arr.sort()
    target = arr[len(arr)//2]

    total_ops = 0

    for num in arr:
        if (num - target) % k != 0:
            return -1
        total_ops += abs(num - target) // k

    return total_ops



n = int(input("Enter N: "))
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))

print(min_operations(arr, k))