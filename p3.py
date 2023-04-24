phobia = list(
    map(int, input("Enter the list of the phobia levels : ").split()))

phobia.sort()

target = phobia[0]
index = (target - 1)
index2 = 0
count = 0
temp = 0

while (index <= len(phobia) - 1):
    if (target == phobia[index]):
        count += 1
        if (index == (len(phobia) - 1)):  # index가 리스트의 마지막 원소를 가리킬 경우 탈출
            break
        target = phobia[index + 1]
        index2 = index
        index += target
        temp = 0
    else:
        temp += (index - index2)  # 지금까지 모인 사람들 수
        target = phobia[index]
        index2 = index  # index2는 바로 이전 index를 추적함 (temp를 구하기 위해서)
        index += (target - temp)  # 추가적으로 더 필요한 사람 수만큼만 이동

print(count)
