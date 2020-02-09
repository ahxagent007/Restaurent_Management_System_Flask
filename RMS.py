import sys

from flask import Flask, render_template, request
import pymysql
import hashlib

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

   def isEmailExist(self, email):
      self.cursor.execute("SELECT * FROM login WHERE email = \""+email+"\";")
      data = self.cursor.fetchall()
      if(len(data)>0 ):
         return True
      else:
         return False

   def addNewEmployee(self, name, phone, email, address, passwd):

      try:
         # getting the last ID
         self.cursor.execute("SELECT user_id from users;")
         data = self.cursor.fetchall()
         print('data = ',data, flush=True)
         id = data[0]['user_id']

         id = id + 1
         print('user_id == ',str(id), flush=True)

         #Adding User
         sql1 = 'INSERT INTO users(user_id, name, phone_no, email, address, type) VALUES({0},"{1}", "{2}", "{3}", "{4}", "{5}");'.format(id, name, phone, email, address, 'EMP')
         self.cursor.execute(sql1)
         self.conection.commit()

         print(sql1, flush=True)

         passwd = hashlib.md5(passwd.encode())
         #adding Login details
         sql2 = 'INSERT INTO login(user_id,  email, password) VALUES({0},"{1}", "{2}");'.format(id, email, passwd)
         self.cursor.execute(sql2)
         self.conection.commit()

         print(sql2, flush=True)
         return True

      except :
         print('Error occurred on addNewEmployee()', flush=True)
         print('Error = ',str(sys.exc_info()[0]), flush=True)
         return False

   def addMenu(self, menu_name, isAvailable):

      try:

         #Adding Menu
         sql1 = 'INSERT INTO menu(menu_name, isAvailable) VALUES("{0}","{1}");'.format(menu_name, isAvailable)
         self.cursor.execute(sql1)
         self.conection.commit()

         print(sql1, flush=True)

         return True

      except :
         print('Error occurred on addMenu()', flush=True)
         print('Error = ',str(sys.exc_info()[0]), flush=True)
         return False

   def addTable(self, table_no, chair, vacancy):

      try:

         #Adding Table
         sql1 = 'INSERT INTO table(table_no, chair, vacancy) VALUES("{0}",{1}, "{2}");'.format(table_no, chair, vacancy)
         self.cursor.execute(sql1)
         self.conection.commit()

         print(sql1, flush=True)

         return True

      except :
         print('Error occurred on addTable()', flush=True)
         print('Error = ',str(sys.exc_info()[0]), flush=True)
         return False

   def addOffer(self, discount, date_from, date_to):

      try:

         #Addin Menu
         sql1 = 'INSERT INTO offers(discount,date_from, date_to) VALUES({0},"{1}","{2}");'.format(discount, date_from, date_to)
         self.cursor.execute(sql1)
         self.conection.commit()

         print(sql1, flush=True)

         return True

      except :
         print('Error occured on addOffer()', flush=True)
         print('Error = ',str(sys.exc_info()[0]), flush=True)
         return False

   def addDish(self, dishName, dishPrice, dishDes, dishPic, isAvailable):

      try:

         #Adding Dish
         sql1 = 'INSERT INTO dish(dish_name, dish_price, dish_des, dish_pic, isAvailable) VALUES("{0}",{1},"{2}","{3}","{4}");'.format(dishName, dishPrice, dishDes, dishPic,  isAvailable)
         self.cursor.execute(sql1)
         self.conection.commit()

         print(sql1, flush=True)

         return True

      except :
         print('Error occured on addDish()', flush=True)
         print('Error = ',str(sys.exc_info()[0]), flush=True)
         return False

   def getValidateLogin(self, email, passs):
      sql = 'SELECT * from login WHERE email = "{0}";'.format(email)
      self.cursor.execute(sql)
      data = self.cursor.fetchall()

      if len(data)>0:
         print(data)
         id = data[0]['user_id']
         emailed = data[0]['email']
         passed = data[0]['password']

         if email == emailed and passed == hashlib.md5(passs.encode()):
            return id, True
         else:
            return id, False

      else:
         return -1, False

   def getAllEmployee(self):
      sql = 'SELECT * from users WHERE type = "EMP";'
      self.cursor.execute(sql)
      data = self.cursor.fetchall()

      if len(data)>0:
        return data, True

      else:
         return data, False

   def getAllStock(self):
      sql = 'SELECT * from product;'
      self.cursor.execute(sql)
      data = self.cursor.fetchall()

      if len(data)>0:
        return data, True
      else:
         return data, False

   def getRangeOrdersDetails(self, page, range):
      fromm = page * range;
      sql = 'SELECT * FROM flask_db.order LIMIT {0}, {1};'.format(fromm, range)
      sql_all = 'SELECT user_order.order_id, user_order.user_id, user_order.pay_id, order_date, total_bill, VAT,phone_no, email, type, address, name FROM flask_db.order INNER JOIN user_order ON user_order.order_id = flask_db.order.order_id INNER JOIN users ON users.user_id = user_order.user_id LIMIT {0}, {1};'.format(fromm, range)
      self.cursor.execute(sql_all)
      data = self.cursor.fetchall()

      print('getRangeOrdersDetails data type : ',type(data), flush=True)
      print('data : ', str(data), flush=True)

      if len(data)>0:
        return data, True
      else:
         return data, False

   def getAllMsg(self, page, range, uid):
      fromm = page * range;
      sql = 'SELECT * FROM flask_db.message JOIN flask_db.users ON users.user_id = message.from_user WHERE to_user = {0}  LIMIT {1}, {2};'.format(uid, fromm, range)

      self.cursor.execute(sql)
      data = self.cursor.fetchall()

      print('getAllMsg data type : ', type(data), flush=True)
      print('data : ', str(data), flush=True)

      if len(data) > 0:
         return data, True
      else:
         return data, False

