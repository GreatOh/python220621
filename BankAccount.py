# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)

#이름에 접근... 하면 에러나고
#print(account1.__balance)

#비록 쓰기는 안되지만
_BankAccount__balance = 0

# 이렇게 하면 에러 안나게 조회는 된다.(백도어)
print(account1._BankAccount__balance)
print(account1)
