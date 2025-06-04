class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def merge(arr, low, mid, high):
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]

        def countPairs(arr, low, mid, high):
            cnt = 0
            right = mid + 1
            for i in range(low, mid + 1):
                while right <= high and arr[i] > 2 * arr[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt

        def mergeSort(arr, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            cnt = mergeSort(arr, low, mid)
            cnt += mergeSort(arr, mid + 1, high)
            cnt += countPairs(arr, low, mid, high)
            merge(arr, low, mid, high)
            return cnt

        return mergeSort(nums, 0, len(nums) - 1)
