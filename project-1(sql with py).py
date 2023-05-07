import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Myselfs@1')
print(mydb.connection_id)
a=mydb.cursor()
a.execute('create database Inventory_Management')
a.execute('use Inventory_Management')
# Create the 'manufacture' table
a.execute('CREATE TABLE manufacture (manufacture_id int  not null PRIMARY KEY, item_name VARCHAR(20),company varchar(20),item_color varchar(20) not null,quantity int not null ,defective_items  int not null)')

# Create the 'goods' table
a.execute('CREATE TABLE goods (goods_id int not null PRIMARY KEY, manufacture_id INTEGER, manufacture_date DATE,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id))')

# Create the 'purchase' table
a.execute('CREATE TABLE purchase (purchase_id int not null primary key,  store_name varchar(20) not null,purchase_amount int not null, purchase_date date not null)')

# Create the 'sale' table
a.execute('CREATE TABLE sale (sale_id int primary key,store_name VARCHAR(30) not null,sale_date DATE,goods_id int not null, profit_margin FLOAT not null,FOREIGN KEY(goods_id) REFERENCES goods(goods_id))')

e1='insert into manufacture(manufacture_id ,item_name ,company,item_color ,quantity ,defective_items) values (%s,%s,%s,%s,%s,%s)'
entries1 = (1, 'wooden chair','GARUD ENTERPRISES' ,'brown', 100, 0), (3, 'wooden table','SS EXPORT' 'brown', 50, 1),(2, 'red toy','F3 TOYS','red', 200, 0),(4,'shirt','ADIDAS','black',300,1)
a.executemany(e1,entries1)
mydb.commit()
#Insert multiple entries to the 'goods' table
e2='insert into goods(goods_id , manufacture_id , manufacture_date)values (%s,%s,%s)'
entries2 = (1, 1, '2023-04-20'),(2, 1, '2023-04-22'),(3, 2, '2023-04-25'),(4, 3, '2023-04-26')
a.executemany(e2,entries2)
mydb.commit()
# Insert multiple entries to the 'purchase' table
e3='insert into purchase(purchase_id , store_name,purchase_amount,purchase_date)values(%s,%s,%s,%s)'
entries3 = (1, 'ORay', 500, '2023-04-21'), (2, 'MyKids', 1000, '2023-04-22'),(3, 'OnlineMart', 750, '2023-04-23')
a.executemany(e3,entries3)
mydb.commit()
# Insert multiple entries to the 'sale' table
e4='INSERT INTO sale(sale_id ,store_name ,sale_date,goods_id , profit_margin )values(%s,%s,%s,%s,%s)'
entries4 = (1, 'MyCare', '2023-04-01', 1, 100),(2, 'ORay', '2023-04-03', 2, 50),(3, 'MyKids', '2023-04-05', 3, 75),(4, 'OnlineMart', '2023-04-06', 4, 80)
a.executemany(e4,entries4)
mydb.commit()

#Queries
s='DELETE FROM purchase WHERE item_name = "shirt" AND purchase_date = "2023-04-01" AND store_name = "ORay"'
a.execute(s)
mydb.commit()


t='UPDATE manufacture SET quantity = 500 WHERE item_color = "red" AND manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM sale WHERE store_name = "MyKids")'
a.execute(t)
mydb.commit()


u='SELECT * FROM  goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE item_name = "wooden chair" AND manufacture_date< "2023-05-01"'
a.execute(u)
rows=a.fetchall()
for i in rows:
    print(i)
mydb.commit()

v='SELECT sale.profit_margin FROM sale JOIN goods ON sale.goods_id = goods.goods_id JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.purchase_id = purchase.purchase_id WHERE item_name = "wooden table" AND store_name = "MyCare",company = "SS Export"'
a.execute(v)
row = a.fetchone()
print(row[0])
mydb.commit()