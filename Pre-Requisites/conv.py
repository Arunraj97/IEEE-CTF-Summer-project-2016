print" Enter 1 if you want to convert dec to bin"
print" Enter 2 if you want to convert bin to dec"

x=input("Enter your choice: ")
if x==1:
  i=1
  s=0
  dec=input("Enter decimal to be converted: ")
  while dec>0:
      rem=dec%2
      s=s+(i*rem)
      dec=dec/2
      i=i*10
  print "The binary of the given number is ",s,'.'
else:
  bin=raw_input ('Enter binary to be converted: ')
  n=len(bin)
  res=0
  for i in range(1,n+1):
      res=res+ int(bin[i-1])*2**(n-i)
  print "The decimal of the given binary is ",res,'.'
