import mysql.connector as mysql

myhost = "localhost"
myuser = "python"
mypass = "pythonmysql"

db = mysql.connect(host=myhost,user=myuser,password=mypass)
cur = db.cursor()
cur.execute('CREATE DATABASE IF NOT EXISTS mydatabase')
db = mysql.connect(host=myhost,user=myuser,password=mypass,database="mydatabase")   
cur = db.cursor(buffered = True)
cur.execute("DROP TABLE IF EXISTS customers")
sql_create = ''' CREATE TABLE IF NOT EXISTS customers(
                                            id INT AUTO_INCREMENT PRIMARY KEY,
                                            name VARCHAR(255),
                                            gender CHAR(5),
                                            address VARCHAR(255),
                                            acc_type CHAR(20),
                                            phone CHAR(11),
                                            balance NUMERIC(10, 2)
                                            )'''
cur.execute(sql_create)


class Customer:
    def __init__(self,id):
        self.id = id
        sql = "SELECT * FROM customers WHERE id=%s"
        cur.execute(sql,(id,))
        self.customer_info = cur.fetchone()
        self.name = self.customer_info[1]
        self.gender = self.customer_info[2]
        self.address = self.customer_info[3]
        self.acc_type = self.customer_info[4]
        self.phone = self.customer_info[5]
        self.banlance = self.customer_info[6]

    @staticmethod
    def add(new_customer):
        sql = "INSERT INTO customers(name,gender,address,acc_type,phone,balance) VALUES(%s,%s,%s,%s,%s,%s)"
        val = new_customer
        cur.execute(sql,val)
        db.commit()

    def get(self):
        return self.customer_info


def initialize():
    Customer.add(('John Doe','M','Buffalo,NY','Saving','5022222222',5000))
    Customer.add(('Bela Doe','F','Baker,CA','Saving','5022222222',1000))