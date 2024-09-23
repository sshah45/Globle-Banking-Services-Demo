import csv
import re
import os
import string
import random
from tabulate import tabulate
from customer_class import Customer, Transactions






def main():

    select = 0
    
    print()
    effect1 = [["🌎 Welcome to the Global Internet Banking Services"]]                     #effect 1
    print(tabulate(effect1,tablefmt="simple"))
    print()
    effect2 = [["Press 1","Account Login"],["Press 2","Create A New Account"]]             #effect 2
    print(tabulate(effect2,tablefmt="grid"))
    
    # Account Login or to Create a New.
    
    while select < 5:
        
        try:
            x = int(input("\nSelect: "))
            os.system("cls")
            
            
            if x == 1:
                select = 5
                
                
                found = False
                while found == False:
                    A = input("\nAccount Num: ")
                    P = input("Password: ")
                    os.system("cls")
                    
                    try:
                         n, a, p = login(A,P)     # 'n', 'a', 'p' is for name, account number and the pin of the loged in customer.  
                         found = True
                    
                    except ValueError:
                         
                         print("\nEither Account Number or Password is Incorrect Please try Again!")
                         continue
                         
                         
                         
                customer_balance = Transactions(n,a,p)   #Instantiating just to get the Latest Account Balance(because creating this instance will call 'find_acc' method from init).
                
                effect3 = [[f"Welcome  {n}"],[f"Account Balance: ₹{customer_balance.balance:,}"]]                 #effect 3
                print(tabulate(effect3,tablefmt="rst"))
                
                
                while True:
                
                    print()
                    effect4 = [
                               ["Press 1","Deposit Money"],
                               ["Press 2","Withdraw Money"],                        #effect 4
                               ["Press 3","Account Statement"],
                               ["Press 4","Logout"]
                              ]
                    print(tabulate(effect4,tablefmt="grid"))  

                                                                                
                    
                    if functionality(n,a,p) == True:
                         continue
                         
                    else:
                         break
                    
                
                

                    
                    
            elif x == 2:
                 select = 5
                 
                 
                 # Receiving Data form a new customer.
                 
                 print("\nKindly Enter your Details\n")
                 
                 name = customer_name()
                 contact = customer_contact()
                 accnum = gen_accnum()
                 password = customer_password()
                 pin = customer_pin()
                 
                

                 # Instantiating Customer Class to Store the Received Data of a new customer.

                 new_account = Customer(name, contact, accnum, password, pin)
                 new_account.store_data1()
                 new_account.store_data2()

                 effect5= [[f"Please Note Your Account Number: {accnum}"]]                              #effect 5
                 print(tabulate(effect5,tablefmt= "grid"))
                        
                 
           
            else:
                print("1Invalid Input!")
                select += 1
                continue
        
        
        except:

            print("2Invalid Input!")
            select += 1
            continue
                    
                         
                
                
                    
                     
       
                    
                
                 
                 
    
    
    
    

    



def login(accnum,password) -> tuple[str]:      # It will throughly check the csv file and search whether account exists or not. 
                 
    found=False
    row=0          # To know at which row(of the csv) the acc_num matches.
    
    with open("input_data1.csv") as file:
        reader = csv.DictReader(file)
        data = list(reader)     #List of dictionaries.
        
       
        for dictionary in data:
                    row += 1
                    if accnum == dictionary["acc_num"]:
                        found=True
                        matched_dict = data[row-1]
                        break
                    else:
                        continue
        
        if found == False:
            raise ValueError
            
                
        if password == matched_dict["password"]:
            print("\nLogged in Succesfully!\n")
            return (matched_dict["name"], matched_dict["acc_num"], matched_dict["pin"])
            
        else:
            raise ValueError
    
        
                
                
def customer_name() -> str:             # Validates required name format.

    while True:
        name = input("\nName (First,Middle,Last): ")

        if re.search(r"^[A-Z]+ [A-Z]+ [A-Z]+$", name, re.IGNORECASE):
            name = name.upper()
            return name
        
        else:
            print("Incorrect Format❗")
            continue


def customer_contact() -> str:          # Check for correct length(10 digits) and format of the contact number.

    while True:
        contact = input("Contact (10 digits): ")

        if re.search(r"^[0-9]{10}$",contact):
            return contact
        
        else:
            print("Invalid Contact❗")
            continue


