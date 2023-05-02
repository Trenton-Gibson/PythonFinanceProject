#Created: 04/24/23
#Trenton Gibson
#FinanceProjectDatabaseAccess.py

# import sqlite resources
import sqlite3 as lite
import sys

conn = lite.connect('PythonFinanaces.db')

with conn:
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
		
	def AccOverDataWithoutTransID():
		conn = lite.connect('PythonFinanaces.db')
		cur = conn.cursor()
		AccountIDs = AccountOverviewTreeviewDataFiltering()

		cur.execute('''SELECT AccountID,Account_Type,Balance FROM Accounts
		WHERE AccountID NOT IN (SELECT AccountID FROM 'Transaction') ''')
		rows=cur.fetchall()
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
				TransIDList.insert(1, TransIDString)
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
AccOverDataWithTransID()
AccOverDataWithoutTransID()