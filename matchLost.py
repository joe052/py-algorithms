boxGroups = [[140,120,150,100,170,200,90,180],[170,150,140,90,100,120,180,200],[120,90,200,150,180,140,100,170]]

def binary_search(nums,low,high,x):
  while low<=high:
    mid = (low+high)/2
    mid = int(mid)
    if nums[mid]==x:
      return mid
    elif nums[mid]>x:
      high = mid-1
    else:
      low = mid+1
  return -1

def find_index(nums,x):
  i = 1
  l = len(nums)
  while i<l:
    if nums[i-1]==x:
      return i
    elif 2*i<l and nums[2*i-1]>x:
      return binary_search(nums,i-1,2*i-1,x)
    i = 2*i
  return binary_search(nums,i/2,l-1,x)

def main(arr,x): 
  arr = sorted(arr)
  print ("Sorted array: ",arr)
  print (find_index(arr, x))

main(boxGroups[2],180)