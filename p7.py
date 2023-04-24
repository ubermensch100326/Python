S = input("Enter the string : ")
A = []
B = ""
C = ""
temp = 0

for s in S:
    if (ord('0') <= ord(s) <= ord('9')):
        temp += int(s)
    else:
        if (len(A) == 0):
            A.append(s)
        else:
            for i in range(len(A)):   # sort 함수 못 쓰는 줄 알았음..
                if (ord(s) > ord(A[i])):
                    if (i == (len(A) - 1)):
                        A.insert((i + 1), s)
                        break
                    else:
                        continue
                elif (ord(s) <= ord(A[i])):
                    A.insert(i, s)
                    break
                else:
                    print("Unknown Error!")

for a in A:
    C += a

if (temp == 0):
    print(C)
else:
    B += str(temp)
    print(C + B)
