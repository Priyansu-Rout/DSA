# Find the Second Largest Element in an Array

##  Brute Force Approach
```python
class Solution:
    def getSecondLargest(self, arr):
        arr = list(set(arr))
        arr.sort()
        return arr[-2]  
```

- TC :- $$\mathcal{O}(n \log n)$$
- SC :- $$\mathcal{O}(1)$$

## Optimal Solution (Single Pass)
```python
def SecondLargest(arr):
	largest = float('-inf')
	s_largest = float('-inf')
	n = len(arr)
	for i in range(0,n):
		if arr[i]>largest:
			s_largest = largest
			largest = arr[i]
		elif arr[i]>s_largest and arr[i]!=largest:
			s_largest = arr[i]
	return s_largest
```
- TC:- $$mathcal{O}(n)$$
- SC:- $$mathcal{O}(1)$$
