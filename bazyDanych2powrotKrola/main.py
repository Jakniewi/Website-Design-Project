from website import createApp
from flask_mysqldb import MySQL

app = createApp()

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)