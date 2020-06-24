import sqlite3

#使用‘:memory:’在内存中创建了一个数据库，创建了连接对象con来代表数据库
con = sqlite3.connect('voice_acquisition')

# query = """CREATE TABLE User
#             (uid VARCHAR(50),
#             nickName VARCHAR(50),
#             wx_number VARCHAR(50),
#             age INT);"""
#
# #使用连接对象的execute()方法执行query中的SQL命令
# con.execute(query)
#
# #使用连接对象的commit()方法将修改提交（保存）到数据库
# con.commit()
#
# data = [('000001','Mike','vx_01',15),
#         ('000002','Tom','vx_02',18),
#         ('000003','Alex','vx_03',25),
#         ('000004','Bob','vx_04',31)]
#
# #将插入语句赋给变量statement，？是占位符
# statement = "INSERT INTO User VALUES(?,?,?,?)"
#
# #因为有四个占位符，这里就需要提供一个包含4个值的元组，executemany()方法为data中的每个数据元组执行
# #statement中的SQL命令，这里执行了四次insert命令
# con.executemany(statement,data)
#
# #将修改保存到数据库
# con.commit()

#查询User表，并将命令结果赋值给一个光标对象cursor，光标对象有execute、executemany、fetchone、
#fetchmany和fetchall方法
cursor = con.execute("SELECT * FROM User")

#返回结果集中的所有行
rows = cursor.fetchall()
print(rows)
print('………………')
#查询结果中行的数量
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('………………')
print('Number of rows: %d' % (row_counter))