#Created: 04/24/23
#Trenton Gibson
#FinanceProjectDatabaseAccess.py

# import sqlite resources
import sqlite3 as lite
import sys

conn = lite.connect('PythonFinanaces.db')

with conn:
	#Gets AccountIDs with Transactions
	def AccOverDataWithTransID():
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		AccountIDs = AccountOverviewTreeviewDataFiltering()
		rows=[]
		AddRows=()
		for item in AccountIDs:
			TransIDList= TransIDProcessing(item)
			if 'e' not in TransIDList:
				MaxTransID = max(TransIDList)
				MaxTransID=str(MaxTransID)
				AddRows= tuple(WithTransIDAccountInfo(MaxTransID))
				rows.insert(1,AddRows)
		conn.close()
		return rows
		
	
	def AccountOverviewTreeviewDataFiltering():
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		cur.execute("SELECT AccountID FROM Accounts")
		rows = list(cur.fetchall())
		AccIDList = []
		for item in rows:
			AccIDString = str(item)
			AccIDString = AccIDString.lstrip('(')
			AccIDString = AccIDString.rstrip(')')
			AccIDString = AccIDString.rstrip(',')
			AccIDInt = int(AccIDString)
			AccIDList.insert(1, AccIDInt)
		return AccIDList
	
	def TransIDProcessing(AccountID):
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		cur.execute("SELECT TransactionID FROM 'Transaction' WHERE AccountID=?", (AccountID,))
		TransID = cur.fetchall()
		TransIDList = []
		if len(TransID)>0:
			for item in TransID:
				TransIDString = str(item)
				TransIDString = TransIDString.lstrip('(')
				TransIDString = TransIDString.rstrip(')')
				TransIDString = TransIDString.rstrip(',')
				TransIDInt=int(TransIDString)
				TransIDList.insert(1, TransIDInt)
		if not TransIDList:
			TransIDList='e'
		if TransIDList:
			return TransIDList
	def WithTransIDAccountInfo(MaxTransID):
		conn=lite.connect('PythonFinanaces.db')
		cur=conn.cursor()
		cur.execute('''SELECT Accounts.AccountID,Accounts.Account_Type,Accounts.Balance,
		'Transaction'.TransactionID,'Transaction'.Money_Transferred,'Transaction'.Date_Of_Transaction
		FROM Accounts INNER JOIN 'Transaction' ON Accounts.AccountID= 'Transaction'.AccountID
		WHERE TransactionID=?''',(MaxTransID,))
		rows = cur.fetchall()
		for item in rows:
			String =item
			break
		rows=String
		conn.close()
		return rows
	#Get Accounts without Transactions
	def AccOverDataWithoutTransID():
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		cur.execute('''SELECT AccountID,Account_Type,Balance FROM Accounts
		WHERE AccountID NOT IN (SELECT AccountID FROM 'Transaction') ''')
		rows=cur.fetchall()
		conn.close()
		return rows
	def HandleAccount(AccountInfo,TransactionDate,TransactionAmount,TransactionType):
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		if len(TransactionAmount)>0:
			TransactionAmount=float(TransactionAmount)
			TransactionAmount = round(TransactionAmount, 2)
		AccountNum=AccountInfo[0]
		cur.execute('SELECT Balance FROM Accounts WHERE AccountID = ?',(AccountNum,))
		PreviousBalance =cur.fetchall()
		for item in PreviousBalance:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			PreviousBalance=(String)
		PreviousBalance = float(PreviousBalance)
		PreviousBalance = round(PreviousBalance, 2)
		if TransactionAmount!=0:
			NewBalance=PreviousBalance+TransactionAmount
			NewBalance = round(NewBalance, 2)
		cur.execute('SELECT max(TransactionID) FROM "Transaction"')
		TransID=cur.fetchall()
		for item in TransID:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			NewTransID=int(String)+1
		cur.execute('''INSERT INTO 'Transaction'VALUES(?,?,?,?,?,?,?)'''
		,(NewTransID,AccountNum,TransactionDate,TransactionAmount,PreviousBalance,NewBalance,TransactionType))
		cur.execute('SELECT * FROM "Transaction"')
		rows=cur.fetchall()
		conn.commit()
		cur.execute('''UPDATE Accounts SET Balance=? WHERE AccountID=? ''',(NewBalance,AccountNum))
		rows = cur.fetchall()
		conn.commit()
		conn.close()
	def AddDelAddAccount(Balance,AccountType):
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		cur.execute('''INSERT INTO Accounts (Balance,Account_Type)VALUES(?,?)''',(Balance,AccountType))
		conn.commit()
		conn.close()
	def AccountName():
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		cur.execute('SELECT Account_Type FROM Accounts')
		AccountName=cur.fetchall()
		conn.close
		return AccountName
	def AddDelDeleteAccount(ToBeDeletedAccount):
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		cur.execute('''DELETE FROM Accounts WHERE Account_Type=?''',(ToBeDeletedAccount,))
		conn.commit()
		conn.close()
	def TransactionHistory():
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		cur.execute("SELECT Accounts.AccountID,Accounts.Account_Type,Accounts.Balance,"
		"'Transaction'.TransactionID,'Transaction'.Money_Transferred,'Transaction'.Date_Of_Transaction "
		"FROM Accounts INNER JOIN 'Transaction' ON Accounts.AccountID= 'Transaction'.AccountID")
		TransactionHistory=cur.fetchall()
		conn.close()
		return TransactionHistory
	def AccountTransactionHistory(AccountHistory):
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		if AccountHistory=='':
			cur.execute("SELECT Accounts.AccountID,Accounts.Account_Type,'Transaction'.Previous_Balance,'Transaction'.New_Balance,"
			"'Transaction'.TransactionID,'Transaction'.Money_Transferred,'Transaction'.Date_Of_Transaction "
			"FROM Accounts INNER JOIN 'Transaction' ON Accounts.AccountID= 'Transaction'.AccountID")
		else:
			cur.execute("SELECT Accounts.AccountID,Accounts.Account_Type,'Transaction'.Previous_Balance,'Transaction'.New_Balance,"
			"'Transaction'.TransactionID,'Transaction'.Money_Transferred,'Transaction'.Date_Of_Transaction "
			"FROM Accounts INNER JOIN 'Transaction' ON Accounts.AccountID= 'Transaction'.AccountID WHERE Account_Type=?",
			(AccountHistory,))
		AccountTransactionHistory=cur.fetchall()
		conn.close()
		return AccountTransactionHistory
	def AccountTransfer(AmountTransferred,GivingAccount,RecipientAccount):
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		AmountTransferred=float(AmountTransferred)
		AmountTransferred = round(AmountTransferred, 2)
		cur.execute('SELECT max(TransactionID) FROM "Transaction"')
		TransID = cur.fetchall()
		for item in TransID:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			NewTransID=int(String)+1
		cur.execute('''SELECT AccountID FROM Accounts WHERE Account_Type=?''',(RecipientAccount,))
		AccountNum=cur.fetchall()
		for item in AccountNum:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			AccountNum=int(String)
		cur.execute('SELECT Balance FROM Accounts WHERE AccountID = ?', (AccountNum,))
		PreviousBalance = cur.fetchall()
		for item in PreviousBalance:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			PreviousBalance = (String)
		PreviousBalance = float(PreviousBalance)
		PreviousBalance = round(PreviousBalance, 2)
		NewBalance = PreviousBalance + AmountTransferred
		NewBalance = round(NewBalance, 2)
		cur.execute('''INSERT INTO 'Transaction'VALUES(?,?,date(),?,?,?,'Recipient of transfer')'''
		,(NewTransID,AccountNum,AmountTransferred,PreviousBalance,NewBalance))
		cur.execute('''UPDATE Accounts SET Balance=(Balance+?) WHERE Account_Type=?''',
					(AmountTransferred, RecipientAccount))
		AmountTransferred=float(AmountTransferred)
		AmountTransferred=-(AmountTransferred)
		AmountTransferred = round(AmountTransferred, 2)
		cur.execute('SELECT max(TransactionID) FROM "Transaction"')
		TransID = cur.fetchall()
		for item in TransID:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			NewTransID = int(String) + 1
		cur.execute('''SELECT AccountID FROM Accounts WHERE Account_Type=?''', (GivingAccount,))
		AccountNum = cur.fetchall()
		for item in AccountNum:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			AccountNum = int(String)
		cur.execute('SELECT Balance FROM Accounts WHERE AccountID = ?', (AccountNum,))
		PreviousBalance = cur.fetchall()
		for item in PreviousBalance:
			String = str(item)
			String = String.lstrip('(')
			String = String.rstrip(')')
			String = String.rstrip(',')
			PreviousBalance = (String)
		PreviousBalance = float(PreviousBalance)
		PreviousBalance = round(PreviousBalance, 2)
		NewBalance = PreviousBalance + AmountTransferred
		NewBalance = round(NewBalance, 2)
		cur.execute('''INSERT INTO 'Transaction'VALUES(?,?,date(),?,?,?,'Transfer')'''
					, (NewTransID, AccountNum, AmountTransferred, PreviousBalance, NewBalance))
		cur.execute('''UPDATE Accounts SET Balance=(Balance+?) WHERE Account_Type=?''',
					(AmountTransferred, GivingAccount))
		conn.commit()
		conn.close()
if __name__ == '__main__':
	AccOverDataWithTransID()
	AccOverDataWithoutTransID()
	HandleAccount('AccountInfo','TransactionAmount','TransactionType','TransactionDate')