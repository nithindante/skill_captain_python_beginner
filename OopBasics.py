class BankAccount:
  def __init__(self,accountNo,name,balance):
    self.accountNo = accountNo
    self.name = name
    self.balance = balance
  def deposit(self,amount):
    self.balance = self.balance + amount
    print("Deposited",amount,"into account",self.accountNo)
  def withdraw(self,amount):
    self.balance = self.balance - amount
    print("Deposited",amount,"into account",self.accountNo)
  def __str__(self):
    return f"Account No:{self.accountNo} , Name:{self.name}, Balance:{  self.balance}"
sbi = BankAccount(1234,"Ram",1000)
print(sbi)
