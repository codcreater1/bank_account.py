from bank_account import * 

Murat = BankAccount(1000,"Murat")
Can = BankAccount(2000,"Can")

Murat.getBalance()
Can.getBalance()

Murat.deposit(100)
Can.withdraw(4000)
Can.withdraw(10)

Murat.transfer(1000,Can)
