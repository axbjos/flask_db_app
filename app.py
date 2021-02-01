from flask import Flask, render_template
import pymysql
app = Flask(__name__)
class Database:
    def __init__(self):
        host = "172.16.132.131"
        user = "joeaxberg"
        password = "abc123"
        db = "employees"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()
    def list_employees(self):
        self.cur.execute("SELECT first_name, last_name, gender FROM employees LIMIT 50")
        result = self.cur.fetchall()
        return result
@app.route('/')
def employees():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('employees.html', result=res, content_type='application/json')
@app.route('/addemployee')
def addemployee():
    def db_query():
        db = Database()
        emps = db.list_employees()
        return emps
    res = db_query()
    return render_template('addemployee.html', result=res, content_type='application/json')

if __name__ == "__main__":
        app.run(host="0.0.0.0")
