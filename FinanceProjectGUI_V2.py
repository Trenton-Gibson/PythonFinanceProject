# Trenton Gibson
# Created: 04/21/23
# FinanceProjectGUI_V2.py

# import tkinter GUI materials
import tkinter as tk
from tkinter import *
from tkinter import ttk
import FinanceProjectDatabaseAccess


# Create Finance GUI class
class FinanceGUI:
	def __init__(self):
		# Create Account Overview window
		self.PersonalFinanceManager = tk.Tk()
		self.PersonalFinanceManager.title('Personal Finance Manager')
		self.PersonalFinanceManager.geometry("1920x1080")
		self.PersonalFinanceManager.attributes('-fullscreen', True)
		# Create Frames and  Widgets for Account Overview window
		# Create Parent Frames
		self.TopFrame=Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		self.TopMidFrame = Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		self.BottomMidFrame = Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		self.BottomFrame=Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
		# Create child frames
		self.AccountTreeviewFrame = Frame(self.BottomMidFrame,relief=SUNKEN,borderwidth=10)
		self.TransactionTreeviewFrame = Frame(self.BottomMidFrame, relief=SUNKEN, borderwidth=10)
		self.ButtonsFrame = Frame(self.BottomFrame,relief=RAISED,borderwidth=10)
		self.HandleAccountFrame=Frame(self.TopMidFrame,relief=SUNKEN,borderwidth=10)
		self.TransferMoneyFrame=Frame(self.TopFrame,relief=SUNKEN,borderwidth=10)
		self.AddDeleteAccountFrame=Frame(self.TopFrame,relief=SUNKEN,borderwidth=10)
		self.TransactionHistoryFrame=Frame(self.TopMidFrame,relief=SUNKEN,borderwidth=10)
		self.TransferMoneyLabelsFrame=Frame(self.TopFrame,relief=SUNKEN,borderwidth=10)
		#pack parent frames
		self.TopFrame.pack()
		self.TopMidFrame.pack()
		self.BottomMidFrame.pack()
		self.BottomFrame.pack()
		#pack child frame
		self.AddDeleteAccountFrame.pack(side='left', padx=50)
		self.TransferMoneyLabelsFrame.pack(side='right',padx=50)
		self.TransferMoneyFrame.pack(side='right', padx=50)
		self.HandleAccountFrame.pack(side='left',padx=200)
		self.TransactionHistoryFrame.pack(side='left',padx=200)
		self.ButtonsFrame.pack(side='bottom')
		self.AccountTreeviewFrame.pack(side='left')
		self.TransactionTreeviewFrame.pack(side='left')
		# Widgets
		# Create Account Treeview
		self.AccOverAccountsInfoTreeview = ttk.Treeview(self.AccountTreeviewFrame,height=20,
														columns=('column1', 'column2', 'column3', 'column4', 'column5',
																 'column6'), show='headings')
		self.AccOverAccountsInfoTreeview['columns'] = \
			('AccountID', 'Account Type', 'Balance', 'TransactionID', 'Money Transferred', 'Date of Transaction')
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
		self.AccOverAccountsInfoTreeview.pack(side='left')
		# Populate treeview with data
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		self.TransHisTransactionInfo = ttk.Treeview(self.TransactionTreeviewFrame,height=20,
		columns=('column1', 'column2', 'column3', 'column4', 'column5','column6','column7'),
													show='headings')
		self.TransHisTransactionInfo['columns'] = (
			'AccountID', 'Account Type', 'Previous Balance','Current Balance', 'TransactionID', 'Money Transferred', 'Date of Transaction')
		self.TransHisTransactionInfo.column('AccountID', width=100)
		self.TransHisTransactionInfo.heading("#1", text="AccountID")
		self.TransHisTransactionInfo.column('Account Type', width=100)
		self.TransHisTransactionInfo.heading("#2", text="Account Type")
		self.TransHisTransactionInfo.column('Previous Balance', width=100)
		self.TransHisTransactionInfo.heading("#3", text="Previous Balance")
		self.TransHisTransactionInfo.column('Current Balance',width=100)
		self.TransHisTransactionInfo.heading("#4", text="Current Balance")
		self.TransHisTransactionInfo.column('TransactionID', width=100)
		self.TransHisTransactionInfo.heading("#5", text="TransactionID")
		self.TransHisTransactionInfo.pack()
		self.TransHisTransactionInfo.column('Money Transferred', width=150)
		self.TransHisTransactionInfo.heading("#6", text="Money Transferred")
		self.TransHisTransactionInfo.pack()
		self.TransHisTransactionInfo.column('Date of Transaction', width=150)
		self.TransHisTransactionInfo.heading("#7", text="Date of Transaction")
		self.TransHisTransactionInfo.pack(side='left')
		self.StartAccountHistory='all'
		rows = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for row in rows:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
		# Create buttons for button frame
		self.AccOverQuitButton = tk.Button(self.ButtonsFrame, text='Quit', command=self.PersonalFinanceManager.destroy)
		self.ConfirmTransactionButton = tk.Button(self.ButtonsFrame, text='Confirm Transaction',
												  command=self.TransDataAndTransCommit)
		self.AccountHistoryButton = tk.Button(self.ButtonsFrame, text="Account's Transaction History",
											  command=self.AccountHistory)
		self.AddAccountButton = tk.Button(self.ButtonsFrame, text='Add Account', command=self.AddAccount)
		self.DeleteAccountButton = tk.Button(self.ButtonsFrame, text='Delete Account', command=self.DeleteAccount)
		self.ConfirmTransferButton = tk.Button(self.ButtonsFrame, text='Confirm Transfer',
											   command=self.TransferringMoney)
		self.ConfirmTransferButton.pack(side='left', padx=50)
		self.AddAccountButton.pack(side='left', padx=50)
		self.DeleteAccountButton.pack(side='left', padx=50)
		self.ConfirmTransactionButton.pack(side='left',padx=50)
		self.AccountHistoryButton.pack(side='left', padx=50)
		self.AccOverQuitButton.pack(side='left',padx=50)
		
		# transaction history frame widgets
		self.AccountHistoryLabel = tk.Label(self.TransactionHistoryFrame,
											text='Name account you want to show history of or type all to show all:')
		self.AccountHistoryEntry = tk.Entry(self.TransactionHistoryFrame, width=50)
		self.AccountHistoryLabel.pack()
		self.AccountHistoryEntry.pack()
		#create/delete account frame widgets
		self.CreateAccountLabel = tk.Label(self.AddDeleteAccountFrame,
										   text='Fill the two entries below for a new account then click "Create Account"')
		self.NameAccountLabel = tk.Label(self.AddDeleteAccountFrame, text='Name your account:')
		self.NameAccountEntry = tk.Entry(self.AddDeleteAccountFrame, width=50)
		self.IntialBalanceLabel = tk.Label(self.AddDeleteAccountFrame, text='State the intial balance:')
		self.IntialBalanceEntry = tk.Entry(self.AddDeleteAccountFrame, width=50)
		self.CreateAccountLabel.pack(padx=10)
		self.NameAccountLabel.pack(padx=10)
		self.NameAccountEntry.pack(padx=10)
		self.IntialBalanceEntry.pack(padx=10)
		self.IntialBalanceLabel.pack(padx=100)
		#Transfer money frame widgets
		self.GivingAccountButton = tk.Button(self.TransferMoneyFrame, text='Set Giving Account',
											 command=self.GetGivingAccount)
		self.RecipientAccountButton = tk.Button(self.TransferMoneyFrame, text='Set Recipient Account',
												command=self.GetRecipientAccount)
		self.AmountTransferredLabel = tk.Label(self.TransferMoneyFrame, text='Amount being Transferred into Recipient $:')
		self.AmountTransferredEntry = tk.Entry(self.TransferMoneyFrame, width=50)
		self.AmountTransferredLabel.pack()
		self.AmountTransferredEntry.pack()
		self.GivingAccountButton.pack()
		self.RecipientAccountButton.pack()
		# Transfer money label frames
		self.GiverAccountLabel=tk.Label(self.TransferMoneyLabelsFrame,text='Giving Account:',font='Algerian')
		self.RecipientAccountLabel = tk.Label(self.TransferMoneyLabelsFrame,text='Recipient Account:',font='Algerian')
		self.GiverAccountLabel.pack()
		self.RecipientAccountLabel.pack()
		#handle account frame widgets
		self.TransactionLabel = tk.Label(self.HandleAccountFrame,
										 text='Enter the transaction amount here\n(negative amount for costs and postive for income):')
		self.TransactionEntry = tk.Entry(self.HandleAccountFrame, width=50)
		self.DateofTransLabel = tk.Label(self.HandleAccountFrame, text='Enter the date of the transaction:')
		self.DateofTransEntry = tk.Entry(self.HandleAccountFrame, width=50)
		self.TransactionTypeLabel = tk.Label(self.HandleAccountFrame, text='What type of transaction was this?')
		self.TransactionTypeEntry = tk.Entry(self.HandleAccountFrame, width=50)
		self.TransactionLabel.pack()
		self.TransactionEntry.pack()
		self.DateofTransLabel.pack()
		self.DateofTransEntry.pack()
		self.TransactionTypeLabel.pack()
		self.TransactionTypeEntry.pack()
		# Start the mainloop
		tk.mainloop()
	# Additional Methods
	def TransDataAndTransCommit(self):
		# Get data for Transaction
		self.selected = self.AccOverAccountsInfoTreeview.focus()
		self.Account = self.AccOverAccountsInfoTreeview.item(self.selected, 'values')
		self.TransactionDate = self.DateofTransEntry.get()
		self.TransactionAmount = self.TransactionEntry.get()
		self.TransactionType = self.TransactionTypeEntry.get()
		FinanceProjectDatabaseAccess.HandleAccount(self.Account, self.TransactionDate, self.TransactionAmount,
												   self.TransactionType)
		# Repopulate treeviews with data
		for item in self.AccOverAccountsInfoTreeview.get_children():
			self.AccOverAccountsInfoTreeview.delete(item)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
	
	def AddAccount(self):
		self.AccountName = self.NameAccountEntry.get()
		self.IntialBalance = self.IntialBalanceEntry.get()
		FinanceProjectDatabaseAccess.AddDelAddAccount(self.IntialBalance, self.AccountName)
		# Repopulate treeviews with data
		for item in self.AccOverAccountsInfoTreeview.get_children():
			self.AccOverAccountsInfoTreeview.delete(item)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
	
	def DeleteAccount(self):
		self.selected = self.AccOverAccountsInfoTreeview.focus()
		self.AccountToDelete= self.AccOverAccountsInfoTreeview.item(self.selected, 'values')
		count=0
		for item in self.AccountToDelete:
			count+=1
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			self.AccountToDelete = String
			if count>1:
				break
		FinanceProjectDatabaseAccess.AddDelDeleteAccount(self.AccountToDelete)
		# Repopulate treeviews with data
		for item in self.AccOverAccountsInfoTreeview.get_children():
			self.AccOverAccountsInfoTreeview.delete(item)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
	
	def AccountHistory(self):
		self.AccountHistory = self.AccountHistoryEntry.get()
		TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.AccountHistory)
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
	
	def TransferringMoney(self):
		self.TransferredMoney = self.AmountTransferredEntry.get()
		self.TransMonGivingAccount = self.GivingAccount
		self.TransMonRecipientAccount = self.RecipientAccount
		FinanceProjectDatabaseAccess.AccountTransfer \
			(self.TransferredMoney, self.TransMonGivingAccount, self.TransMonRecipientAccount)
		# Repopulate treeviews with data
		for item in self.AccOverAccountsInfoTreeview.get_children():
			self.AccOverAccountsInfoTreeview.delete(item)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
		self.GiverAccountLabel.config(text='Giving Account:',font='Algerian')
		self.RecipientAccountLabel.config(text='Recipient Account:')
	
	def GetGivingAccount(self):
		self.selected = self.AccOverAccountsInfoTreeview.focus()
		self.GivingAccount = self.AccOverAccountsInfoTreeview.item(self.selected, 'values')
		count = 0
		for item in self.GivingAccount:
			count += 1
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			self.GivingAccount = String
			if count > 1:
				break
		self.GiverAccountLabel.config(text='Giving Account:'+self.GivingAccount)
		return self.GivingAccount
	
	def GetRecipientAccount(self):
		self.selected = self.AccOverAccountsInfoTreeview.focus()
		self.RecipientAccount = self.AccOverAccountsInfoTreeview.item(self.selected, 'values')
		count = 0
		for item in self.RecipientAccount:
			count += 1
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			self.RecipientAccount = String
			if count > 1:
				break
		self.RecipientAccountLabel.config(text='Giving Account:' + self.RecipientAccount)
		return self.RecipientAccount
		
# Call the Finance GUI Class
if __name__ == '__main__':
	FinanceGUI()