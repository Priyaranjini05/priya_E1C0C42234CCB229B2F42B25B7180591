def fact-rec(n):
if n==0 or n==1:
  return 1
else:
  return n*fact-rec(n-1)
  number=int(input("Enter the value:"))
  res=fact-rec(number)
  print("The factorial of{} is {}.".format(number,yes))