import threading as th
import time

def proc(n,str):
   print(str, n)
   time.sleep(5)

p = []
j = 1

for i in range(10):
    test = 'Process :'
    for ch in test:
        p.append(th.Thread(target=proc, name="t1", args=[i,ch], daemon=True))
        j+=1

for i in range(j-1):
    p[i].start()