@app.route('/')
def index():

   return 'INDEX'



@app.route('/Manager')
def manager_dashboard():

   db = DatabaseByPyMySQL()
   RecentOrders, notEmpty = db.getRangeOrdersDetails(page=0, range=20)

   data = {
      'RecentOrders' : RecentOrders
   }

   return render_template('manager.html', data=data)

@app.route('/Manager/Sales')
def manager_sales():
   db = DatabaseByPyMySQL()
   RecentOrders, notEmpty = db.getRangeOrdersDetails(page=0, range=20)

   data = {
      'RecentOrders': RecentOrders
   }

   return render_template('manager_sales.html', data=data)

@app.route('/Manager/Stock')
def manager_stock():
   return render_template('manager_stock.html')

@app.route('/Manager/EmpAll')
def manager_emp_all():

   db = DatabaseByPyMySQL()

   AllEmployee, notEmpty = db.getAllEmployee()

   data = {
      'AllEmp': AllEmployee
   }

   return render_template('manager_emp_all.html', data=data)

@app.route('/Manager/EmpWork')
def manager_emp_work():
   return "not Found!!"

@app.route('/Manager/Message')
def manager_msg():

   db = DatabaseByPyMySQL()
   all_msg, isEmpty = db.getAllMsg(uid=1,page=0, range=10)
   data = {
      'msg': all_msg
   }
   return render_template('manager_msg.html', data=data)



@app.route('/Manager/Add/Menu')
def manager_add_menu():
   return render_template('manager_add_menu.html')

@app.route('/Manager/Add/MenuForm', methods = ['POST'])
def manager_add_menu_form():
   if request.method == 'POST':
      MenuName = request.form['MenuName']
      availability = request.form['Availability']
      log = MenuName, availability
      print(log, flush=True)

      db = DatabaseByPyMySQL()

      status = db.addMenu(menu_name=MenuName, isAvailable=availability)

      if(status):
         return render_template('manager_add_menu.html', msg='success')
      else:
         return render_template('manager_add_menu.html', msg = 'failed')



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


@app.route('/Manager/Add/Employee')
def manager_add_emp():
   return render_template('manager_add_emp.html')

@app.route('/Manager/Add/EmployeeAdd',methods = ['POST'])
def manager_add_emp_form():
   if request.method == 'POST':
      EmployeeName = request.form['EmployeeName']
      EmployeePhoneNumber = request.form['EmployeePhoneNumber']
      EmployeeAddress = request.form['EmployeeAddress']
      EmployeeEmail = request.form['EmployeeEmail']
      EmployeePass = request.form['EmployeePass01']

      log = EmployeeName +" "+EmployeePhoneNumber+" "+EmployeeAddress+" "+EmployeeEmail+" "+EmployeePass
      print(log, flush=True)

      db = DatabaseByPyMySQL()

      if db.isEmailExist(EmployeeEmail):
         print(" USER EXIST ", flush=True)
         return render_template('manager_add_emp.html', msg='user_exist')
      else:
         print(" USER IS NEW ", flush=True)
         feedback = db.addNewEmployee(name=EmployeeName, email=EmployeeEmail, address=EmployeeAddress, phone=EmployeePhoneNumber, passwd=EmployeePass)

         if feedback:
            return render_template('manager_add_emp.html', msg='success')
         else:
            return render_template('manager_add_emp.html', msg='failed')













app.debug = True
app.run()
app.run(debug = True)


if __name__ == '__main__':
   app.run()
