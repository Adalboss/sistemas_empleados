from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='adal5018'
app.config['MYSQL_DATABASE_DB']='empleados'

mysql.init_app(app)

@app.route('/')
def index():
    
    conn=mysql.connect()
    cursor=conn.cursor()
    sql="INSERT INTO empleados (nombre,correo,foto) values ('Fabian','Fabian@exe','fotoFabi.jpg');"
    cursor.execute(sql)
    conn.commit()
    return render_template('empleados/index.html')


if __name__=='__main__':
    app.run(debug=True)