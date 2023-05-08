# Trenton Gibson
# Created: 04/21/23
# FinanceProjectGUI_V2.py

# import tkinter GUI materials
import tkinter as tk
from tkinter import *
from tkinter import ttk
import FinanceProjectDatabaseAccess
import tkinter.messagebox
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
		self.DeleteAccountLabelFrame=Frame(self.PersonalFinanceManager,relief=RAISED,borderwidth=10)
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
		self.DeleteAccountLabelFrame.pack()
		self.BottomFrame.pack()
		#pack child frame
		self.AddDeleteAccountFrame.pack(side='left')
		self.TransferMoneyLabelsFrame.pack(side='right')
		self.TransferMoneyFrame.pack(side='right')
		self.HandleAccountFrame.pack(side='left')
		self.TransactionHistoryFrame.pack(side='left')
		self.ButtonsFrame.pack(side='bottom')
		self.AccountTreeviewFrame.pack(side='left')
		self.TransactionTreeviewFrame.pack(side='left')
		# Widgets
		# Create Account Treeview
		self.Accounts_yscroll = Scrollbar(self.AccountTreeviewFrame)
		self.Accounts_yscroll.pack(side=LEFT, fill=Y)
		self.AccOverAccountsInfoTreeview = ttk.Treeview(self.AccountTreeviewFrame,height=10,
		columns=('column1', 'column2', 'column3', 'column4', 'column5','column6'),
		show='headings',yscrollcommand=self.Accounts_yscroll)
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
		self.Accounts_yscroll.config(command=self.AccOverAccountsInfoTreeview.yview)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		self.Transaction_yscroll=Scrollbar(self.TransactionTreeviewFrame)
		self.Transaction_yscroll.pack(side=RIGHT,fill=Y)
		
		self.TransHisTransactionInfo = ttk.Treeview(self.TransactionTreeviewFrame,height=10,
		columns=('column1', 'column2', 'column3', 'column4', 'column5','column6','column7'),
													show='headings',yscrollcommand=self.Transaction_yscroll.set)
		self.TransHisTransactionInfo['columns'] = (
			'AccountID', 'Account Type', 'Previous Balance','Current Balance', 'TransactionID', 'Money Transferred', 'Date of Transaction')
		self.TransHisTransactionInfo.column('AccountID',width=80)
		self.TransHisTransactionInfo.heading("#1", text="AccountID")
		self.TransHisTransactionInfo.column('Account Type',width=110)
		self.TransHisTransactionInfo.heading("#2", text="Account Type")
		self.TransHisTransactionInfo.column('Previous Balance',width=110)
		self.TransHisTransactionInfo.heading("#3", text="Previous Balance")
		self.TransHisTransactionInfo.column('Current Balance',width=110)
		self.TransHisTransactionInfo.heading("#4", text="Current Balance")
		self.TransHisTransactionInfo.column('TransactionID',width=110)
		self.TransHisTransactionInfo.heading("#5", text="TransactionID")
		self.TransHisTransactionInfo.column('Money Transferred',width=110)
		self.TransHisTransactionInfo.heading("#6", text="Money Transferred")
		self.TransHisTransactionInfo.column('Date of Transaction',width=110)
		self.TransHisTransactionInfo.heading("#7", text="Date of Transaction")
		self.TransHisTransactionInfo.pack(side='left')
		self.Transaction_yscroll.config(command=self.TransHisTransactionInfo.yview)
		self.StartAccountHistory=''
		rows = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for row in rows:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
		style = ttk.Style()
		style.configure("Treeview.Heading",fieldbackground='#9613bb',font=('Times New Roman', 11))
		style.configure("Treeview", font=('Times New Roman', 11))
		style.configure("Treeview", foreground='yellow', background='#9613bb')
		
		# Create buttons for button frame
		self.AccOverQuitButton = tk.Button(self.ButtonsFrame, text='Quit', command=self.PersonalFinanceManager.destroy,font=('Times New Roman',11))
		self.ConfirmTransactionButton = tk.Button(self.ButtonsFrame, text='Confirm Transaction',
												  command=self.TransDataAndTransCommit,font=('Times New Roman',11))
		self.AccountHistoryButton = tk.Button(self.ButtonsFrame, text="Transaction History",
											  command=self.AccountHistory,font=('Times New Roman',11))
		self.AddAccountButton = tk.Button(self.ButtonsFrame, text='Add Account', command=self.AddAccount,font=('Times New Roman',11))
		self.DeleteAccountButton = tk.Button(self.ButtonsFrame, text='Delete Account', command=self.DeleteAccount,font=('Times New Roman',11))
		self.ConfirmTransferButton = tk.Button(self.ButtonsFrame, text='Confirm Transfer',
											   command=self.TransferringMoney,font=('Times New Roman',11))
		self.ConfirmTransferButton.pack(side='left', padx=50)
		self.AddAccountButton.pack(side='left', padx=50)
		self.DeleteAccountButton.pack(side='left', padx=50)
		self.ConfirmTransactionButton.pack(side='left',padx=50)
		self.AccountHistoryButton.pack(side='left', padx=50)
		self.AccOverQuitButton.pack(side='left',padx=50)
		
		# transaction history frame widgets
		self.AccountHistoryLabel = tk.Label(self.TransactionHistoryFrame,
											text="Account's Transaction history: enter the name of the account below and click the Transaction History button.\n To restore the table click Transaction History button with the entry area blank.",font=('Times New Roman', 11))
		self.AccountHistoryEntry = tk.Entry(self.TransactionHistoryFrame, width=50,font=('Times New Roman',11))
		self.AccountHistoryLabel.pack()
		self.AccountHistoryEntry.pack()
		#create/delete account frame widgets
		self.CreateAccountLabel = tk.Label(self.AddDeleteAccountFrame,
		text='Fill the two entries below for a new account then click "Add Account"',font=('Times New Roman',11))
		self.NameAccountLabel = tk.Label(self.AddDeleteAccountFrame, text='Name your account:',font=('Times New Roman',11))
		self.NameAccountEntry = tk.Entry(self.AddDeleteAccountFrame, width=50,font=('Times New Roman',11))
		self.IntialBalanceLabel = tk.Label(self.AddDeleteAccountFrame, text='State the intial balance(only use numbers and decimals):',font=('Times New Roman',11))
		self.IntialBalanceEntry = tk.Entry(self.AddDeleteAccountFrame, width=50,font=('Times New Roman', 11))
		self.CreateAccountLabel.pack(padx=10)
		self.NameAccountLabel.pack(padx=10)
		self.NameAccountEntry.pack(padx=10)
		self.IntialBalanceLabel.pack(padx=10)
		self.IntialBalanceEntry.pack(padx=10)
		#create delete account label frame widget
		self.DeleteAccountLabel=Label(self.DeleteAccountLabelFrame,text='To Delete Account, Click the account row from the left table you want to delete then click Delete Account Button.'
	  ,font=('Times New Roman', 11))
		self.DeleteAccountLabel.pack()
		
		#Transfer money frame widgets
		self.GivingAccountButton = tk.Button(self.TransferMoneyFrame, text='Set Giving Account'
											 ,font=('Times New Roman',11), command=self.GetGivingAccount)
		self.RecipientAccountButton = tk.Button(self.TransferMoneyFrame, text='Set Recipient Account'
												,font=('Times New Roman',11),command=self.GetRecipientAccount)
		self.AmountTransferredLabel = tk.Label(self.TransferMoneyFrame, text='Transfer Money Between Accounts: First set the giving and recipient accounts\n by clicking the accounts in the left table and clicking the corresponding button.'
		'\nNext, put the amount the recipient account will receive(only use numbers and decimals). Finally, click "Confirm Transfer."',font=('Times New Roman',11))
		self.AmountTransferredEntry = tk.Entry(self.TransferMoneyFrame, width=50,font=('Times New Roman', 11))
		self.AmountTransferredLabel.pack()
		self.AmountTransferredEntry.pack()
		self.GivingAccountButton.pack()
		self.RecipientAccountButton.pack()
		# Transfer money label frames
		self.GiverAccountLabel=tk.Label(self.TransferMoneyLabelsFrame,text='Giving Account:',font=('Times New Roman',11), foreground='black', background='white')
		self.RecipientAccountLabel = tk.Label(self.TransferMoneyLabelsFrame,text='Recipient Account:',font=('Times New Roman', 11), foreground='black', background='white')
		self.GiverAccountLabel.pack()
		self.RecipientAccountLabel.pack()
		#handle account frame widgets
		self.TransactionLabel = tk.Label(self.HandleAccountFrame,
		text='To enter a transaction, click the account row in the left table where the transacation took place then put the transaction amount here.'
		'\nOnly enter numbers and decimals here(negative amount for costs and postive for income):',font=('Times New Roman', 11))
		self.TransactionEntry = tk.Entry(self.HandleAccountFrame, width=50,font=('Times New Roman', 11))
		self.DateofTransLabel = tk.Label(self.HandleAccountFrame, text='Next, enter the date of the transaction:',font=('Times New Roman', 11))
		self.DateofTransEntry = tk.Entry(self.HandleAccountFrame, width=50,font=('Times New Roman', 11))
		self.TransactionTypeLabel = tk.Label(self.HandleAccountFrame, text=' Third, put in what type of transaction occured and then click Confirm Transaction button:',font=('Times New Roman', 11))
		self.TransactionTypeEntry = tk.Entry(self.HandleAccountFrame, width=50,font=('Times New Roman', 11))
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
		try:
			# Get data for Transaction
			self.selected = self.AccOverAccountsInfoTreeview.focus()
			self.Account = self.AccOverAccountsInfoTreeview.item(self.selected, 'values')
			self.TransactionDate = self.DateofTransEntry.get()
			self.TransactionAmount = self.TransactionEntry.get()
			self.TransactionType = self.TransactionTypeEntry.get()
			if self.TransactionDate == ''or self.TransactionAmount =='' or self.TransactionType == '':
				# Create an error message variable
				self.ErrorMessage = 'Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
			else:
				FinanceProjectDatabaseAccess.HandleAccount(self.Account, self.TransactionDate, self.TransactionAmount, self.TransactionType)
				# Repopulate treeviews with data
				self.RepopulateAccountsTreeview()
				self.RepopulateTransactionsTreeview()
				self.DateofTransEntry.delete(0, END)
				self.TransactionEntry.delete(0, END)
				self.TransactionTypeEntry.delete(0, END)
		except:
			# Create an error message variable
			self.ErrorMessage ='Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	def AddAccount(self):
		try:
			self.AccountName = self.NameAccountEntry.get()
			self.IntialBalance = self.IntialBalanceEntry.get()
			if self.AccountName == '' or self.IntialBalance == '':
				# Create an error message variable
				self.ErrorMessage = 'Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
			else:
				FinanceProjectDatabaseAccess.AddDelAddAccount(self.IntialBalance, self.AccountName)
				# Repopulate treeviews with data
				self.RepopulateAccountsTreeview()
				self.RepopulateTransactionsTreeview()
				self.NameAccountEntry.delete(0,END)
				self.IntialBalanceEntry.delete(0,END)
		except:
			# Create an error message variable
			self.ErrorMessage ='Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	def DeleteAccount(self):
		try:
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
			self.RepopulateAccountsTreeview()
			self.RepopulateTransactionsTreeview()
		except:
			# Create an error message variable
			self.ErrorMessage ='Error! Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	def AccountHistory(self):
		try:
			self.AccountHistory = self.AccountHistoryEntry.get()
			if self.AccountHistory=='':
				# Create an error message variable
				self.ErrorMessage = 'Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
			else:
				TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.AccountHistory)
				self.RepopulateAccountsTreeview()
		except:
			# Create an error message variable
			self.ErrorMessage ='Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	def TransferringMoney(self):
		try:
			self.TransferredMoney = self.AmountTransferredEntry.get()
			self.TransMonGivingAccount = self.GivingAccount
			self.TransMonRecipientAccount = self.RecipientAccount
			if self.TransferredMoney == '' or self.TransMonGivingAccount == '' or self.TransMonRecipientAccount=='':
				# Create an error message variable
				self.ErrorMessage = 'Follow the directions and please try again.'
				# Display the error message in an info dialog box.
				tk.messagebox.showinfo('Error!', self.ErrorMessage)
			else:
				FinanceProjectDatabaseAccess.AccountTransfer \
					(self.TransferredMoney, self.TransMonGivingAccount, self.TransMonRecipientAccount)
				# Repopulate treeviews with data
				self.RepopulateAccountsTreeview()
				self.RepopulateTransactionsTreeview()
				self.GiverAccountLabel.config(text='Giving Account:',font=('Times New Roman', 11), foreground='black', background='white')
				self.RecipientAccountLabel.config(text='Recipient Account:',font=('Times New Roman', 11), foreground='black', background='white')
				self.AmountTransferredEntry.delete(0,END)
		except:
			# Create an error message variable
			self.ErrorMessage ='Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	def GetGivingAccount(self):
		try:
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
			self.GiverAccountLabel.config(text='Giving Account:'+self.GivingAccount,font=('Times New Roman',11), foreground='yellow', background='#9613bb')
			return self.GivingAccount
		except:
			# Create an error message variable
			self.ErrorMessage ='Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	def GetRecipientAccount(self):
		try:
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
			self.RecipientAccountLabel.config(text='Recipient Account:' + self.RecipientAccount,font=('Times New Roman',11), foreground='yellow', background='#9613bb')
			return self.RecipientAccount
		except:
			# Create an error message variable
			self.ErrorMessage ='Follow the directions and please try again.'
			# Display the error message in an info dialog box.
			tk.messagebox.showinfo('Error!', self.ErrorMessage)
	def RepopulateAccountsTreeview(self):
		for item in self.AccOverAccountsInfoTreeview.get_children():
			self.AccOverAccountsInfoTreeview.delete(item)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
		rows = FinanceProjectDatabaseAccess.AccOverDataWithoutTransID()
		for row in rows:
			self.AccOverAccountsInfoTreeview.insert("", tk.END, values=row)
	def RepopulateTransactionsTreeview(self):
		TransactionAccountHistory = FinanceProjectDatabaseAccess.AccountTransactionHistory(self.StartAccountHistory)
		for item in self.TransHisTransactionInfo.get_children():
			self.TransHisTransactionInfo.delete(item)
		for row in TransactionAccountHistory:
			self.TransHisTransactionInfo.insert("", tk.END, values=row)
# Call the Finance GUI Class
if __name__ == '__main__':
	FinanceGUI()