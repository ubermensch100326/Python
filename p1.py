# import time


# N = int(input("Enter the N : "))
# K = int(input("Enter the K : "))

# # N, K = map(int, input().split())

# count = 0

# start = time.time()
# while (N != 1):
#     if (N % K != 0):
#         N -= 1
#         count += 1
#     else:
#         N /= K
#         count += 1

# print(f"Least Time : {count}")

# print(f"Execution Time : {time.time() - start}")


N, K = map(int, input("Enter the N, K : ").split())

count = 0

while True:
    target = (N // K) * K
    count += N - target
    N = target
    if (N < K):
        break
    else:
        N /= K
    count += 1

count += (N - 1)

print(count)
