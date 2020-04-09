#this program prints all odd numbers  till the given input.

import time

s=input()
start = time.time()

num=list(range(1,int(s),2))
print(num)

end = time.time()
print("total execution time:"+str(end - start))

          

