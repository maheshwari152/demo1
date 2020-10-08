import pyodbc

print("CRUD using python")
def read(conn):
    print("Read the data from students table")
    cursor = conn.cursor()
    cursor.execute("select * from students")
    for row in cursor:
        print(f'row = {row}')
    print()

def create(conn):
   
    print("inserting values into students table")
    cursor = conn.cursor()
    cursor.execute(
        'insert into students(id,Name,email,city) values(?,?,?,?);',
        (3, 'black','m@gmail','hyd')
       
    )
    conn.commit()
    read(conn)

def update(conn):
    print("Update the values in student table")
    cursor = conn.cursor()
    cursor.execute(
        'update students set Name = ? where id = ?;',
        ('red','2')
    )
    conn.commit()
    read(conn)

def delete(conn):
    print("Delete the values in student table")
    cursor = conn.cursor()
    cursor.execute(
        'delete from students where id=?;',
        ('3')
    )
    conn.commit()
    read(conn)    

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=.;"
    "Database=mahi;"
    "Trusted_Connection=yes;"
)

read(conn)
create(conn)
update(conn)
delete(conn)

conn.close()