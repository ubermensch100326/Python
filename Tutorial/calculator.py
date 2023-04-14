class Stack:  # Stack 클래스 정의
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty!")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty!")

    def __len__(self):
        return len(self.items)


def inToPost(expression):  # infix를 postfix로 바꾸는 함수 정의
    outStack = Stack()
    opStack = Stack()
    for token in expression:
        if token not in '+-*/' and token not in '()':
            outStack.push(token)
        elif token == '(':
            opStack.push(token)
        elif token in '+-*/':
            if opStack.top() == '*' or opStack.top() == '/':
                outStack.push(opStack.top())
                opStack.pop()
                opStack.push(token)
            else:
                opStack.push(token)
        else:
            while (opStack.top() != '('):
                outStack.push(opStack.top())
                opStack.pop()
            opStack.pop()
    while (len(opStack) != 0):
        outStack.push(opStack.top())
        opStack.pop()
    return outStack


testExpression = input("Enter the experssion : ")
postExpression = inToPost(testExpression)


def reverseStack(inStack):  # 스택의 원소를 거꾸로 하는 함수 정의
    outStack = Stack()
    while (len(inStack) != 0):
        outStack.push(inStack.top())
        inStack.pop()
    return outStack


reverseExpression = reverseStack(postExpression)


def stackToList(inStack):  # 스택을 리스트로 변환하는 함수 정의
    temp = []
    while (len(inStack) != 0):
        temp.append(inStack.top())
        inStack.pop()
    return temp


listExpression = stackToList(reverseExpression)
print(listExpression)


def calculator(inList):  # 리스트와 스택을 이용하여 계산하는 함수 정의
    temp = Stack()
    for element in inList:
        if element not in '+-*/':
            temp.push(element)
        elif element is '+':
            bValue = temp.top()
            temp.pop()
            aValue = temp.top()
            temp.pop()
            temp.push(float(aValue) + float(bValue))
        elif element is '-':
            bValue = temp.top()
            temp.pop()
            aValue = temp.top()
            temp.pop()
            temp.push(float(aValue) - float(bValue))
        elif element is '*':
            bValue = temp.top()
            temp.pop()
            aValue = temp.top()
            temp.pop()
            temp.push(float(aValue) * float(bValue))
        elif element is '/':
            bValue = temp.top()
            temp.pop()
            aValue = temp.top()
            temp.pop()
            temp.push(float(aValue) / float(bValue))
    result = float(temp.top())
    return result


print(calculator(listExpression))
