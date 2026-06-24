import time
import random


def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        if arr[high] == arr[low]:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

        if pos < low or pos > high:
            return -1, comparisons

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    sizes = [100, 500, 1000, 5000, 10000]

    print(f"{'Size':>8} {'IS Time (ms)':>15} {'BS Time (ms)':>15} {'IS Comparisons':>18} {'BS Comparisons':>18}")
    print("-" * 80)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(f"{size:>8} {is_time:>15.6f} {bs_time:>15.6f} {comp_is:>18} {comp_bs:>18}")


arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
target = 35

idx, comps = interpolation_search(arr, target)

print("Array:", arr)
print("Searching for:", target)

if idx != -1:
    print(f"Found at index: {idx}, Comparisons: {comps}")
else:
    print(f"Not found, Comparisons: {comps}")

print()
performance_analysis()