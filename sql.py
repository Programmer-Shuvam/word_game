import sqlite3 as sql
con=sql.connect('words.db')
c=con.cursor()
c.execute('create table if not exists words (word char(30))')
f=open("words.txt",'r')
data=f.read()
d=data.split(',')
for i in d:
    c.execute('INSERT INTO words VALUES (?);',(i,))
con.commit()
f.close()
