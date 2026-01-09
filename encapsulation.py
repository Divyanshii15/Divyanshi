# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance

#     def show_balance(self):
#         return self.__balance
    

# x=BankAccount("Divyanshi", 1500)
# # x.add_amount(300)
# print(x.show_balance())


# class ATM:
#     def __init__(self, pin, bal):
#         self.__pin=pin
#         self.__bal=bal
#     def check__bal(self,pin):

#         if pin == self.__pin:
#             return self.__bal
#         # ("Transaction Compelete. ")
#         else:
#             return "Incorrect PIN"
# x=ATM(1530,1510)
# print(x.check__bal(1510))


class employee:
    def __init__(self):
        self.name=None
        self.__salary=0
def set_details(self,name,salary):
    self.name=name
    if salary>0:
        self.__salary =salary
    else:
        print('Salary must be Positive!!')
def show_name(self):
    print("Employee Name: ", self.name)
def update_salary(self,amount):
    if amount > 0:
        self.__salary +=amount
        print("Salary Upadated Successfully ")

        def show_salary(self):
            print("Current Salary:", self.__salary)

emp=employee("Divyanshi", 25000)
print("Employee Name: "emp.set_detail)
emp.show_name()
emp.update_salary(5000)
emp.show_salary()
