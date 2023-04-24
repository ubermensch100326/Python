import time

N = int(input("Enter the N : "))
h = 0
m = 0
s = 0
count = 0

start = time.time()

while ((h*60*60 + m*60 + s) <= (N*60*60 + 59*60 + 59)):
    H = str(h)
    M = str(m)
    S = str(s)
    if "3" in H or "3" in M or "3" in S:
        count += 1
        # print(H + "h" + M + "m" + S + "s")
    s += 1
    if (s == 60):
        m += 1
        s = 0
    if (m == 60):
        h += 1
        m = 0

print(f"Number of Cases : {count}")
print(f"Elapsed Time : {time.time() - start}")
