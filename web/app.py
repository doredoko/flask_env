from flask import Flask
from flask import render_template
import mysql.connector

app=Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(user='my' password='my', host='flask-db', database='my')
    cur=conn.coursor()
    cur.execute("select * from book")
    books=cur.fetchall()
    cur.close()
    conn.close()
    
    html=render_template('index.html',books=books)
    return html

if __name__ == '__main__':
    app.run(port=5000)