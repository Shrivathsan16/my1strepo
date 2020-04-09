#prints sum of numbers till 10.

import time

'''
num=list(range(1,11))
print("debug statement1"+str(num))
s = sum(num)
print(s)
'''
n = input()
start = time.time()
counter = 0
for i in range (int(n)+1):
    counter += i
print(counter)
#this part of the program prints the time taken.
end = time.time()
print("total execution time:"+str(end - start))

          


