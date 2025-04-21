import math
import time

#O(1)-constant Time
def get_10000th_eement(data):
    return data[9999]

data_O1 = list(range(1000000))
start_time = time.time()
first = get_10000th_eement(data_O1)
end_time = time.time()
print(f"O(1):10000th element is {first}, time taken:{end_time :.16f} seconds")

#O(log n)- logarithmic Time (binary search)

def search(data, target):
  left, right = 0,len(data) - 1
  while left <= right : 
     mid = (left + right)//2
     if data[mid] == target:
        return mid
     elif data[mid] < target:
        left = mid + 1
     else:
        right = mid - 1
  return - 1

data_for_Ologn = sorted(list(range(1,1000001)))

start_time = time.time()
index = search(data_for_Ologn,1000000)
end_time = time.time()

print(f"Olog(n) : found at index, {index}, took {end_time:.16f} secomds")

#O(n) - linear time

def get_elements(data, target):
   for element in data:
      if element == target:
         return True
      else :
         return False 

data_On = list(range(1,1000001))
start_time = time.time()
found = get_elements(data_On, 1000000)
end_time = time.time()
print(f"O(n) : {found}, took {end_time :.16f} seconds")


#O(nlog(n)) - linearithmic time 

def merge_sort(data):
   if len(data) <= 1:
      return data
   mid = len(data)//2
   left = merge_sort(data[:mid])
   right = merge_sort(data[mid:])
   return merge(left,right)

def merge(left, right):
   merged = []
   left_idx, right_idx = 0,0
   while left_idx < len(left) and right_idx < len(right):
      if left[left_idx] <= right[right_idx]:
         merged.append(left(left_idx))
         left_idx += 1
      else:
         merged.append(right[right_idx])
         right_idx += 1

   merged.extend(left[left_idx:])
   merged.extend(right[right_idx:])
   return merged

data_Onlogn = list(range(10000, 0 , -1))
start_time = time.time()
sorted_data = merge_sort(data_Onlogn)
end_time = time.time()
print(f"O(nlog(n)): sorted 1st 5 elements: {sorted_data[:5]}, took:{end_time:.16f} seconds")

#O(n^2)-quadratic Time

def find_copy(data):
   duplicates = []
   n = len(data)
   for i in range(n):
      for j in range(i + 1, n):
         if data[i] == data[i] not in duplicates:
            duplicates.append(data[i])
   return duplicates

data_On2 = list(range(1, 101))*2 
start_time = time.time()
copies = find_copy(data_On2)
end_time = time.time()
print(f"O(n^2): copies found: {copies[:10]}, took:{end_time:.16f} seconds")

#O(n^k) - polynomial Timme : k = 4 (ttriple nested loop)

def iter(n):
   count = 0
   for i in range(n):
      for j in range(n):
         for k in range(n):
            for l in range(n):
               count += 1
   return count

n_onk = 50
start_time = time.time()
oper = iter(n_onk)
end_time = time.time()
print(f"O(n^4): number of operations : {oper}, time taken : {end_time:.16f} seconds")
    