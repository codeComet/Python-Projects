class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return "%s's account, Balance: $%.2f" % (self.name, self.balance)
   
  def show_balance(self):
    print("Balance: $%.2f" % (self.balance))
    
  def deposit(self, amount):
    if amount <= 0:
      print("Invalid Value!")
      return
    else:
      print("Money $%.2f deposit successful!" % (amount))
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount > self.balance:
      print("Invalid value!")
      return
    else:
      print("You are withdrawing: $%.2f" % (amount))
      self.balance -= amount
      self.show_balance()
  
  my_account = BankAccount("Bishal")
  print(my_account)
  my_account.show_balance()
  my_account.deposit(2000)
  my_account.withdraw(1000)
  print(my_account)







