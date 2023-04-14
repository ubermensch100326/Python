class Tutorial:
    def __init__(self):  # 클래스를 선언하는 순간 실행되는 함수
        self.name = input("Name : ")  # self는 클래스 자기자신을 의미
        self.age = input("Age : ")

    def show(self):  # Tutorial.show()로 실행
        print("My name is {}.\nI'm {} years old.".format(self.name, self.age))


# test = Tutorial()
# test.show()


class Tutorial2(Tutorial):  # 클래스 상속
    def __init__(self):
        super().__init__()  # super는 상속한 클래스, Tutorial을 의미
        self.sex = input("Sex : ")

    def show(self):
        super().show()
        print("I'm {}.".format(self.sex))

    def __real__(self):
        return len


test2 = Tutorial2()
test2.show()
print(test2.__real__())


class Tutorial3(Tutorial2):
    pass  # 상속한 클래스를 그대로 들고옴옴


test3 = Tutorial3()
test3.show()
