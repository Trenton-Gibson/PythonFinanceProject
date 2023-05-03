# Trenton Gibson
# Created: 04/21/23
# FinanceProjectGUI.py

# import tkinter GUI materials
import tkinter as tk
from tkinter import *
from tkinter import ttk
import FinanceProjectDatabaseAccess

# Create Finance GUI class
class FinanceGUI:
	def __init__(self):
		# Create Account Overview window
		self.AccountOverview = tk.Tk()
		self.AccountOverview.title('Account Overview')
		# Create Frames and  Widgets for Account Overview window
		# Frames
		self.AccOverTopFrame = Frame(self.AccountOverview)
		self.AccOverBotFrame = Frame(self.AccountOverview)
		self.AccOverTopFrame.pack()
		self.AccOverBotFrame.pack()
		# Widgets
		# Create Account Treeview
		self.AccOverAccountsInfoTreeview = ttk.Treeview(self.AccOverTopFrame,
		columns=('column1','column2','column3','column4','column5','column6'),show='headings')
		self.AccOverAccountsInfoTreeview['columns'] = \
			('AccountID','Account Type', 'Balance', 'TransactionID','Money Transferred','Date of Transaction')
		self.AccOverAccountsInfoTreeview.column('AccountID', width=100)
		self.AccOverAccountsInfoTreeview.heading("#1", text="AccountID")
		self.AccOverAccountsInfoTreeview.column('Account Type', width=100)
		self.AccOverAccountsInfoTreeview.heading("#2", text="Account Type")
		self.AccOverAccountsInfoTreeview.column('Balance', width=100)
		self.AccOverAccountsInfoTreeview.heading("#3", text="Balance")
		self.AccOverAccountsInfoTreeview.column('TransactionID', width=100)
		self.AccOverAccountsInfoTreeview.heading("#4", text="TransactionID")
		self.AccOverAccountsInfoTreeview.pack()
		self.AccOverAccountsInfoTreeview.column('Money Transferred', width=150)
		self.AccOverAccountsInfoTreeview.heading("#5", text="Money Transferred")
		self.AccOverAccountsInfoTreeview.pack()
		self.AccOverAccountsInfoTreeview.column('Date of Transaction', width=150)
		self.AccOverAccountsInfoTreeview.heading("#6", text="Date of Transaction")
		self.AccOverAccountsInfoTreeview.pack()
		#Populate treeview with data
		rows=FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		# Buttons
		self.AccOverHandleAccountButton = tk.Button(self.AccOverBotFrame, text='Handle Account',
													command=self.HandleAccountWindow)
		self.AccOverAddDeleteButton = tk.Button(self.AccOverBotFrame, text='Add/Delete Account',
												command=self.AddDeleteWindow)
		self.AccOverTransferMoneyButton = tk.Button(self.AccOverBotFrame, text='Transfer Money',
													command=self.TransferMoneyWindow)
		self.AccOverTransactionHistoryButton=tk.Button(self.AccOverBotFrame,text='Transaction History',command=self.TransactionHistoryWindow)
		self.AccOverQuitButton = tk.Button(self.AccOverBotFrame, text='Quit', command=self.AccountOverview.destroy)
		self.AccOverHandleAccountButton.pack(side='left', pady=10)
		self.AccOverAddDeleteButton.pack(side='left', pady=10)
		self.AccOverTransferMoneyButton.pack(side='left', pady=10)
		self.AccOverTransactionHistoryButton.pack(side='left', pady=10)
		self.AccOverQuitButton.pack(side='left', pady=10)
		# Start the mainloop
		tk.mainloop()
	
	# Additional window methods
	def AddDeleteWindow(self):
		# Remove Account Overview Window
		self.AccountOverview.destroy()
		# Create Add/Delete Account Window
		self.AddDeleteAccount = tk.Tk()
		self.AddDeleteAccount.title('Add/Delete Account')
		# create and pack frames
		self.AddDelTopFrame = tk.Frame(self.AddDeleteAccount)
		self.AddDelMidFrame = tk.Frame(self.AddDeleteAccount)
		self.AddDelBotFrame = tk.Frame(self.AddDeleteAccount)
		self.AddDelTopFrame.pack()
		self.AddDelMidFrame.pack()
		self.AddDelBotFrame.pack()
		# Create Widgets
		# Widgets for top frame
		self.CreateAccountLabel = tk.Label(self.AddDelTopFrame,
										   text='Fill the two entries below for a new account then click "Create Account"')
		self.NameAccountLabel = tk.Label(self.AddDelTopFrame, text='Name your account:')
		self.NameAccountEntry = tk.Entry(self.AddDelTopFrame, width=50)
		self.IntialBalanceLabel = tk.Label(self.AddDelTopFrame, text='State the intial balance:')
		self.IntialBalanceEntry = tk.Entry(self.AddDelTopFrame, width=50)
		# Pack top frame widgets
		self.CreateAccountLabel.pack()
		self.NameAccountLabel.pack()
		self.NameAccountEntry.pack()
		self.IntialBalanceLabel.pack()
		self.IntialBalanceEntry.pack()
		# Widgets for middle frame
		self.ExistingAccountsLabel = tk.Label(self.AddDelMidFrame, text='Click Account you wish to delete\n then click Delete Account Button.')
		self.ExistingAccountsListbox = tk.Listbox(self.AddDelMidFrame,selectmode=tk.SINGLE)
		self.AccountNames=FinanceProjectDatabaseAccess.AccountName()
		print(self.AccountNames)
		for row in self.AccountNames:
			self.ExistingAccountsListbox.insert(tk.END,row)
		# pack middle frame widgets
		self.ExistingAccountsLabel.pack()
		self.ExistingAccountsListbox.pack()
		# Widgets for bottom frame
		self.AddAccountButton = tk.Button(self.AddDelBotFrame, text='Add Account',command=self.AddAccount)
		self.DeleteAccountButton = tk.Button(self.AddDelBotFrame, text='Delete Account',command=self.DeleteAccount)
		self.AddDelReturnParentWindowButton = tk.Button(self.AddDelBotFrame, text='Return to Parent Window',
														command=self.ReturnParentWindowAddDel)
		self.AddDelQuitButton = tk.Button(self.AddDelBotFrame, text='Quit Program',
										  command=self.AddDeleteAccount.destroy)
		# pack the bottom frame widgets
		self.AddAccountButton.pack(side='left')
		self.DeleteAccountButton.pack(side='left')
		self.AddDelReturnParentWindowButton.pack(side='left')
		self.AddDelQuitButton.pack(side='left')
	
	def HandleAccountWindow(self):
		# remove account overview window
		self.AccountOverview.destroy()
		# Create Handle account window
		self.HandleAccount = tk.Tk()
		self.HandleAccount.title('Handle Account')
		# Create frames
		self.HandAccTopFrame = tk.Frame(self.HandleAccount)
		self.HandAccMidFrame=tk.Frame(self.HandleAccount)
		self.HandAccBotFrame = tk.Frame(self.HandleAccount)
		self.HandAccTopFrame.pack()
		self.HandAccMidFrame.pack()
		self.HandAccBotFrame.pack()
		# Create top Frame widgets
		self.TransactionLabel = tk.Label(self.HandAccTopFrame,
	 	text='Enter the transaction amount here\n(negative amount for costs and postive for income):')
		self.TransactionEntry = tk.Entry(self.HandAccTopFrame, width=50)
		self.DateofTransLabel=tk.Label(self.HandAccTopFrame,text='Enter the date of the transaction:')
		self.DateofTransEntry=tk.Entry(self.HandAccTopFrame,width=50)
		self.TransactionTypeLabel=tk.Label(self.HandAccTopFrame,text='What type of transaction was this?')
		self.TransactionTypeEntry=tk.Entry(self.HandAccTopFrame,width=50)
		self.TransactionLabel.pack()
		self.TransactionEntry.pack()
		self.DateofTransLabel.pack()
		self.DateofTransEntry.pack()
		self.TransactionTypeLabel.pack()
		self.TransactionTypeEntry.pack()
		#Create Mid Frame Widgets
		# Create Account Treeview
		self.AccOverAccountsInfoTreeview = ttk.Treeview(self.HandAccMidFrame,
		columns=('column1', 'column2', 'column3', 'column4', 'column5','column6'), show='headings')
		self.AccOverAccountsInfoTreeview['columns'] =('AccountID', 'Account Type', 'Balance', 'TransactionID', 'Money Transferred', 'Date of Transaction')
		self.AccOverAccountsInfoTreeview.column('AccountID', width=100)
		self.AccOverAccountsInfoTreeview.heading("#1", text="AccountID")
		self.AccOverAccountsInfoTreeview.column('Account Type', width=100)
		self.AccOverAccountsInfoTreeview.heading("#2", text="Account Type")
		self.AccOverAccountsInfoTreeview.column('Balance', width=100)
		self.AccOverAccountsInfoTreeview.heading("#3", text="Balance")
		self.AccOverAccountsInfoTreeview.column('TransactionID', width=100)
		self.AccOverAccountsInfoTreeview.heading("#4", text="TransactionID")
		self.AccOverAccountsInfoTreeview.pack()
		self.AccOverAccountsInfoTreeview.column('Money Transferred', width=150)
		self.AccOverAccountsInfoTreeview.heading("#5", text="Money Transferred")
		self.AccOverAccountsInfoTreeview.pack()
		self.AccOverAccountsInfoTreeview.column('Date of Transaction', width=150)
		self.AccOverAccountsInfoTreeview.heading("#6", text="Date of Transaction")
		self.AccOverAccountsInfoTreeview.pack()
		# Populate treeview with data
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		# Creat bottom frame widgets
		self.ConfirmTransactionButton = tk.Button(self.HandAccBotFrame, text='Confirm Transaction',command=self.TransDataAndTransCommit)
		self.HandAccReturnParentWindow = tk.Button(self.HandAccBotFrame, text='Return to Parent Window',command=self.ReturnParentWindowHandAcc)
		self.HandAccQuitButton = tk.Button(self.HandAccBotFrame, text='Quit Program',
										   command=self.HandleAccount.destroy)
		self.ConfirmTransactionButton.pack(side='left')
		self.HandAccReturnParentWindow.pack(side='left')
		self.HandAccQuitButton.pack(side='left')
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		
	def TransferMoneyWindow(self):
		#remove account overview window
		self.AccountOverview.destroy()
		#create transfer money window
		self.TransferMoney = tk.Tk()
		self.TransferMoney.title('Transfer Money')
		#create frames
		self.TransMonTopFrame=tk.Frame(self.TransferMoney)
		self.TransMonTopMidFrame=tk.Frame(self.TransferMoney)
		self.TransMonBotMidFrame=tk.Frame(self.TransferMoney)
		self.TransMonBotFrame=tk.Frame(self.TransferMoney)
		self.TransMonTopFrame.pack()
		self.TransMonTopMidFrame.pack()
		self.TransMonBotMidFrame.pack()
		self.TransMonBotFrame.pack()
		#Create top frame widget
		self.GivingAccountLabel=tk.Label(self.TransMonTopFrame,text='Giving Accounts')
		self.RecipientAccountLabel=tk.Label(self.TransMonTopFrame,text='Recipient Accounts')
		self.GivingAccountLabel.pack(side='left')
		self.RecipientAccountLabel.pack(side='right')
		#Create middle top frame widgets
		self.GivingAccountListbox=tk.Listbox(self.TransMonTopMidFrame)
		self.RecipientAccountListbox=tk.Listbox(self.TransMonTopMidFrame)
		self.GivingAccountListbox.pack(side='left')
		self.RecipientAccountListbox.pack(side='right')
		#create bottom middle frame widgets
		self.AmountTransferredLabel=tk.Label(self.TransMonBotMidFrame,text='Amount being Transferred $:')
		self.AmountTransferredEntry=tk.Entry(self.TransMonBotMidFrame,width=50)
		self.AmountTransferredLabel.pack(side='left')
		self.AmountTransferredEntry.pack(side='left')
		#Create bottom frame widgets
		self.ConfirmTransferButton=tk.Button(self.TransMonBotFrame,text='Confirm Transfer')
		self.TransMonReturnParentWindowButton=tk.Button(self.TransMonBotFrame,text='Return to Parent Window',command=self.ReturnParentWindowTransMon)
		self.TransMonQuitButton=tk.Button(self.TransMonBotFrame,text='Quit Program',command=self.TransferMoney.destroy)
		self.ConfirmTransferButton.pack(side='left')
		self.TransMonReturnParentWindowButton.pack(side='left')
		self.TransMonQuitButton.pack(side='left')
	def TransactionHistoryWindow(self):
		# remove account overview window
		self.AccountOverview.destroy()
		# create transfer money window
		self.TransactionHistory = tk.Tk()
		self.TransactionHistory.title('Transaction History')
		#create frames
		self.TransHisTopFrame=tk.Frame(self.TransactionHistory)
		self.TransHisMidFrame = tk.Frame(self.TransactionHistory)
		self.TransHisBotFrame = tk.Frame(self.TransactionHistory)
		self.TransHisTopFrame.pack()
		self.TransHisMidFrame.pack()
		self.TransHisBotFrame.pack()
		#create top frame widget
		self.AccountHistoryLabel=tk.Label(self.TransHisTopFrame,text='Name account you want to show history of or type all to show all:')
		self.AccountHistoryEntry=tk.Entry(self.TransHisTopFrame,width=50)
		self.AccountHistoryLabel.pack(side='left')
		self.AccountHistoryEntry.pack(side='left')
		#create mid frame widget
		self.TransHisTransactionInfo = ttk.Treeview(self.TransHisMidFrame,
		columns=('column1', 'column2', 'column3', 'column4', 'column5','column6'), show='headings')
		self.TransHisTransactionInfo['columns'] = (
		'AccountID', 'Account Type', 'Balance', 'TransactionID', 'Money Transferred', 'Date of Transaction')
		self.TransHisTransactionInfo.column('AccountID', width=100)
		self.TransHisTransactionInfo.heading("#1", text="AccountID")
		self.TransHisTransactionInfo.column('Account Type', width=100)
		self.TransHisTransactionInfo.heading("#2", text="Account Type")
		self.TransHisTransactionInfo.column('Balance', width=100)
		self.TransHisTransactionInfo.heading("#3", text="Balance")
		self.TransHisTransactionInfo.column('TransactionID', width=100)
		self.TransHisTransactionInfo.heading("#4", text="TransactionID")
		self.TransHisTransactionInfo.pack()
		self.TransHisTransactionInfo.column('Money Transferred', width=150)
		self.TransHisTransactionInfo.heading("#5", text="Money Transferred")
		self.TransHisTransactionInfo.pack()
		self.TransHisTransactionInfo.column('Date of Transaction', width=150)
		self.TransHisTransactionInfo.heading("#6", text="Date of Transaction")
		self.TransHisTransactionInfo.pack()
		rows = FinanceProjectDatabaseAccess.TransactionHistory()
		for row in rows:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
		#create bottom frame widgets
		self.TransHisReturnParentButton = tk.Button(self.TransHisBotFrame, text='Return to Parent Window',
		command=self.ReturnParentWindowTransHis)
		self.AccountHistoryButton = tk.Button(self.TransHisBotFrame, text="Account's Transaction History",
	  	command=self.AccountHistory)
		self.TransHisQuitButton = tk.Button(self.TransHisBotFrame, text='Quit Program',
		command=self.TransactionHistory.destroy)
		self.TransHisReturnParentButton.pack(side='left')
		self.AccountHistoryButton.pack(side='left')
		self.TransHisQuitButton.pack(side='left')
	#End of Window Methods
	# Additional Methods
	def ReturnParentWindowAddDel(self):
		self.AddDeleteAccount.destroy()
		FinanceGUI()
	
	def ReturnParentWindowHandAcc(self):
		self.HandleAccount.destroy()
		FinanceGUI()
		
	def ReturnParentWindowTransMon(self):
		self.TransferMoney.destroy()
		FinanceGUI()
	def ReturnParentWindowTransHis(self):
		self.TransactionHistory.destroy()
		FinanceGUI()
	def TransDataAndTransCommit(self):
		# Get data for Transaction
		self.selected = self.AccOverAccountsInfoTreeview.focus()
		self.Account = self.AccOverAccountsInfoTreeview.item(self.selected, 'values')
		self.TransactionDate = self.DateofTransEntry.get()
		self.TransactionAmount=self.TransactionEntry.get()
		self.TransactionType=self.TransactionTypeEntry.get()
		FinanceProjectDatabaseAccess.HandleAccount(self.Account,self.TransactionDate,self.TransactionAmount,self.TransactionType)
		#Repopulate treeview with data
		for item in self.AccOverAccountsInfoTreeview.get_children():
			self.AccOverAccountsInfoTreeview.delete(item)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
	def AddAccount(self):
		self.AccountName=self.NameAccountEntry.get()
		self.IntialBalance=self.IntialBalanceEntry.get()
		FinanceProjectDatabaseAccess.AddDelAddAccount(self.IntialBalance,self.AccountName)
		self.ExistingAccountsListbox.delete(0, END)
		self.AccountNames = FinanceProjectDatabaseAccess.AccountName()
		print(self.AccountNames)
		for row in self.AccountNames:
			self.ExistingAccountsListbox.insert(tk.END, row)
	def DeleteAccount(self):
		AccountToDelete=self.ExistingAccountsListbox.get(self.ExistingAccountsListbox.curselection())
		print(AccountToDelete)
		for item in AccountToDelete:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			AccountToDelete=String
		FinanceProjectDatabaseAccess.AddDelDeleteAccount(AccountToDelete)
		self.ExistingAccountsListbox.delete(0,END)
		self.AccountNames = FinanceProjectDatabaseAccess.AccountName()
		print(self.AccountNames)
		for row in self.AccountNames:
			self.ExistingAccountsListbox.insert(tk.END, row)
	def AccountHistory(self):
		AccountHistory=self.AccountHistoryEntry.get()
		TransactionAccountHistory=FinanceProjectDatabaseAccess.AccountTransactionHistory(AccountHistory)
		print(TransactionAccountHistory)
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in TransactionAccountHistory:
			print(row)
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
# Call the Finance GUI Class
if __name__ == '__main__':
	FinanceGUI()