import pyodbc 
con = pyodbc.connect("Driver={SQL Server};"
                      "Server=IN2399645W1\SQLEXPRESS;"
                      "Database=dictData;"
                      "Trusted_Connection=yes;")


cursor = con.cursor()