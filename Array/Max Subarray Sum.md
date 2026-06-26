# Max Subarray Sum
## Brute Force Approach
```python
class Solution:
    def maxSubarraySum(self, arr):
        n = len(arr)
        maxi = float('-inf')
        for i in range(0,n):
            total = 0
            for j in range(i,n):
                total = total+ arr[j]
                maxi = max(total,maxi)
        return maxi
```
- Time Complexity O($n^2$)
- Space Complexity o(1)

## Kadane's Algorithm
```python
class Solution:
    def maxSubarraySum(self, arr):
        n = len(arr)
        maxi = float('-inf')
        total = 0
        for i in range(0,n):
            total = total+arr[i]
            maxi = max(total,maxi)
            if total<0:
                total = 0
        return maxi
```
-  Time Complexity O(n)
- Space Complexity o(1)
