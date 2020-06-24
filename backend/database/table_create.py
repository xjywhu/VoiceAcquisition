import sqlite3

def createTab(db_name,create_sql,tab_name = None,datas = None):
    con = sqlite3.connect(db_name)
    con.execute(create_sql)
    con.commit()
    if tab_name is not None and datas is not None:
        statement = "INSERT INTO %s VALUES(?,?,?,?)" % tab_name
        #statement中的SQL命令
        con.executemany(statement,datas)
        #将修改保存到数据库
        con.commit()
    con.close()

db_name = 'voice_acquisition'

tab_name = 'User'

create_sql = """CREATE TABLE User
                (uid VARCHAR(50),
                nickName VARCHAR(50),
                wx_number VARCHAR(50),
                age INT);"""

datas = [('000001','Mike','vx_01',15),
        ('000002','Tom','vx_02',18),
        ('000003','Alex','vx_03',25),
        ('000004','Bob','vx_04',31)]

createTab(db_name,create_sql,tab_name,datas)


