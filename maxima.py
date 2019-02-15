# lbasdfasdf sadfasdf

def find_maxima(arr):
    """Returns the positions of the local maximum values in the array
    arr.

    Example:
    find_maxima([]) → []
    find_maxima([1, 2, 1]) → [1]
    find_maxima([2, 0, 0, -2, 2]) → [0, 4]
    """
    ans = []
    for i in range(len(arr)):
        if (arr[i] > arr[i-1] and
            arr[i] > arr[i+1]):
            ans.append(i)
    return ans

examples = [
    [],
    [1, 2, 1],
    [2, 0, 0, -2, 2],
]

def test_find_maxima():
    for example in examples:
        ans = find_maxima(example)
        print(example, '→', ans)
