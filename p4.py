N = int(input("Enter the N (1 <= N <= 100) : "))
S = map(str.upper, input("Enter the direction plan : "))


# R, L, D, U
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
x = 1
y = 1

for s in S:
    if s == "R":
        if y == N:
            continue
        else:
            x += dx[0]
            y += dy[0]
    elif s == "L":
        if y == 1:
            continue
        else:
            x += dx[1]
            y += dy[1]
    elif s == "D":
        if x == N:
            continue
        else:
            x += dx[2]
            y += dy[2]
    elif s == "U":
        if x == 1:
            continue
        else:
            x += dx[3]
            y += dy[3]
    else:
        print("Unknown Error!")

print(f"Destination : {x} {y}")
