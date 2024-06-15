from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import pymysql

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'mysql-4165eac-project-2138.j.aivencloud.com:26208'
# app.config['MYSQL_USER'] = 'avnadmin'
# app.config['MYSQL_PASSWORD'] = 'AVNS_VfsUj4yoyP-FZ2wRNfD'
# app.config['MYSQL_DB'] = 'defaultdb'

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

mysql = MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        password = '123'
        cursor=connection.cursor()
        cursor.execute("USE menu")
        cursor.execute("CALL Login(%s,%s,%s)",(email,name,password))
        connection.commit()
        cursor.close()
        return 'test2'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)