def customer_password() -> str:         # Validates user generated password and does not accept it if not formated correctly.
    
    print("\nSet Your Password --> Include Atleast ☑ 4 Characters(atleast ☑ 1 Upper Cased), ☑ 2 Numerics and ☑ 1 Special Character (length: 8 - 14)")
    while True:
        p = input("Password: ").strip()
        password = list(p)
        upp=0
        alpha=0
        num=0
        spe=0
        pun = list(string.punctuation)  # List of Punctuation Marks

            
        if re.search(r"^[a-zA-Z0-9\W]{8,14}$",p) and re.search(r"[\s'']",p) == None:
                
                    for ele in password:
                                if ele.isupper():
                                        upp += 1
                                elif ele.isalpha():
                                        alpha += 1
                                elif ele.isnumeric():
                                        num += 1
                                elif ele in pun:
                                        spe += 1
                    
                    char = upp + alpha

                    if (char >= 4 and upp >= 1) and (num >= 2 and spe >= 1):
                            print("\nPassword Created Succesfully!")
                            return p
                    else:
                            print("\nIncorrect❗")
                            print('❌',end="") if char < 4 else print('✅',end="")
                            print("  4 Characters")
                            print('❌',end="") if upp < 1 else print('✅',end="")
                            print("  1 Upper Cased")
                            print('❌',end="") if num < 2 else print('✅',end="")
                            print("  2 Numerics")
                            print('❌',end="") if spe < 1 else print('✅',end="")
                            print("  1 Special Character")
                            print("\nPlease Set Again")
                            continue
                            
                            
                
        else:
                print("\nInvalid Input❗ --> Length must be between 8 to 14 Characters (Whitespace is Not Allowed)")
                #print("Include Atleast ☑ 4 Characters(atleast ☑ 1 Upper Cased), ☑ 2 Numerics and ☑ 1 Special Character")
                continue
   

def customer_pin() -> str:              # Check for correct length(4-6 digits) and format of the pin generated by user.

    while True:
        pin = input("Set Transaction PIN (length: 4 - 6): ")
        
        if re.search(r"^[0-9]{4,6}$",pin):
            return pin
        
        else:
            print("Invalid❗")
            continue
            

def gen_accnum() -> str:                # Generates unique random acc_num for the new costomer.
    acc_prefix = "GLOBFI"

    for _ in range(6):
        ran = random.randint(0,9)
        acc_prefix += str(ran)

    with open("input_data1.csv") as file:
         reader = csv.DictReader(file)
         data = list(reader)

         for d in data:

              if acc_prefix == d["acc_num"]:

                   #print("Second Call to gen_accnum()")
                   gen_accnum()

              else:
                   #print("Does not Found simillar acc_num")
                   return acc_prefix
 
    


def functionality(name: str, accnum: str, pin: str):              # Provides all the functionalities(deposit,withdrawal,statement) to the user by means of Transactions class.

     select = 0
    
     while select < 5:
        try:
            y = int(input("\nSelect: "))
            os.system("cls")
            
            if y == 1:
                select = 5
                
                
                action1 = Transactions(name,accnum,pin)
                amount = int(input("\nAmount to Deposit: ₹"))
                
                while True:
                    pin_num = input("\nPlease Enter Your Transaction Pin: ")
                    new_balance = action1.deposit(amount,pin_num)
                    
                    if new_balance != False:
                        print()
                        effect6 = [[f"Amount ₹{amount:,} is Suceessfully Deposited"],[f"Account Balance: ₹{new_balance:,}"]]                #effect 6      
                        print(tabulate(effect6,tablefmt="rst"))
                        action1.write_record()
                        break
                    else:
                         continue
                    
                
                return True
                    
                
               
                
            elif y == 2:
                 select = 5
                 
                 i = 0
                 j = 0
                 
                 action2 = Transactions(name,accnum,pin)
                 
                 while i == 0:
                      
                    amount = int(input("\nAmount to Withdraw: ₹"))
                    j = 0

                    while j == 0:
                        pin_num = input("\nPlease Enter Your Transaction Pin: ")
                        new_balance = action2.withdraw(amount,pin_num)
                        
                        if new_balance == 1:
                             continue
                        
                        elif new_balance == 0:
                             j = 1
                            
                        
                        else:
                            print()
                            effect7 = [[f"Amount ₹{amount:,} is Suceessfully Debited"],[f"Account Balance: ₹{new_balance:,}"]]                #effect 7
                            print(tabulate(effect7,tablefmt="rst"))
                            action2.write_record()
                            j = 1
                            i = 1
                             
                             
                        
                 return True
                 
                      
                            
                 
                 
                
            elif y == 3:
                 select = 5
                 
                 action3 = Transactions(name,accnum,pin)
                 action3.Append()
                 action3.statement()

                
                 return True
                 
                 
       
                 
            elif y == 4:
                 select = 5
                 
                 print("\nLogged out\n")
                 
                 
                 return False
            
            
            else:
                print("1Invalid Input!")
                select += 1
                continue
        
        except:

            print("2Invalid Input!")
            select += 1
            continue
                 
    
    
                 
                 
                 
if __name__ == "__main__":
    main()
    
                       

                       

    
            