import pymysql

timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="mysql-4165eac-project-2138.j.aivencloud.com",
  password="AVNS_VfsUj4yoyP-FZ2wRNfD",
  read_timeout=timeout,
  port=26208,
  user="avnadmin",
  write_timeout=timeout,
)
  
try:
  cursor = connection.cursor()
  cursor.execute("use menu")
  cursor.execute("SHOW TABLES")
  print(cursor.fetchall())
finally:
  connection.close()