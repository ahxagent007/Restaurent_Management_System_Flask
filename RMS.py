from flask import Flask, render_template, request
import pymysql

#db = pymysql.connect("localhost", "root", "", "flask_db")


app = Flask(__name__, template_folder='templates', static_folder='static')

class DatabaseByPyMySQL:
   def __init__(self):
      host = "localhost"
      user = "root"
      password = ""
      db = "flask_db"

      self.conection = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
      self.cursor = self.conection.cursor()

   '''def addSome(self):
      self.cursor.execute("INSERT INTO demo VALUES(" + str(32154) + "," + str(85746) + ");")
      self.conection.commit()
      print("DATA ADDED")

   def getSome(self):
      self.cursor.execute("SELECT * from demo;")
      data = self.cursor.fetchall()
      print(data)'''



@app.route('/')
def index():

   return 'INDEX'


@app.route('/Manager')
def manager_dashboard():
   return render_template('manager.html')

@app.route('/Manager/Sales')
def manager_sales():
   return render_template('manager_sales.html')

@app.route('/Manager/Stock')
def manager_stock():
   return render_template('manager_stock.html')

@app.route('/Manager/EmpAll')
def manager_emp_all():
   return render_template('manager_emp_all.html')

@app.route('/Manager/EmpWork')
def manager_emp_work():
   return "not Found!!"

@app.route('/Manager/Message')
def manager_msg():
   return render_template('manager_msg.html')

@app.route('/Manager/Add/Employee')
def manager_add_emp():
   return render_template('manager_add_emp.html')

@app.route('/Manager/Add/Menu')
def manager_add_menu():
   return render_template('manager_add_menu.html')

@app.route('/Manager/Add/Dish')
def manager_add_dish():
   return render_template('manager_add_dish.html')

@app.route('/Manager/Add/Table')
def manager_add_table():
   return render_template('manager_add_table.html')

@app.route('/Manager/Add/Offers')
def manager_add_offers():
   return render_template('manager_add_offers.html')


@app.route('/Sales')
def sales_dashboard():
   return render_template('salesman.html')

@app.route('/Sales/Order')
def sales_order():
   return render_template('salesman_order.html')

@app.route('/Sales/Invoice')
def sales_invoice():
   return render_template('salesman_invoice.html')




app.debug = True
app.run()
app.run(debug = True)


if __name__ == '__main__':
   app.run()
