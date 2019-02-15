# See README.md for documentation

def find_maxima(array):
    """Returns the positions of the local maximum values in the array
    array.

    Example:
    find_maxima([]) → []
    find_maxima([1, 2, 1]) → [1]
    find_maxima([2, 0, 0, -2, 2]) → [0, 4]
    """
    ans = []
    N = len(array)
    for i in range(N):
        if (array[i] > array[i-1] and
            (i >= N or array[i] > array[i+1])):
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
