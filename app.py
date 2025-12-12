from flask import Flask, render_template, request  # pyright: ignore[reportMissingImports]
import sqlite3
import datetime

app = Flask(__name__)

flag = 1

@app.route("/", methods={"GET", "POST"})
def index():
    global flag
    flag = 1
    return(render_template("index.html"))

@app.route("/main", methods={"GET", "POST"})
def main():
    global flag

    if flag == 1:
        name = request.form.get("q")
        timestamp = datetime.datetime.now()
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute('INSERT INTO user (name, timestamp) VALUES (?, ?)', (name, timestamp))
        conn.commit()
        c.close()
        conn.close()
        flag = 0
    return(render_template("main.html"))    

@app.route("/paynow", methods={"GET", "POST"})
def paynow():
    return(render_template("paynow.html"))    

@app.route("/deposit", methods={"GET", "POST"})
def deposit():
    return(render_template("deposit.html"))    

@app.route("/userlog", methods={"GET", "POST"})
def userlog():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user')
    r = ""
    for row in c:
        r = r + str(row)
    c.close()
    conn.close()
    return(render_template("userlog.html",r=r)) 

@app.route("/deleteuserlog", methods={"GET", "POST"})
def deleteuserlog():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute('DELETE FROM user')
    conn.commit()
    c.close()
    conn.close()
    return(render_template("deleteuserlog.html")) 

if __name__ == "__main__":
    app.run()


