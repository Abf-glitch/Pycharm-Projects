import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','Kariuki',45,86000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Mary','Mbotela',34,57000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Ann','Agness',56,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Joe','Wairagu',25,83000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Mark','Ndambuki',19,66000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Whitney','Kimberly',33,76000.00)")

conn.commit()
print("Teachers inserted successfully")
conn.close()
