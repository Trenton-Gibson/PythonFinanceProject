# Trenton Gibson
# Created: 04/21/23
# FinanceProjectGUI_V2.py

#Explanation of project:
#This a personal finance manager that can access my SQLite Database
#and can handle my accounts and transactions.

# import tkinter GUI materials
import tkinter as tk
from tkinter import *
from tkinter import ttk
import FinanceProjectDatabaseAccess
import tkinter.messagebox
# Create Finance GUI class
class FinanceGUI:
	def __init__(self):
		# Create Personal Finance Manager window
		self.PersonalFinanceManager = tk.Tk()
		self.PersonalFinanceManager.title('Personal Finance Manager')
		self.PersonalFinanceManager.attributes('-fullscreen', True)
		
		
		# Create Frames for Personal Finance Manager window
		# Create Parent Frames
		self.TopFrame=Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		self.TopMidFrame = Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		self.TrueMiddleFrame= Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		self.BottomMidFrame=Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		self.BottomFrame=Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		# Create Child frames
		##Child frames of top frame
		self.TransferMoneyFrame=Frame(self.TopFrame,relief=SUNKEN,borderwidth=10)
		self.AddDeleteAccountFrame=Frame(self.TopFrame,relief=SUNKEN,borderwidth=10)
		self.TransferMoneyLabelsFrame=Frame(self.TopFrame,relief=SUNKEN,borderwidth=10)
		##Child frames of top middle frame
		self.TransactionHistoryFrame = Frame(self.TopMidFrame, relief=SUNKEN, borderwidth=10)
		self.HandleAccountFrame = Frame(self.TopMidFrame, relief=SUNKEN, borderwidth=10)
		### Child Frame of Handle account frame
		self.EnterDateFrame=Frame(self.HandleAccountFrame)
		##Child Frames of true middle frame
		self.AccountTreeviewFrame = Frame(self.TrueMiddleFrame, relief=SUNKEN, borderwidth=10)
		self.TransactionTreeviewFrame = Frame(self.TrueMiddleFrame, relief=SUNKEN, borderwidth=10)
		##Child Frame of Bottom middle frame
		self.DeleteAccountLabelFrame=Frame(self.BottomMidFrame,relief=SUNKEN,borderwidth=10)
		##Child Frame of Bottom frame
		self.ButtonsFrame = Frame(self.BottomFrame, relief=RAISED, borderwidth=10)
		#pack parent frames
		self.TopFrame.pack()
		self.TopMidFrame.pack()
		self.TrueMiddleFrame.pack()
		self.BottomMidFrame.pack()
		self.BottomFrame.pack()
		#pack child frames
		##Frames of Top Frame
		self.AddDeleteAccountFrame.pack(side='left')
		self.TransferMoneyLabelsFrame.pack(side='right')
		self.TransferMoneyFrame.pack(side='right')
		##Frames of Top Middle Frame
		self.HandleAccountFrame.pack(side='left')
		self.TransactionHistoryFrame.pack(side='left')
		##Frames of True Middle Frame
		self.AccountTreeviewFrame.pack(side='left')
		self.TransactionTreeviewFrame.pack(side='left')
		##Frame of Bottom Middle frame
		self.DeleteAccountLabelFrame.pack()
		##Frame of Bottom Frame
		self.ButtonsFrame.pack(side='bottom')
		
		
		# Create Widgets for Personal Finance Manager Window
		#Create widgets for the Top Frame
		##create/delete account frame widgets
		self.CreateAccountLabel = tk.Label(self.AddDeleteAccountFrame,text='Fill the two entries below for a new account then click "Add Account"',
										   font=('Times New Roman', 11))
		self.NameAccountLabel = tk.Label(self.AddDeleteAccountFrame, text='Name your account:',font=('Times New Roman', 11))
		self.NameAccountEntry = tk.Entry(self.AddDeleteAccountFrame, width=50, font=('Times New Roman', 11))
		self.IntialBalanceLabel = tk.Label(self.AddDeleteAccountFrame,text='State the intial balance(only use numbers and decimals):',
										   font=('Times New Roman', 11))
		self.IntialBalanceEntry = tk.Entry(self.AddDeleteAccountFrame, width=50, font=('Times New Roman', 11))
		## Pack the delete/add account frame widgets
		self.CreateAccountLabel.pack(padx=10)
		self.NameAccountLabel.pack(padx=10)
		self.NameAccountEntry.pack(padx=10)
		self.IntialBalanceLabel.pack(padx=10)
		self.IntialBalanceEntry.pack(padx=10)
		##Create Transfer money frame widgets
		self.GivingAccountButton = tk.Button(self.TransferMoneyFrame, text='Set Giving Account'
											 , font=('Times New Roman', 11), command=self.GetGivingAccount)
		self.RecipientAccountButton = tk.Button(self.TransferMoneyFrame, text='Set Recipient Account'
												, font=('Times New Roman', 11), command=self.GetRecipientAccount)
		self.AmountTransferredLabel = tk.Label(self.TransferMoneyFrame,
											   text='Transfer Money Between Accounts:\n1.Set the giving(account that will be giving up money) and recipient account(account that will receive money)\n by first clicking the account in the left table and then clicking the corresponding button for each.'
													'\n2. Put the amount the recipient account will receive(only use numbers and decimals). Finally, click "Confirm Transfer."',
											   font=('Times New Roman', 11))
		self.AmountTransferredEntry = tk.Entry(self.TransferMoneyFrame, width=50, font=('Times New Roman', 11))
		## Pack Transfer money frame widgets
		self.AmountTransferredLabel.pack()
		self.AmountTransferredEntry.pack()
		self.GivingAccountButton.pack()
		self.RecipientAccountButton.pack()
		## Create Transfer money label frame Widgets
		self.GiverAccountLabel = tk.Label(self.TransferMoneyLabelsFrame, text='Giving Account:',
										  font=('Times New Roman', 11), foreground='black', background='white')
		self.RecipientAccountLabel = tk.Label(self.TransferMoneyLabelsFrame, text='Recipient Account:',
											  font=('Times New Roman', 11), foreground='black', background='white')
		##Pack Transer money label frame widgets
		self.GiverAccountLabel.pack()
		self.RecipientAccountLabel.pack()
		
		#Create Top Middle Frame Widgets
		## Create transaction history frame widgets
		self.AccountHistoryLabel = tk.Label(self.TransactionHistoryFrame,
											text="Account's Transaction history: enter the name of the account below and click the Transaction History button."
												 "\n To restore the table, type all and click the Transaction History button.",
											font=('Times New Roman', 11))
		##Pack Transaction history frame widgets
		self.AccountHistoryLabel.pack()
		## Create handle account frame widgets
		self.TransactionLabel = tk.Label(self.HandleAccountFrame,
										 text='To enter a transaction, click the account row in the left table where the transacation took place then put the transaction amount here.'
											  '\nOnly enter numbers and decimals here(negative amount for costs and postive for income):',
										 font=('Times New Roman', 11))
		self.TransactionEntry = tk.Entry(self.HandleAccountFrame, width=50, font=('Times New Roman', 11))
		self.DateofTransLabel = tk.Label(self.HandleAccountFrame, text='Next, enter the date of the transaction. All answers only use numbers.',
										 font=('Times New Roman', 11))
		self.MonthofTransEntry = tk.Entry(self.EnterDateFrame, width=10, font=('Times New Roman', 11))
		self.DateDashLabel1= tk.Label(self.EnterDateFrame,text='-')
		self.DayofTransEntry = tk.Entry(self.EnterDateFrame, width=10, font=('Times New Roman', 11))
		self.DateDashLabel2 = tk.Label(self.EnterDateFrame, text='-')
		self.YearofTransEntry = tk.Entry(self.EnterDateFrame, width=10, font=('Times New Roman', 11))
		self.TransactionTypeLabel = tk.Label(self.HandleAccountFrame,
											 text=' Third, put in what type of transaction occured and then click Confirm Transaction button:',
											 font=('Times New Roman', 11))
		self.TransactionTypeEntry = tk.Entry(self.HandleAccountFrame, width=50, font=('Times New Roman', 11))
		## Pack Handle Account Frame Widgets
		self.TransactionLabel.pack()
		self.TransactionEntry.pack()
		self.DateofTransLabel.pack()
		self.MonthofTransEntry.pack(side= LEFT)
		self.DateDashLabel1.pack(side= LEFT)
		self.DayofTransEntry.pack(side=  LEFT)
		self.DateDashLabel2.pack(side= LEFT)
		self.YearofTransEntry.pack(side= LEFT)
		self.EnterDateFrame.pack()
		self.TransactionTypeLabel.pack()
		self.TransactionTypeEntry.pack()
		
		#Create widgets for the True Middle Frame
		# Create Account Treeview
		##Create Account Treeview ScrollBar
		self.Accounts_yscroll = Scrollbar(self.AccountTreeviewFrame)
		self.Accounts_yscroll.pack(side=LEFT, fill=Y)
		##Create actual Account Treeview
		self.AccountsInfoTreeview = ttk.Treeview(self.AccountTreeviewFrame, height=10,
												 columns=(
												 'column1', 'column2', 'column3', 'column4', 'column5'),
												 show='headings', yscrollcommand=self.Accounts_yscroll)
		##Define and create the columns for the Account Treeview
		self.AccountsInfoTreeview['columns'] = (
		'Account Type', 'Balance','Transaction Type','Transaction Amount', 'Date of Transaction')
		self.AccountsInfoTreeview.column('Account Type', width=140)
		self.AccountsInfoTreeview.heading("#1", text="Account Type")
		self.AccountsInfoTreeview.column('Balance', width=140)
		self.AccountsInfoTreeview.heading("#2", text="Balance")
		self.AccountsInfoTreeview.column('Transaction Type', width=140)
		self.AccountsInfoTreeview.heading("#3", text="Transaction Type")
		self.AccountsInfoTreeview.column('Transaction Amount', width=140)
		self.AccountsInfoTreeview.heading("#4", text="Transaction Amount")
		self.AccountsInfoTreeview.column('Date of Transaction', width=140)
		self.AccountsInfoTreeview.heading("#5", text="Date of Transaction")
		## Pack and configure the scrollbar for the Accounts Treeview
		self.AccountsInfoTreeview.pack(side='left')
		self.Accounts_yscroll.config(command=self.AccountsInfoTreeview.yview)
		## Populate treeview with data
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccountsInfoTreeview.insert("", tk.END, values=row)
		
		# Create Transaction Info treeview
		##Create Scrollbars for Transaction Treeview
		self.Transaction_yscroll = Scrollbar(self.TransactionTreeviewFrame)
		self.Transaction_yscroll.pack(side=RIGHT, fill=Y)
		##Create the actual Transaction Treeview
		self.TransHisTransactionInfo = ttk.Treeview(self.TransactionTreeviewFrame, height=10,
													columns=(
													'column1', 'column2', 'column3', 'column4', 'column5', 'column6',),
													show='headings', yscrollcommand=self.Transaction_yscroll.set)
		##Define and create the columns for the Transaction Treeview
		self.TransHisTransactionInfo['columns'] = ( 'Account Type', 'Previous Balance', 'Current Balance',
												   'Transaction Type', 'Transaction Amount', 'Transaction Date')
		self.TransHisTransactionInfo.column('Account Type', width=110)
		self.TransHisTransactionInfo.heading("#1", text="Account Type")
		self.TransHisTransactionInfo.column('Previous Balance', width=115)
		self.TransHisTransactionInfo.heading("#2", text="Previous Balance")
		self.TransHisTransactionInfo.column('Current Balance', width=105)
		self.TransHisTransactionInfo.heading("#3", text="Current Balance")
		self.TransHisTransactionInfo.column('Transaction Type', width=120)
		self.TransHisTransactionInfo.heading("#4", text="Transaction Type")
		self.TransHisTransactionInfo.column('Transaction Amount', width=130)
		self.TransHisTransactionInfo.heading("#5", text="Transaction Amount")
		self.TransHisTransactionInfo.column('Transaction Date', width=120)
		self.TransHisTransactionInfo.heading("#6", text="Transaction Date")
		##Pack the Transaction Treeview
		self.TransHisTransactionInfo.pack(side='left')
		##Configure the Transaction Treeview Scrollbar
		self.Transaction_yscroll.config(command=self.TransHisTransactionInfo.yview)
		##Populate the Transaction Treeview with data
		self.StartAccountHistory = ''
		rows = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for row in rows:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
		
		# Change the style of the Treeviews
		style = ttk.Style()
		style.configure("Treeview.Heading", fieldbackground='#9613bb', font=('Times New Roman', 11))
		style.configure("Treeview", font=('Times New Roman', 11))
		style.configure("Treeview", foreground='yellow', background='#9613bb')
		
		#Create widget for Bottom Middle Frame
		## create delete account label frame widget
		self.DeleteAccountLabel = Label(self.DeleteAccountLabelFrame,
										text='To Delete Account, Click the account row from the left table you want to delete then click Delete Account Button.'
										, font=('Times New Roman', 11))
		## Pack Delete Account label Frame
		self.DeleteAccountLabel.pack()
		
		#Create Widgets for Bottom Frame
		## Create buttons for button frame
		self.AccOverQuitButton = tk.Button(self.ButtonsFrame, text='Quit', command=self.PersonalFinanceManager.destroy,font=('Times New Roman',11))
		self.ConfirmTransactionButton = tk.Button(self.ButtonsFrame, text='Confirm Transaction',
												  command=self.TransDataAndTransCommit,font=('Times New Roman',11))
		self.AccountHistoryButton = tk.Button(self.ButtonsFrame, text="Transaction History",
											  command=self.AccountHistory,font=('Times New Roman',11))
		self.AddAccountButton = tk.Button(self.ButtonsFrame, text='Add Account', command=self.AddAccount,font=('Times New Roman',11))
		self.DeleteAccountButton = tk.Button(self.ButtonsFrame, text='Delete Account', command=self.DeleteAccount,font=('Times New Roman',11))
		self.ConfirmTransferButton = tk.Button(self.ButtonsFrame, text='Confirm Transfer',
											   command=self.TransferringMoney,font=('Times New Roman',11))
		self.TransHisTreeResetButton = tk.Button(self.ButtonsFrame, text='Reset Transaction Table',
											   command=self.ResetTransHisTree, font=('Times New Roman', 11))
		#Pack Widgets for the button frame
		self.ConfirmTransferButton.pack(side='left', padx=50)
		self.AddAccountButton.pack(side='left', padx=50)
		self.DeleteAccountButton.pack(side='left', padx=50)
		self.ConfirmTransactionButton.pack(side='left',padx=50)
		self.AccountHistoryButton.pack(side='left', padx=50)
		self.TransHisTreeResetButton.pack(side='left', padx=50)
		self.AccOverQuitButton.pack(side='left',padx=50)
		
		
		# Start the mainloop
		tk.mainloop()
		
		
	# Additional Methods
	#Handles Typical transactions.Is called by Handle Account Frame Widgets.
	def TransDataAndTransCommit(self):
		try:
			# Get data for Transaction
			self.selected = self.AccountsInfoTreeview.focus()
			self.Account = self.AccountsInfoTreeview.item(self.selected, 'values')
			self.Month=self.MonthofTransEntry.get()
			self.Day = self.DayofTransEntry.get()
			self.Year=self.YearofTransEntry.get()
			self.TransactionDate=self.Month+'-'+self.Day+'-'+self.Year
			self.TransactionAmount = self.TransactionEntry.get()
			self.TransactionType = self.TransactionTypeEntry.get()
			#if any of the date entries can't be converted to integers then the exception handling will kick in
			self.MonthTest= int(self.Month)
			self.DayTest= int(self.Day)
			self.YearTest=int(self.Year)
			#If any of the entries are unpopulated or aren't within the proper date range, it sends an error message and the core code isn't executed
			if self.TransactionAmount =='' or self.TransactionType == '' or self.Month=='' or self.Year==''or self.Day==''\
			or self. MonthTest > 12 or self. MonthTest<1 or self.DayTest<0 or self.DayTest>31 or self.YearTest < 2023  :
				# Create an error message variable
				self.ErrorMessage = 'Error! Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
			# The core code
			else:
				#Calls the Handle Account Function from the other module to interact with the database
				FinanceProjectDatabaseAccess.HandleAccount(self.Account, self.TransactionDate, self.TransactionAmount, self.TransactionType)
				# Repopulate treeviews with data after the changes are made to represent them
				self.RepopulateAccountsTreeview()
				self.RepopulateTransactionsTreeview()
				self.TransactionEntry.delete(0, END)
				self.TransactionTypeEntry.delete(0, END)
				self.YearofTransEntry.delete(0,END)
				self.DayofTransEntry.delete(0,END)
				self.MonthofTransEntry.delete(0,END)
		except:
			#Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			#Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
			
			
	#Creates a new account
	def AddAccount(self):
		try:
			#get data from the entries to create a new account
			self.AccountName = self.NameAccountEntry.get()
			self.IntialBalance = self.IntialBalanceEntry.get()
			self.IntialBalance= float(self.IntialBalance)
			# If any of the entries are unpopulated, it sends an error message and the core code isn't executed
			if self.AccountName == '' or self.IntialBalance == '':
				# Create an error message variable
				self.ErrorMessage = 'Error! Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
			#The core code
			else:
				#Add Account Function is called from the other module to interact with the database
				FinanceProjectDatabaseAccess.AddAccount(self.IntialBalance, self.AccountName)
				# Repopulate treeviews with data
				self.RepopulateAccountsTreeview()
				self.RepopulateTransactionsTreeview()
				self.NameAccountEntry.delete(0,END)
				self.IntialBalanceEntry.delete(0,END)
		except:
			# Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	
			
	#Deletes an account if called
	def DeleteAccount(self):
		try:
			#get data for which account to delete
			self.selected = self.AccountsInfoTreeview.focus()
			self.AccountToDelete= self.AccountsInfoTreeview.item(self.selected, 'values')
			#set up accumulator to end the loop when the correct tuple data is place
			count=0
			#processe tuple data into a usable string form
			for item in self.AccountToDelete:
				count+=1
				String = str(item)
				String = String.lstrip('(')
				String = String.rstrip(')')
				String = String.rstrip(',')
				self.AccountToDelete = String
				#loop ends when the second data value gets processed
				if count>1:
					break
			#Calls Delete account function from the other module to interact with the database
			FinanceProjectDatabaseAccess.DeleteAccount(self.AccountToDelete)
			# Repopulate treeviews with data
			self.RepopulateAccountsTreeview()
			self.RepopulateTransactionsTreeview()
		except:
			# Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
			
	
	#Gets the account transaction history of a specific account
	def AccountHistory(self):
		try:
			#get the selected account name from the accounts treeview
			self.selected = self.AccountsInfoTreeview.focus()
			self.AccountHistory = self.AccountsInfoTreeview.item(self.selected, 'values')
			#isolate the account name from the rest of the data
			# start accumulator to act as a trigger to end the loop early so the needed value can be obtained
			count = 0
			# process tuple data into string data
			for item in self.AccountHistory:
				count += 1
				String = str(item)
				self.AccountHistory = String
				# end the loop when the correct value is in play
				if count == 1:
					break
			#if there is no account clicked the table is restored
			if self.AccountHistory!='':
				# call the Account transaction History function to retrieve data from the database to view
				self.TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(
					self.AccountHistory)
				# clear the data out and replace it with the requested data
				for item in self.TransHisTransactionInfo.get_children():
					self.TransHisTransactionInfo.delete(item)
				for row in self.TransactionAccountHistory:
					self.TransHisTransactionInfo.insert("", tk.END, values=row)
			else:
				# Create an error message variable
				self.ErrorMessage = 'Error! Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
		except:
			# Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
			
			
	#Handles transferring money between two accounts
	def TransferringMoney(self):
		try:
			#get accounts transferring and amount of money being transferred
			self.TransferredMoney = self.AmountTransferredEntry.get()
			self.TransMonGivingAccount = self.GivingAccount
			self.TransMonRecipientAccount = self.RecipientAccount
			#if any of the values are empty then an error message will pop up and the core code will not execute
			if self.TransferredMoney == '' or self.TransMonGivingAccount == '' \
			or self.TransMonRecipientAccount=='' or self.TransferredMoney==self.TransferredMoney.isalpha():
				# Create an error message variable
				self.ErrorMessage = 'Error! Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
			else:
				#Calls Account transfer function which will handle the database interactions for transferring money
				FinanceProjectDatabaseAccess.AccountTransfer(self.TransferredMoney, self.TransMonGivingAccount, self.TransMonRecipientAccount)
				# Repopulate treeviews with data
				self.RepopulateAccountsTreeview()
				self.RepopulateTransactionsTreeview()
				#reformat labels back to original state
				self.GiverAccountLabel.config(text='Giving Account:',font=('Times New Roman', 11), foreground='black', background='white')
				self.RecipientAccountLabel.config(text='Recipient Account:',font=('Times New Roman', 11), foreground='black', background='white')
				#clear amount transferred entry
				self.AmountTransferredEntry.delete(0,END)
		except:
			# Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	
	
	#gets the giving account for transferring money
	def GetGivingAccount(self):
		try:
			#obtains the giving account
			self.selected = self.AccountsInfoTreeview.focus()
			self.GivingAccount = self.AccountsInfoTreeview.item(self.selected, 'values')
			#start accumulator to act as a trigger to end the loop early so the needed value can be obtained
			count = 0
			#process tuple data into string data
			for item in self.GivingAccount:
				count += 1
				String = str(item)
				self.GivingAccount = String
				#end the loop when the correct value is in play
				if count == 1:
					break
			#if the Giving Account variable isn't empty, make the Giving account label change text and coloring
			if self.GivingAccount!= '':
				self.GiverAccountLabel.config(text='Giving Account:'+self.GivingAccount,font=('Times New Roman',11), foreground='yellow', background='#9613bb')
			# return the variable for transferring the money
			return self.GivingAccount
		except:
			# Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
			
			
	# gets the recipient account for transferring money
	def GetRecipientAccount(self):
		try:
			#obtain the recipient account from the accounts treeview and put in the recipient account variable
			self.selected = self.AccountsInfoTreeview.focus()
			self.RecipientAccount = self.AccountsInfoTreeview.item(self.selected, 'values')
			# start accumulator to act as a trigger to end the loop early so the needed value can be obtained
			count = 0
			# process tuple data into string data
			for item in self.RecipientAccount:
				count += 1
				String = str(item)
				self.RecipientAccount = String
				# end the loop when the correct value is in play
				if count == 1:
					break
			#if the Recipient Account variable isn't empty, make the Recipient account label change text and coloring
			if self.RecipientAccount!= '':
				self.RecipientAccountLabel.config(text='Recipient Account:' + self.RecipientAccount,font=('Times New Roman',11), foreground='yellow', background='#9613bb')
			# return the variable for transferring the money
			return self.RecipientAccount
		except:
			# Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
			
			
	#Repopulates the accounts treeview with data
	def RepopulateAccountsTreeview(self):
		#Clears the old treeview data
		for item in self.AccountsInfoTreeview.get_children():
			self.AccountsInfoTreeview.delete(item)
		#obtain data for accounts with transactions recorded and add the data to the treeview
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccountsInfoTreeview.insert("", tk.END, values=row)
		# obtain data for accounts without transactions recorded and add the data to the treeview
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccountsInfoTreeview.insert("", tk.END, values=row)
			
			
	#Repopulate the transaction treeview with data
	def RepopulateTransactionsTreeview(self):
		#get the transaction history for all the accounts
		TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		#clear the transaction treeview
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		#Insert new transaction treeview data into the transaction treeview
		for row in TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
	
	def ResetTransHisTree(self):
		#make account history an empty string to reset the treeview
		self.AccountHistory=''
		#get the transaction info from the other module
		self.TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(
			self.AccountHistory)
		# clear the data out and replace it with the requested data
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in self.TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
			
# Call the Finance GUI Class
if __name__ == '__main__':
	FinanceGUI()