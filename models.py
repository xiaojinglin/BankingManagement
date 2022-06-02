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


    def __repr__(self):
        return f'''ID: {self.id}
                \rName: {self.name}, Gender: {self.gender}, Address: {self.address} 
                \rAccount Type: {self.acc_type} , Phone: {self.phone} 
                \rBalance: {self.banlance}'''

    @staticmethod
    def add(new_info):
        sql = "INSERT INTO customers(name,gender,address,acc_type,phone,balance) VALUES(%s,%s,%s,%s,%s,%s)"
        val = new_info
        cur.execute(sql,val)
        db.commit()

    def get(self):
        return self.customer_info


    def delete(self):
        sql = 'DELETE FROM customers WHERE id=%s'
        val = (self.id,)
        cur.execute(sql,val)
        db.commit()


    def update(self,edit_info):
        sql = f"update customers set name=%s,gender=%s,address=%s,acc_type=%s,phone=%s,balance=%s where id={self.id}"
        val = edit_info
        cur.execute(sql,val)
        db.commit()

    # def update_balance(self,amount):
    #     sql = f"update customers set balance=%s where id={self.id}"
    #     val = (float(self.banlance) + amount,)
    #     cur.execute(sql,val)
    #     db.commit()


    @staticmethod
    def search_customer(search_info):
        sql = "SELECT id FROM customers WHERE "+ search_info[0] + " LIKE '%"+ search_info[1] +"%'"
        cur.execute(sql)
        ids_list = cur.fetchall()
        if ids_list == None:
            return None
        ids = []
        for id in ids_list:
            ids += list(id)
        return ids

def initialize():
    Customer.add(('John Doe','M','Buffalo,NY','S','5022222222',5000))
    Customer.add(('Bela Doe','F','Baker,CA','S','5022222222',1000))
    