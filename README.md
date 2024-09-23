# Global Banking Services
####
### Description :
This progarm provides demo banking services.In this program user can create a new bank account by providing some personal details and then the system will generate unique random account number for that new account.After having an account, customer can login to that account by providing the account number and the password that customer has created for his/her account.New bank account's initial balance is 1000 Rs.After login to the account, customer can deposit money to his/her account and also withdraw money from that account.Customer can also generate an account statement(pdf) of upto 20 previous transactions.

### Details of the design of the Software/Program :
There are Four files in this project: 
* (1) Data1.csv
* (2) Data2.csv
* (3) customer_classes.py
* (4) project.py

**(1) Data1.csv** : This csv file contains all the data of a new customer.

Data : Name, Contact, Acc_num, Password, and the Transaction pin number of all the customers.



**(2) Data2.csv** : This csv file contains Transaction date,Transaction time, Record, Acc_num and Balance of customer's account.




**(3) customer_class.py** : This file contains two classes.

* Customer
* Transactions

**Customer class** : This is the data oriented class of this program. This class helps to store personal details of a new customer inside the Data1.csv file using 'store_data1' method of this class.Also this class has another instance method called 'store_data2', which stores new customer's account balance and other important data related to the customer inside the Data2.csv file.

**Transactions class** : This is the method oriented class of this program. This class contains deposit, withdraw, statement and the pdf generation methods. All the instance level methods of this class play an important role in this program. Perticularly 'find_acc' method of this class is very crucial and is called from an init method whenever the instance of this class is created.'find_acc' method basically returns transaction record, latest/closing account balance of a loged in account and the list of all transactions of that account. There is an algorithm to sort the list of all transactions in a way that most recent transaction appers first and therefore all transactions are organized in the recent to oldest order.After using either deposit or withdraw method, immediately 'write_record' method of this class is used and it stores the updated record, date and the time of the transaction in to the Data2.csv file.




**(4) project.py** : This file contanins total of eight functions including the main function.This file is responsible for creating a new bank account, login to the existing bank account and for using all the functionalities related to the customer's bank account by using 'Transactions class'.

**Functions** :
* main
* login
* customer_name
* customer_contact
* customer_password
* customer_pin
* gen_accnum
* functionality

**main** : The main function is responsible for calling all the functions of this file and also responsible for creating many side effects for this program.

**login** :The login function search through the Data1.csv file where all the customers data is stored and then try to match the account number and the password of the customer who try to login to his/her account.If user provides correct account number and the password of his/her account, then login returns customer name , account number and the transaction pin number of that account.But if customer fails to enter the correct details of his/her account then login raises ValueError and user will be prompt again for the account number and the password.

**customer_name** : This function validates whether user has given his/her name according to the required format.

**customer_contact** : This function validates the contact number given by the user.

**customer_password** : This function validates the password that user try to set up for his/her new bank account and accept if formated correctly.

**customer_pin** : This function validates the transaction pin that user try to set up.

**gen_accnum** : This function generates unique random bank account number for the new customer.

**functionality** : This function allow user to deposit and withdraw money form an account and also allow to create an account statement all by means of 'Transactions class'.




















