
# operations
operations = (
           "1.Balance\n",
           "2.Withdraw\n",
           "3.Deposit\n",
           "4.Transfer\n",
           "5.History\n",
           "6.Logout\n",
)


# accounts_table

accounts ={12345:"6789"}

#user_details table
user_details = {
    12345 : ["gopikrishna",1000, "gopikrishna6547@gmail.com"]
}

# login function
def login(user_name:int,password:str):
    #checking account user_name present in account table or not
    if user_name in accounts:
        if accounts [user_name] == password:
            print("Successfully login in to gopikrishna6547 online netbanking")
        else:
            print("check your user creditials ")
    else:
        print("user not found")
    return False

# operations functions creation
# balance function creation
def balance (user_name : int):
    print(" i am in balance page")
    pass

#withdraw function creation 
def withdraw(user_name: int ,withdraw_amount:int):
    print( "i am in withdraw page")
    pass

#depsoit function creation
def deposit(user_name :int ,deposit_amount :int):
    print(" i am in deposit page")
    pass

#Transfer function defination
def transfer (to_account: int,amount:int):
    print(" i am in transfer page")
    pass

#mini statement function creation
def ministatement(user_name :int):
    print("i am in a mini statement page")
    pass

# logout function creation
def logout():
    pass


# main function
if __name__ == "__main__":
    print("welcome to gopikrishna online netbanking app")
    account =int(input("please enter your account number:"))
    password =input("please enter the password:")
    while login (user_name=account ,password=password):
        print(*operations)
        choice = int(input("please select your operation:"))
        if choice ==1:
            balance(user_name=account)
        elif choice ==2:
            withdraw(user_name=account ,withdraw_amount=0)    
        elif choice ==3:
            deposit(user_name=account , deposit_amount =0)
        elif choice ==4:
            transfer(user_name=account , transfer_amount=0)
        elif choice ==5:
            ministatement(user_name=account )
        elif choice ==6:
            logout()
        else :
            print("please enter between 1-6") 


        break

