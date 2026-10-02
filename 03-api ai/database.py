import sqlite3
conn=sqlite3.connect("chat.db")
cursor=conn.cursor()
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
      id INTEGER PRIMARY KEY AUTOINCRENMENT,
      question TEST NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
conn.commit()
conn.close()
print("数据库创建成功")
