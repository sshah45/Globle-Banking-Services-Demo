import csv
from datetime import date, datetime
from fpdf import FPDF





class Customer:         # Data-Oriented Class.
    
    def __init__(self, name: str, contact: str, acc_num: str, password: str, pin: str, balance = 1000, record = 0, date = None, time = None):
        
        self.name = name
        self.contact = contact
        self.acc_num = acc_num
        self.password = password
        self.pin = pin
        self.balance = balance
        self.record = record
        self.date = date
        self.time = time
    

    def store_data1(self):    # This method will store all the details of the new account into the csv1.

        with open("input_data1.csv", "a") as data1:
            writer = csv.DictWriter(data1, fieldnames = ["name","contact","acc_num","password","pin"])
            writer.writerow(
                {
                "name":self.name,
                "contact":self.contact,
                "acc_num":self.acc_num,
                "password":self.password,
                "pin":self.pin
                }
                )

        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")
        print(f"\nAccount Created Succesfully! On {self.date} at {self.time}")

        

    
    def store_data2(self):    # This will store 'acc_num' of the new customer along with other important details into the csv2.
        
        with open("input_data2.csv","a") as data2:
            writer = csv.DictWriter(data2,fieldnames = ["date","time","record","acc_num","balance"])
            writer.writerow(
                {
                "date":self.date,
                "time":self.time,
                "record":self.record,
                "acc_num":self.acc_num,
                "balance":self.balance
                }
                )
                
                
            

            
        






