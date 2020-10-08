Introductory information
	Filename-student.py
To perform CRUD operations using python I have choosed visual studio and SQL server
Visual studio-installed python Application, pyodbc,pip,pypyodbc
SQL server managment-installed SQL Server

Methodological information
 Used pyodbc to connect to SQL Server
Created database=mahi
server="."
imported pyodc
defined a connection using pyodbc using a string
given a server name and database name to connect db can check by going to SQL Server
used 4 functions read(),create(),update(),delete() and given connection
 
read()
4 rows in the table as id,Name,city,email
used a varible as cursor 
used a foreach loop to print all rows from table
create()
used insert query and connection to SQLServer and calling the read function to preview the data
update()
used update query and decalred values and called read function to preview data
delete()
given a delete query and given condition to delete values, commited the changes
