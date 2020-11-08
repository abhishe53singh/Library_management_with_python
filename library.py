import sqlite3

conn = sqlite3.connect('library.db')
cur=conn.cursor()
5
#--- - - SQL QUERIES  -- - - -- ---- - - - ---- - - 

def create():
	cur.execute("CREATE TABLE IF NOT EXISTS Books( book_n text  PRIMARY KEY, lended INTEGER , s_id text, staff_id text ,issue_d TIMESTAMP DEFAULT CURRENT_TIMESTAMP )")
	conn.commit()
	cur.execute("CREATE TABLE IF NOT EXISTS Login( id text , is_teacher INTEGER ,password text,times integer DEFAULT 0)")
	conn.commit()
#(id,is_teacher,password )
#book_n,lended,s_id,staff_id
create()	
#--- - - insert  -- - - -- ---- - - - ---- - - 	
def add_book(book_name , lended):
	cur.execute("INSERT INTO Books(book_n , lended) VALUES (? , ?)",(book_name , lended))
	conn.commit()
	
def del_book(book_name ):
	cur.execute(" delete from Books where book_n =? ",(book_name))
	conn.commit()	
	
def insert(book_name , lended , id , st ):
    cur.execute("INSERT INTO Books(book_n,lended,s_id,staff_id) VALUES (? ,?,?,?)",(book_name , lendmed , id , st ))
    conn.commit()
    
def insert_id( id, is_teacher, password ):
	cur.execute("INSERT INTO Login (id,is_teacher,password ) VALUES (?,?,?)",( id, is_teacher, password ))
	conn.commit()
    
      
def update_book(book_name , lended , id , st ):
	cur.execute("update Books set lended =? , s_id =? , staff_id =? where book_n =? ",( lended , id , st, book_name ))
	conn.commit()

def update_login_teacher(id, is_teacher, password):
	cur.execute("update Books set is_teacher = ? , password = ? where id = ? ",( is_teacher, password, id))
	conn.commit()

def tim(times,id):
	cur.execute("update Login set times=? where id = ? ",( times, id))
	conn.commit()
	
	
def update_login_student(id, is_teacher, password):
	cur.execute("update Books set is_teacher = ? , password = ? where id = ? ",( is_teacher, password, id))
	conn.commit()
    
###--SQL ENDED-------#####
	
##--- - - library functions  -- - - -- -- ---- - 
	
#--- - - display_books  -- - - -- ---- ---- - - - 
	
def display_books():
    for i in book :
        print(i)
    '''

	print(f"1	Available books\n2	Lended books")
	ch=input('Enyer choice : ')
	if ch == '1':
		if len(book)!=0:
			for i,c in enumerate(book):
				print(f"{i+1}  {c}")
		else:
			print('No books to lended')
		
	elif ch == '2':
		if len(return_book)!=0:
			for i,c in enumerate(return_book):
				print(f"{i+1}	{c}")
		else:
			print('No books lended')
		
	'''	

def tim_f(id):
	cur.execute("SELECT times FROM Login where id =? ",(id,))
	da=cur.fetchall()
	for i in da:
		for j in i:
			data=j
	times=int(data)+1
	tim(times,id)
	
	
def csv():
	import pandas as pd
	from pandas import ExcelWriter
	df_list = []
	df1=pd.read_sql_query("select * from Books;", conn)
	df2=pd.read_sql_query("select * from Login;", conn)
	# , header=False
	df_list.append(df1)
	df_list.append(df2)
	writer = ExcelWriter('library.xlsx')
	for n, df in enumerate(df_list):
	   df.to_excel(writer, 'sheet%s' % str(n + 1) , index=False)
	   #sheet_name=f'sheetName_{n+1}' )
	   writer.save()
	
	'''
	df.to_csv('library.csv',index=False)
	ndf=pd.read_csv('library.csv')
	print(ndf)
	'''
#####-- Lend_f  -- - - -- ---- - - - ---- - - - 			
def lend_f():
	try:
		st=tempid
		sp=temppas
		if st not in staff :
			print('please login first')
			teach()
		else:
			id=input('Enter student id = ')
			book_name=input('Enter book = ')
				
			if id not in lended_id and book_name in book and book_name not in return_book and id in s_id and st in staff and sp==s_d[st]:
				lended = 1
				#print( 'lended_id.append(id)' )
				#print( 'return_book')
				#lended , id , st, book_name
				update_book(book_name , lended , id , st )
				tim_f(id)
				print('Book lended')
				
			elif book_name in return_book:
					print('Book is already issued')
			elif book_name not in book or book_name in ['',' ']:
				print('Book not available')
			elif id in lended_id :
				print('Book is already issued on this id ')
			elif id not in s_id or id in ['',' '] :
				print('Invalid student id')
			#print('Invalid student id or staff id or password')
			
	#except AssertionError as e:
	except:
		#print(e)
		print('please login first')
		teach()

##---- return_f  -- - - -- ---- - - - ---- - - - 
			
def return_f ():
	try:
		st=tempid
		sp=temppas
		if sp!=s_d[st] :
			print('please login first')
			teach()
		else:
			#st=int(input('Enter your staff id = '))
			#sp=input('Enter your password = ')
			id=input('Enter student id = ')
			book_name=input('Enter book = ')
			if lend[id]==book_name and sp==s_d[st]:
				lended = 0
				print('updating')
				update_book( book_name,lended , id , st  )
				print('Book is returned')
				#print(lend)
			elif book_name not in return_book:
				print('book not lended')
			else :
				print(id,' has not lended ',book_name,' book')

	except:
		print('please login first')
		teach()
#####---ad  -- - - -- ---- - - - ---- - - - 

