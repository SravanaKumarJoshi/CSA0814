n=5
a,b= 0,1
for i in range(n):
  for _ in range(i+1):
    print(a, end=' ')
    a,b = b, a+b
    print()
