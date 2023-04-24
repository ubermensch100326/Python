S = input("Enter the coordinate of the Knight : ")
X = "abcdefgh"
x = (int(X.index(S[0])) + 1)
y = int(S[1])
count = 0

x_move = [-2, -1, 1, 2, 2, 1, -1, -2]
y_move = [-1, -2, -2, -1, 1, 2, 2, 1]

for i in range(8):
    x += x_move[i]
    y += y_move[i]
    if (1 <= x <= 8) and (1 <= y <= 8):
        count += 1
    x = (int(X.index(S[0])) + 1)
    y = int(S[1])

print(count)
