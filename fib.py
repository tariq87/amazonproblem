#Fibonacci Series
def fibnac(s):
  n = len(s)
  fib = [0]*(n+1)
  fib[1] = 1
  sm = fib[0]+fib[1]
  for i in range(2,n+1):
    fib[i] = fib[i-1]+fib[i-2]
    sm += fib[i]
  fin = list(zip(s,map(str,fib[1:])))
  return str(sm)+"".join(sum(fin,()))


print(fibnac("beautiful"))
