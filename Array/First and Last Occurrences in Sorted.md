# First and Last Occurrences in Sorted Array

[visualize](https://pythontutor.com/visualize.html#code=def%20find%28arr,%20x%29%3A%0A%20%20%20%20n%20%3D%20len%28arr%29%0A%20%20%20%20%0A%20%20%20%20%23%20Initialize%20first%20and%20last%20index%0A%20%20%20%20first%20%3D%20-1%0A%20%20%20%20last%20%3D%20-1%0A%20%20%20%20%0A%20%20%20%20for%20i%20in%20range%28n%29%3A%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20If%20x%20is%20different,%20continue%0A%20%20%20%20%20%20%20%20if%20x%20!%3D%20arr%5Bi%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20continue%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20If%20first%20occurrence%20found%0A%20%20%20%20%20%20%20%20if%20first%20%3D%3D%20-1%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20first%20%3D%20i%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20Update%20last%20occurrence%0A%20%20%20%20%20%20%20%20last%20%3D%20i%0A%20%20%20%20res%20%3D%20%5Bfirst,%20last%5D%0A%20%20%20%20return%20res%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20arr%20%3D%20%5B1,%203,%205,%205,%205,%205,%207,%20123,%20125%5D%0A%20%20%20%20x%20%3D%205%0A%20%20%20%20res%20%3D%20find%28arr,%20x%29%0A%20%20%20%20print%28res%5B0%5D,%20res%5B1%5D%29&curInstr=36&mode=display&origin=opt-frontend.js&py=311)

```python
def find(arr, x):
    n = len(arr)
    
    # Initialize first and last index
    first = -1
    last = -1
    
    for i in range(n):
        
        # If x is different, continue
        if x != arr[i]:
            continue
        
        # If first occurrence found
        if first == -1:
            first = i
        
        # Update last occurrence
        last = i
    res = [first, last]
    return res

if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 5, 7, 123, 125]
    x = 5
    res = find(arr, x)
    print(res[0], res[1])
```
`O(n) Time and O(1) Space`
