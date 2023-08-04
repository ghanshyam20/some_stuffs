#python exceptions=> When a python programs meets an error,it stops the execution of the rest of the program

# if 5>6:
#     print("five is greater than 6")

# else:
#     print("six is greater")


#python syntax error

# print("hello world!"

# for i in range(8):
#     print(i)

#exception handling in python!!
try:
    num=int(input("Enter any number:"))
    result=10/num
    print("Result is",result)

except ZeroDivisionError:
    print("Error:Cannot divide by zero.")


#In python exceptions are 
#1.ZeroDivisionError
#2.TypeError
#ValueError
#FileNotFoundError
#IndexError

#ZeroDIvisionError=Raised when we try to divide by zero
#TypeError=Raised when an operation or function is applied to an object of an inappropriate type
#valueError=Raised when a function recieves an argument of the crrect type but with an invalid value.
#FileNotFoundError=Raised when a file or directory is requested but cannot be found.

#IndexError=Raised when trying to access an index that is outside the bounds of sequence.

#dbeaver download garne !!1

#sql 
#dbeaver=It is a popular open-source database management tool that supports various database system ,making  it valuable and versatile tool for database adminstrations developers and daya analysis.It provides a graphical user interface for interacting with databases enablling users to exexute queries manage database structures and perform data analysis.

#key features of its

#1) cross-platform
#2) support for various database
#3) Data visulization
#4)Database schema management
#5) data transfer and migration
#6) extensions and plugins
#7) data export and import



#sql query 


#database can be broadly categorized into several types based on their structure, storage model and application. Here are some reasons.


#1) Relational database(RDBMS:
#Relational databases uses a tabular structure to store data, with rows representing records and columns represnting attributes.They reley on structured query language(sql) fo data manipulation.MySQl,PostgreSQL,Oracle,Microsoft SQl server and SQlite.

#sqlite3=development ko time ma use garinxa

#for production =oracle ,PostGreSQl

#NOSQl databases=>Non-relational databases designed to handle unstructured or semi-structured data. They offer flexible schema design and horizontal scalability.Different types of NOSQL databases include.

#document databases(MongoDB) store data in JSON-like document.
#key-Value stores
#Column-family stores=Organizes data into column families.

#Graph databasees=stores and manages data into graph structure.




#Object-oriented Databases=They are designed to work with object-oriented programming languages.They store objetcs directly and allow for complex data relationships.Examples include ObjectDB.



#Time-Series database are optimized for handling time-stamped or time-series data.Often used in applications like IOT,Financial system,monitoring.


#distrubuted database=>Distruted database spread data accross multiple nodes to achieve high availability ,faulttolerance and scalability .Exampples include Apache Hadoop Google Cloud Bigtable.


#In-memory databases=>In-memory databases store data in RAM for faster access and retrieval.offering high-speed perforamance.Examples includes Redis.


#spatial datbase=>It is designed to store and query spatial data. such s geographic information system (GIS) data.They support spatial indexing and geospatial operations.
#example include POSTGIS(an extension for Postgre SQL) and MongoDB with spatial features.







































