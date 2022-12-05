
# creating a function for insertion  
def insertion_sort(arr):  
  
        # Outer loop to traverse through 1 to len(arr)  
        for i in range(1, len(arr)):  
  
            value = arr[i]  
  
            # Move elements of arr[0..i-1], that are  
            # greater than value, to one position ahead  
            # of their current position  
            j = i - 1  
            while j >= 0 and value < list1[j]:  
                arr[j + 1] = arr[j]  
                j -= 1  
            arr[j + 1] = value  
        return arr  
            # Driver code to test above  
  
arr = [10, 5, 13, 8, 2]  
print("The unsorted arr is:", arr)  
  
print("The sorted arr is:", insertion_sort(arr))  
