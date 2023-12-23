def lengthOfLIS(nums):
    # Binary search approach
    n = len(nums)
    ans = []

    # Initialize the answer list with the
    # first element of nums
    ans.append(nums[0])

    for i in range(1, n):
        if nums[i] > ans[-1]:
            # If the current number is greater
            # than the last element of the answer
            # list, it means we have found a
            # longer increasing subsequence.
            # Hence, we append the current number
            # to the answer list.
            ans.append(nums[i])
        else:
            # If the current number is not
            # greater than the last element of
            # the answer list, we perform
            # a binary search to find the smallest
            # element in the answer list that
            # is greater than or equal to the
            # current number.
            low = 0
            high = len(ans) - 1
            while low < high:
                mid = low + (high - low) // 2
                if ans[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            # We update the element at the
            # found position with the current number.
            # By doing this, we are maintaining
            # a sorted order in the answer list.
            ans[low] = nums[i]

    # The length of the answer list
    # represents the length of the
    # longest increasing subsequence.
    return [len(ans), [ans]]

arr = [4, 1, 13, 7, 0, 2, 8, 11, 3]
print("The array is: " + str(arr))
print("The length of the LIS is: " + str(lengthOfLIS(arr)[0]))
print("The LIS is: " + str(lengthOfLIS(arr)[1]) + "\n")
