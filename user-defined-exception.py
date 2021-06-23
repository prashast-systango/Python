#This is a user defined exception
class UserException(Exception):
    pass

def checkBalance(amount):
    balance = 10000
    withdraw = amount
    try:
        avl_balance = balance - withdraw
        if(avl_balance < 0):
            raise UserException("Insufficient Balance")  # user defined exception raised here
        print("Available Balance :",avl_balance)
    except UserException as e:
        print(e)    
    
amount1 = int(input("Enter amount you want to withdraw :"))
checkBalance(amount1)