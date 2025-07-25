v = [5, 3, 2, 4, 7, 1, 0, 6]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    sorted_v = bubble_sort(v)
    print("Sorted:", sorted_v)
    assert sorted_v == [0, 1, 2, 3, 4, 5, 6, 7], "Erro"
