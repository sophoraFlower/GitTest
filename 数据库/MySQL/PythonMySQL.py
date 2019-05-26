import pymysql
import time
 
# 打开数据库连接
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='2017@zhanqiTV', db='shop', charset='utf8mb4')
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据
data = cursor.fetchone()
 
print("Database version : %s " % data)

time.sleep(10)

# 关闭数据库连接
db.close()