class Transactions():       # Method-Oriented Class.
    
    
    
    
    def __init__(self, name: str, acc_num: str, pin: str, date= None, time = None):

        self.name = name
        self.acc_num = acc_num
        self.pin = pin
        self.date = date
        self.time = time
        self.record, self.balance, self.transactions = self.find_acc()
        
        self.closing_balances = []       # Will be the list of a 'Closing Balance' after each transactions.
        self.date_time = []              # Will be the list of a dictionaries having keys ('date' and 'time') of a transactions.
        self.statement_related = []      # Will be the list of a dictionaries having keys ('cd', 'closing', 'date' and 'time') where,
        #                                #'cd' is the amount credited or debited in the user's account.
    
    
    

    
    def __str__(self) -> str:
        return self.balance   

        
    
    
    

    def find_acc(self) -> tuple[int,int,list]:     # This will load all the previous transactions made by the customer in the list(all_transactions) and then sort that list in the decending order.
        
        row = 0     # To know at which row(of the csv) the acc_num matches.

        with open("input_data2.csv") as f1:
            reader = csv.DictReader(f1)
            data = list(reader)
            
            all_transactions = []         # This list will have information of all the previous transactions made by the loged in customer.
            
            for dictionary in data:         
                row += 1
                if self.acc_num == dictionary["acc_num"]:
                    all_transactions.append(data[row-1])
                    continue

                else:
                    continue

            # Now 'all_transactions' list will be sorted in the decending order where the most recent transaction made by a user will apperar at '0'th index.
            
            all_transactions = sorted(all_transactions, key= lambda all_transactions: int(all_transactions["record"]), reverse=True)
            mostrecent_transaction = all_transactions[0]

            return (int(mostrecent_transaction["record"]), int(mostrecent_transaction["balance"]), all_transactions)




    def write_record(self):     # This method will write each New transaction details into the csv2.


        with open("input_data2.csv","a") as f2:
            writer = csv.DictWriter(f2,fieldnames = ["date","time","record","acc_num","balance"])
            writer.writerow(
                {
                "date":self.date,
                "time":self.time,
                "record":self.record,
                "acc_num":self.acc_num,
                "balance":self.balance
                }
                )




    def deposit(self,n,p):      # To Deposit money in an account.

            if p == self.pin:
                self.record  += 1
                self.balance += n
                self.date = date.today()
                self.time = datetime.now().strftime("%H:%M:%S")
                return self.balance
                
               
            else:
                print("\nIncorrect Pin!, Please Enter Again")
                return False


                
                
    def withdraw(self,n,p):     # To Withdraw money from an account.

                if p == self.pin:
                    
                    if n <= self.balance:
                        self.record += 1
                        self.balance -= n
                        self.date = date.today()
                        self.time = datetime.now().strftime("%H:%M:%S")
                        return self.balance
                    
                    else:
                       print("\nInsufficient Balance In Your Account!") 
                       return 0
                else:
                    print("\nIncorrect Pin!, Please Enter Again")
                    return 1
                   
                
                   
           

                    

    def Append(self):   # This method will load all the empty lists in the 'init'.

        for x in self.transactions:
            self.closing_balances.append(x["balance"])
        #print(self.closing_balances)


        for y in self.transactions:
            k = {"date": y["date"], "time": y["time"]}
            self.date_time.append(k)
        #print(self.date_time)
    
    
    
    
    def statement(self):    # This method is resposible for creating all the necessary information regarding the statement.
       

       for i in range(0 , len(self.closing_balances)-1):  # e.g If the length of self.closing_balances is 5 then we have only 
        #4 pairs available for subraction below.
           
           # Here I am subtracting previous account balance from the closing balance, Hence if x>0 then that amount is credited
           # else if x<0 then that amount is debited from the account.
           
           x = int(self.closing_balances[i]) - int(self.closing_balances[i+1])
           y = {"cd": x , "closing": int(self.closing_balances[i]), "date": None, "time": None}
           self.statement_related.append(y)


       for j in range(len(self.statement_related)):
           
           d1 = self.statement_related[j]
           d2 = self.date_time[j]
           d1["date"] = d2["date"]
           d1["time"] = d2["time"]
          
       #print(self.statement_related)

       
       self.form_pdf()
  

    
           
    def form_pdf(self):     # Resposible for creating a pdf.
    
        n = self.name
        a = self.acc_num
        d = date.today()
        records = self.statement_related[:20]
        
        
    
    
        class PDF(FPDF):    # Sub-class of FPDF.

            
            def header(self):
                
                self.set_font("Times","", 12)
                self.set_y(10)
                self.cell(48)
                self.cell(None,None,"GLOBAL BANK ACCOUNT STATEMENT", align = "C")
                self.ln(15)
                self.set_font("Times","", 10)
                self.cell(5)
                self.cell(None,None,f"Account Name :  {n}",align = "L" )
                self.ln(5)
                self.cell(5)
                self.cell(None,None,f"Account Number :  {a}", align = "L")
                self.ln(5)
                self.cell(5)
                self.cell(None,None,f"Date :  {d}", align = "L")
                self.ln(10)
                self.cell(5)
                self.cell(None,None,f"Account Summary", align = "L")
                self.ln(5)
                self.cell(5)
                self.cell(None,None,f"Past Transactions(Max 20)")
                self.ln(10)
                
                self.form_table()


            
            def form_table(self):

                    with self.table() as table:
                        row = table.row()
                        row.cell("Transaction(Date&Time)")
                        row.cell("Debit (in ruppes)")
                        row.cell("Credit (in ruppes)")
                        row.cell("Closing Balance (in ruppes)")


                        for rec in records:
                            if rec['cd'] > 0:
                                
                                row = table.row()
                                row.cell(f"On {rec['date']} At {rec['time']}")
                                row.cell("")
                                row.cell(f"{rec['cd']:,}")
                                row.cell(f"{rec['closing']:,}")
                                continue
                            
                            else:
                                
                                row = table.row()
                                row.cell(f"On {rec['date']} At {rec['time']}")
                                row.cell(f"{-rec['cd']:,}")
                                row.cell("")
                                row.cell(f"{rec['closing']:,}")
                                continue



        pdf = PDF()
        pdf.add_page()    #According to the documentation of the fpdf2 library, this line automatically calls 'header' of the PDF class.
        pdf.output("Account_Statement.pdf")   
    
       
    


