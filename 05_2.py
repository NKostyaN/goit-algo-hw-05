def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    iter_count = 0
    biggest = arr[-1]

    while low <= high:
        iter_count += 1
        mid = (high + low) // 2

        if arr[mid] < item:
            low = mid + 1

        elif arr[mid] > item:
            high = mid - 1
            biggest = arr[mid]

        else:
            return [iter_count, biggest]

    return "Not found"


def main():
    data = [1.53, 3.32, 5.64, 8.09, 10.28, 12.48, 15.02, 18.82, 20.48, 22.73, 24.27]
    print(binary_search(data, 12.48))
    print(binary_search(data, 18.82))
    print(binary_search(data, 24.27))
    print(binary_search(data, 1.53))
    print(binary_search(data, 9.99))


if __name__ == "__main__":
    main()
