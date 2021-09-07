#left shift array by N places
def leftshift(arr,n):
  n = n%len(arr)
  print(arr[n:]+arr[:n])

leftshift([1,2,3,4,5],111)