def ad():
	book_name=input('Enter book name = ')
	if book_name in['',' ' ]:
		print('Please enter a valid book name')
	elif book_name not in book :
		print('Book added')
		lended = 0
		add_book (book_name , lended )
	else:
		print('Book already exist')
		
		
		
def dele():
	book_name=input('Enter book name = ')
	if book_name in['',' ' ]:
		print('Please enter a valid book name')
	elif book_name in book :
		del_book (book_name)
		print('Book Deleted ')
	elif book_name in return_book :
		print('Book already issued ')
	elif book_name not in book :
		print("Book not available  ")
	
			
	

def teach():
	print('1	login\n2	logout')
	o=input('Choose option = ')
	if o=='1':
		logid=input('Enter id = ')
		logpas=input('Enter password = ')
		if logid in staff and logpas in s_d.values():
			global tempid
			tempid=logid
			global temppas
			temppas=logpas
			#	return(tempid,temppas)
		else:
			print('from login no tescher in s_d')
			print(s_d)
	elif o== '2':
		tempid=0
		temppas=''
	elif o==None:
		teach()
		
####------Admin  -- - - -- ---- - - - ---- - - - 

def admin():
	p='123'
	#p=input('Enter password')
	if p==pas:
		print('1	Add Teacher\n2	Add Student\n3	Books issued\n4	database')
		inp=input('Choose option = ')
		if inp=='1':
			ip=input('Enter Teacher\'s id')
			pa=input('Enter Password = ')
			if ip.isalpha():
				print('Please enter a digit')
			elif ip not in staff  and ip.isdigit() :
				if int(ip) <101:
					is_teacher = 1
					insert_id( ip, is_teacher, pa )
				else:
					print('Teacher\'s id should be less than 100')
			elif ip in staff:
				print('Entered id is already in use')
			'''elif ip<=0:
				print('Id less than 1 not allowed')
				'''
		elif inp== '2' :
			ip=input('Enter Students\'s id')
			if ip.isalpha():
				print('Please enter a digit')
			elif ip not in s_id and ip not in staff:
				if int(ip) >100:
					is_teacher = 0
					passw = 'student'
					insert_id( ip, is_teacher, passw )
				else:
					print('student id should be greater than 100')
			elif ip in s_id:
				print('Id is already alotted')
		elif inp == '3' :
			if len(return_book)!=0:
				for i,c in enumerate(return_book):
					print(f"{i+1}	{c}")
		elif inp== '4':
			print('Books database')
			cur.execute("SELECT *FROM Books")
			rows=cur.fetchall()
			for i in rows:
				print(i)
			print('Login database')
			cur.execute("SELECT *FROM Login")
			rows=cur.fetchall()
			for i in rows:
				print(i)
		'''
		else:
			print('No books lended')
		
		elif inp== '3' :
			for i in lend:
				print(i,lend[i])
		elif inp==None():
			admin()
		'''
					
	else:
		print('Unauthorised access denied')
		
def lender_data():
	print(lend_data)

#--- - - MAIN  -- - - -- ---- - - - ---- - - - 
		
def main():
	
	print('\n----Library Management----\n1	list of books\n2	Issue book\n3	Return\n4	Add book\n5	delete book\n6	Teacher \n7	administration\n8	lender database\n9	upload to csv')
	op=input('Enter your choice : ')
	if op==None:
		main()
	if op=='0':
		main()
	elif op=='1':
		display_books()
	elif op=='2':
		lend_f()
	elif op=='3':
		return_f()
	elif op=='4':
		ad()
	elif op=='5':
		dele()	
	elif op=='6':
		teach()
	elif op=='7':
		admin()
	elif op == '8':
		lender_data()
	elif op =='9':
		csv()
'''	elif op in ['',' ']:
		main()
'''

###------INITIALISE-----VARIABLES--------------
def init():
	global s_d,book,s_id,staff,lended_id,return_book,pas,lend,lend_data
	create()
	lend_data ={}
	cur.execute("SELECT s_id,book_n FROM Books where lended = 1 ")
	rows=cur.fetchall()
	for id,books in rows:
		lend_data[id] =books
	s_d={}
	cur.execute("SELECT id , password FROM Login where is_teacher=1")
	rows=cur.fetchall()
	
	for id,pas in rows:
		s_d[id]=pas
		#print(id,pas)
		
	book=[ ]
	cur.execute("SELECT book_n FROM Books where lended = 0 ")
	rows=cur.fetchall()
	for books in rows:
		for j in books:
			book.append(j)
	#print('Books ' , book)
	staff=s_d.keys()
	s_id=[ ]
	cur.execute("SELECT id FROM Login where is_teacher=0")
	rows=cur.fetchall()
	for id in rows:
		for j in id:
			s_id.append(j)
	#print('s_id ',s_id)
	lended_id=[ ]
	cur.execute("SELECT s_id FROM Books where lended = 1 ")
	rows=cur.fetchall()
	for books in rows:
		for j in books:
			lended_id.append(j)
	#print(lended_id)
	return_book=[ ]
	cur.execute("SELECT book_n FROM Books where lended =1 ")
	rows=cur.fetchall()
	for books in rows:
		for j in books:
			return_book.append(j)
	#print('book lended',return_book)
	pas='123'
	lend={}
	cur.execute("SELECT book_n,s_id FROM Books where lended = 1 ")
	rows=cur.fetchall()
	for books,id in rows:
		lend[id]=books
	
	#print('lend ',lend)
	#l=lend.keys()
	#print(f's_d {s_d}')
	#print(f's_id {s_id}')
	main()
	
	
###----Initialise ends--------

#--- - - Library start working  -- - - -- ---- -
##---MY CODE RUNNER
c='y'
while c=='y':
	init()
	c='y'

						