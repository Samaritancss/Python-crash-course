from bank_accounts2 import *

Dave = BankAccount(2000, "Dave")
Abigail = BankAccount(1000, "Abigail")

Dave.getBalance()
Abigail.getBalance()

Dave.deposit(800)

Abigail.withdraw(700)

Dave.transfer(800, Abigail)

Nat = InterestRewardsAcct(2000, "Nat")

Nat.getBalance()

Nat.deposit(200)

Nat.transfer(350, Abigail)

Kim = SavingsAcct(2200, "Blaze")

Kim.getBalance()

Kim.deposit(150)

Kim.transfer(450, Dave)



