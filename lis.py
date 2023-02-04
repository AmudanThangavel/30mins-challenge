def longest_increasing_subsequence(nums):
    l = len(nums)
    result = [1 for _ in range(l)]
    for i in range(l):
        for j in range(i):
            if nums[j] < nums[i]:
                result[i] = max(result[i], result[j] + 1)
    # print(result)
    return max(result)


testcase = [[10, 9, 2, 5, 3, 7, 101, 8], [
    1, 3, 6, 7, 9, 10, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
for test in testcase:
    print("ANSWER", longest_increasing_subsequence(test))
