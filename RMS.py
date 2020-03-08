import datetime
import os
import sys

import app as app
from flask import Flask, render_template, request, flash, url_for, send_from_directory, jsonify, session, abort, redirect
import pymysql
import hashlib
import time

from werkzeug.utils import secure_filename
# from werkzeug.wrappers import json
import json

UPLOAD_FOLDER = 'static/UPLOADS/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'SECRETKEYXIAN'

# Lambda Function
current_milli_time = lambda: int(round(time.time() * 1000))

class kitchenOrder:
    def __init__(self, OrderDetails, DishList):
        self.OrderDetails = OrderDetails
        self.DishList = DishList

class DatabaseByPyMySQL:
    def __init__(self):
        host = "localhost"
        user = "root"
        password = ""
        db = "flask_db"

        self.conection = pymysql.connect(host=host, user=user, password=password, db=db,
                                         cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conection.cursor()

    '''def addSome(self):
      self.cursor.execute("INSERT INTO demo VALUES(" + str(32154) + "," + str(85746) + ");")
      self.conection.commit()
      print("DATA ADDED")

   def getSome(self):
      self.cursor.execute("SELECT * from demo;")
      data = self.cursor.fetchall()
      print(data)'''

    def isEmailExist(self, email = "xxx", phone = "xxx"):
        self.cursor.execute('SELECT * FROM login WHERE email = "{0}" or phone_no = "{1}";'.format(email, phone))
        data = self.cursor.fetchall()
        if (len(data) > 0):
            return True
        else:
            return False

    def addNewUser(self, name, phone, email, address, passwd, userType):

        try:
            # getting the last ID
            self.cursor.execute("SELECT user_id from users ORDER BY user_id DESC LIMIT 1;")
            data = self.cursor.fetchall()
            print('data = ', data, flush=True)
            id = data[0]['user_id']

            id = id + 1
            print('user_id == ', str(id), flush=True)

            # Adding User
            sql1 = 'INSERT INTO users(user_id, name, phone_no, email, address, type) VALUES({0},"{1}", "{2}", "{3}", "{4}", "{5}");'.format(
                id, name, phone, email, address, userType)
            self.cursor.execute(sql1)
            self.conection.commit()

            print(sql1, flush=True)

            passwd = hashlib.md5(passwd.encode("utf").hexdigest().hexdigest())
            # adding Login details
            sql2 = 'INSERT INTO login(user_id,  email, password, phone_no) VALUES({0},"{1}", "{2}","{3}");'.format(id, email, passwd, phone)
            self.cursor.execute(sql2)
            self.conection.commit()

            print(sql2, flush=True)
            return True

        except:
            print('Error occurred on addNewUser()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def addMenu(self, menu_name, isAvailable):
        try:
            # Adding Menu
            sql1 = 'INSERT INTO menu(menu_name, isAvailable) VALUES("{0}","{1}");'.format(menu_name, isAvailable)
            self.cursor.execute(sql1)
            self.conection.commit()

            print(sql1, flush=True)

            return True

        except:
            print('Error occurred on addMenu()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def addTable(self, table_no, chair, vacancy):

        try:

            # Adding Table
            sql1 = 'INSERT INTO flask_db.table(table_no, chair, vacancy) VALUES("{0}",{1}, "{2}");'.format(table_no,
                                                                                                           chair,
                                                                                                           vacancy)
            self.cursor.execute(sql1)
            self.conection.commit()

            print(sql1, flush=True)

            return True

        except:
            print('Error occurred on addTable()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def addOffer(self, offerName, discount, date_from, date_to):

        try:

            # Addin Menu
            sql1 = 'INSERT INTO offers(offer_name, discount,date_from, date_to) VALUES("{3}",{0},"{1}","{2}");'.format(
                discount, date_from, date_to, offerName)
            self.cursor.execute(sql1)
            self.conection.commit()

            print(sql1, flush=True)

            return True

        except:
            print('Error occured on addOffer()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def addDish(self, dishName, dishPrice, dishDes, dishPic, isAvailable, menu_id):

        try:

            # Adding Dish
            sql1 = 'INSERT INTO dish(dish_name, dish_price, dish_des, dish_pic, isAvailable) VALUES("{0}",{1},"{2}","{3}","{4}");'.format(
                dishName, dishPrice, dishDes, dishPic, isAvailable)
            self.cursor.execute(sql1)
            self.conection.commit()

            print(sql1, flush=True)

            # getting the last id
            sql = 'SELECT dish_id from dish order by dish_id DESC LIMIT 1;'
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data, flush=True)
            dish_id = int(data[0]['dish_id'])
            print(str(dish_id), flush=True)

            # Adding Dish_Menu
            sql2 = 'INSERT INTO dish_menu(dish_id, menu_id) VALUES({0},{1});'.format(dish_id, menu_id)
            self.cursor.execute(sql2)
            self.conection.commit()

            return True

        except:
            print('Error occured on addDish()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def addProduct(self, productName, productDes, productQuantity, productPic, productCat):

        try:
            # Adding Dish
            sql = 'INSERT INTO products(product_name, product_des, product_quantity, product_pic, product_cat) VALUES("{0}","{1}",{2},"{3}","{4}");'.format(
                productName, productDes, productQuantity, productPic, productCat)
            self.cursor.execute(sql)
            self.conection.commit()

            print(sql, flush=True)

            return True

        except:
            print('Error occured on addProduct()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def getValidateLogin(self, email, passs):
        sql = 'SELECT * from login WHERE email = "{0}";'.format(email)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        if len(data) > 0:
            print(data)
            id = data[0]['user_id']
            emailed = data[0]['email']
            passed = data[0]['password']

            if email == emailed and passed == hashlib.md5(passs.encode("utf").hexdigest()):
                return id, True
            else:
                return id, False

        else:
            return -1, False

    def getAllEmployee(self):
        sql = 'SELECT * from users WHERE type = "EMP";'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        if len(data) > 0:
            return data, True

        else:
            return data, False


    def getUserByID(self,ID):
        sql = 'SELECT * from users WHERE user_id = "{}";'.format(ID)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        if len(data) > 0:
            return data[0], True

        else:
            return data[0], False

    def getAllStock(self):
        sql = 'SELECT * from product;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def getRangeOrdersDetails(self, page, range):
        fromm = page * range;
        sql = 'SELECT * FROM flask_db.order LIMIT {0}, {1};'.format(fromm, range)
        sql_all = 'SELECT order_id, users.user_id, pay_id, order_date, total_bill, VAT, phone_no, email, type, address, name FROM flask_db.order INNER JOIN users ON users.user_id = flask_db.order.user_id LIMIT {0}, {1};'.format(
            fromm, range)
        self.cursor.execute(sql_all)
        data = self.cursor.fetchall()

        print('getRangeOrdersDetails data type : ', type(data), flush=True)
        print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def getAllMsg(self, page, range, uid):
        fromm = page * range;
        sql = 'SELECT * FROM flask_db.message JOIN flask_db.users ON users.user_id = message.from_user WHERE to_user = {0}  LIMIT {1}, {2};'.format(
            uid, fromm, range)

        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        print('getAllMsg data type : ', type(data), flush=True)
        print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def getAllMenu(self):
        sql = 'SELECT * FROM flask_db.menu ;'

        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        print('getAllMenu data type : ', type(data), flush=True)
        print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def getAllStock(self):
        sql = 'SELECT * FROM flask_db.products ;'

        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        print('getAllStock data type : ', type(data), flush=True)
        print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def getDishByName(self, dish_name):
        sql = 'SELECT * FROM flask_db.dish WHERE dish_name LIKE "%{0}%";'.format(dish_name)

        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        print('getDishByName data type : ', type(data), flush=True)
        print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def getLastId(self, table):

        if table == 'order':
            sql = 'SELECT order_id FROM flask_db.order ORDER BY order_id DESC LIMIT 1;'
        elif table == 'users':
            sql = 'SELECT user_id FROM flask_db.users ORDER BY user_id DESC LIMIT 1;'

        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        print('getLastId data type : ', type(data), flush=True)
        print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def addOrder(self, order):
        try:

            cus, isext = self.isCustomerExist(order['number'])

            if isext:
                print("CUSTOMER EXIST", flush=True)

                currentDT = datetime.datetime.now()
                # Adding Order
                sql = 'INSERT INTO flask_db.order(total_bill, order_date, user_id) VALUES({0}, "{1}", {2});'.format(
                    order['totalBill'], currentDT.strftime("%d-%m-%Y %H:%M:%S"), cus[0]['user_id'])
                self.cursor.execute(sql)
                self.conection.commit()
                print(sql, flush=True)

            else:
                print("NEW CUSTOMER", flush=True)
                self.addNewUser(name=order['name'], phone=order['number'], email=order['email'],
                                address=order['address'], passwd=order['number'], userType='CUS')

                cus_id, isId = self.getLastId('users')

                currentDT = datetime.datetime.now()
                # Adding Order
                sql = 'INSERT INTO flask_db.order(total_bill, order_date, user_id) VALUES({0}, "{1}", {2});'.format(
                    order['totalBill'], currentDT.strftime("%d-%m-%Y %H:%M:%S"), cus_id[0]['user_id'])
                self.cursor.execute(sql)
                self.conection.commit()
                print(sql, flush=True)

            order_id, isId = self.getLastId('order')
            print('ORDER ID = ' + str(order_id), flush=True)

            for odr in order['orders']:
                sqll = 'INSERT INTO flask_db.ordered_dishes(order_id, dish_id, order_comment) VALUES({0}, {1}, "{2}");'.format(
                    order_id[0]['order_id'], odr['id'], odr['comment'])
                self.cursor.execute(sqll)
                self.conection.commit()

            return True

        except:
            print('Error occurred on addOrder()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def isCustomerExist(self, mobileNumber):

        sql = 'SELECT * FROM flask_db.users WHERE phone_no = "{0}";'.format(mobileNumber)

        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        print('isCustomerExist data type : ', type(data), flush=True)
        print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def updateProductQunatity(self, p_id, new_quan):
        try:
            sql = 'UPDATE flask_db.products SET product_quantity = {0} WHERE product_id = {1};'.format(new_quan, p_id)
            self.cursor.execute(sql)
            self.conection.commit()
            print(sql, flush=True)

            return True

        except:
            print('Error occurred on updateProductQunatity()', flush=True)
            print('Error = ', str(sys.exc_info()[0]), flush=True)
            return False

    def getDishesByOrderId(self, order_id):

        sql = 'SELECT * FROM dish JOIN ordered_dishes ON ordered_dishes.dish_id = dish.dish_id WHERE ordered_dishes.order_id = {0}'.format(order_id)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()

        #print('getDishesByOrderId data type : ', type(data), flush=True)
        #print('data : ', str(data), flush=True)

        if len(data) > 0:
            return data, True
        else:
            return data, False

    def getRangeKitchenOrders(self, page, range):
        fromm = page * range;

        sql_all = 'SELECT * FROM flask_db.order ORDER BY flask_db.order.order_id DESC LIMIT {0}, {1};'.format(fromm, range)
        self.cursor.execute(sql_all)
        data = self.cursor.fetchall()

        allData = []

        for d in data:
            #print(d['order_id'], flush=True)

            de, f = self.getDishesByOrderId(d['order_id'])
            allData.append(kitchenOrder(d,de))

        print('getRangeKitchenOrders allData type : ', type(allData), flush=True)
        print('allData : ', str(allData), flush=True)

        if len(allData) > 0:
            return allData, True
        else:
            return allData, False

    ########## NEW CODES

    def Login(self, email, phone, password):
        if(self.isEmailExist(email=email, phone=phone)):

            self.cursor.execute('SELECT * FROM login WHERE email = "{0}" OR phone_no = "{1}";'.format(email,phone))
            print('Login SQL : '+'SELECT * FROM login WHERE email = "{0}" OR phone_no = "{1}";'.format(email,phone),flush=True)
            data = self.cursor.fetchall()

            if (len(data) > 0):
                serverPass = data[0]['password'];
                md5PassConverted = str(hashlib.md5(password.encode("utf")).hexdigest())
                print(data, flush=True)
                print(serverPass+' SERVER PASS', flush=True)
                print(md5PassConverted+' MD5 PASS', flush=True)

                if md5PassConverted == serverPass :

                    return True, data[0]['user_id']
                else:
                    return False, -1
            else:
                return False, -1
        else:
            return False, -1


@app.route('/')
def index():
    return render_template('dummy_index.html')

@app.route('/Manager')
def manager_dashboard():
    if session.get('id') is not None and session.get('type') == 'MNG':
        db = DatabaseByPyMySQL()
        RecentOrders, notEmpty = db.getRangeOrdersDetails(page=0, range=20)

        data = {
            'RecentOrders': RecentOrders
        }

        return render_template('manager.html', data=data)

    else:
        return redirect(url_for('login'))



@app.route('/Manager/Sales')
def manager_sales():
    if session.get('id') is not None and session.get('type') == 'MNG':
        db = DatabaseByPyMySQL()
        RecentOrders, notEmpty = db.getRangeOrdersDetails(page=0, range=20)

        data = {
            'RecentOrders': RecentOrders
        }

        return render_template('manager_sales.html', data=data)


    else:
        return redirect(url_for('login'))


@app.route('/Manager/Stock')
def manager_stock():
    if session.get('id') is not None and session.get('type') == 'MNG':
        db = DatabaseByPyMySQL()
        allStock, isbool = db.getAllStock();

        data = {
            'stock': allStock
        }

        return render_template('manager_stock.html', data=data)

    else:
        return redirect(url_for('login'))



@app.route('/Manager/EmpAll')
def manager_emp_all():
    if session.get('id') is not None and session.get('type') == 'MNG':
        db = DatabaseByPyMySQL()

        AllEmployee, notEmpty = db.getAllEmployee()

        data = {
            'AllEmp': AllEmployee
        }

        return render_template('manager_emp_all.html', data=data)

    else:
        return redirect(url_for('login'))



@app.route('/Manager/EmpWork')
def manager_emp_work():
    if session.get('id') is not None and session.get('type') == 'MNG':
        return "not Found!!"
    else:
        return redirect(url_for('login'))


@app.route('/Manager/Message')
def manager_msg():
    if session.get('id') is not None and session.get('type') == 'MNG':
        db = DatabaseByPyMySQL()
        all_msg, isEmpty = db.getAllMsg(uid=1, page=0, range=10)
        data = {
            'msg': all_msg
        }
        return render_template('manager_msg.html', data=data)

    else:
        return redirect(url_for('login'))




@app.route('/Manager/Add/Menu')
def manager_add_menu():
    if session.get('id') is not None and session.get('type') == 'MNG':
        return render_template('manager_add_menu.html')

    else:
        return redirect(url_for('login'))

@app.route('/Manager/Add/MenuForm', methods=['POST'])
def manager_add_menu_form():
    if request.method == 'POST':
        MenuName = request.form['MenuName']
        availability = request.form['Availability']
        log = MenuName, availability
        print(log, flush=True)

        db = DatabaseByPyMySQL()

        status = db.addMenu(menu_name=MenuName, isAvailable=availability)

        if (status):
            return render_template('manager_add_menu.html', msg='success')
        else:
            return render_template('manager_add_menu.html', msg='failed')


@app.route('/Manager/Add/Dish', methods=['POST', 'GET'])
def manager_add_dish():
    if session.get('id') is not None and session.get('type') == 'MNG':
        db = DatabaseByPyMySQL()
        menu, booll = db.getAllMenu()
        data = {
            'menu': menu
        }
        if request.method == 'POST':
            # check if the post request has the file part
            if 'dishPic' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['dishPic']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = str(current_milli_time()) + filename[-4:]
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                DishName = request.form['DishName']
                DishDes = request.form['DishDes']
                DishPrice = request.form['DishPrice']
                isAvailable = request.form['isAvailable']
                DishMenu = request.form['DishMenu']

                db = DatabaseByPyMySQL()
                status = db.addDish(dishName=DishName, dishDes=DishDes, dishPrice=DishPrice, dishPic=filename,
                                    isAvailable=isAvailable, menu_id=DishMenu)

                print(str(status), flush=True)
                return render_template('manager_add_dish.html', msg=str(status), data=data)

        return render_template('manager_add_dish.html', data=data)

    else:
        return redirect(url_for('login'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/Manager/Add/Product', methods=['POST', 'GET'])
def manager_add_product():
    if session.get('id') is not None and session.get('type') == 'MNG':
        if request.method == 'POST':
            # check if the post request has the file part
            if 'ProductPic' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['ProductPic']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = str(current_milli_time()) + filename[-4:]
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                ProductName = request.form['ProductName']
                ProductDes = request.form['ProductDes']
                ProductQuantity = request.form['ProductQuantity']
                ProductCategory = request.form['ProductCategory']

                db = DatabaseByPyMySQL()
                status = db.addProduct(productName=ProductName, productDes=ProductDes, productQuantity=ProductQuantity,
                                       productCat=ProductCategory, productPic=filename)

                print(str(status), flush=True)
                return render_template('manager_add_product.html', msg=str(status))

        return render_template('manager_add_product.html')

    else:
        return redirect(url_for('login'))


@app.route('/Manager/Add/Table', methods=['POST', 'GET'])
def manager_add_table():
    if session.get('id') is not None and session.get('type') == 'MNG':
        if request.method == 'POST':
            TableNo = request.form['TableNo']
            Chair = request.form['NumberChair']

            db = DatabaseByPyMySQL()

            status = db.addTable(table_no=TableNo, chair=Chair, vacancy='YES')

            if (status):
                return render_template('manager_add_table.html', msg='success')
            else:
                return render_template('manager_add_table.html', msg='failed')

        return render_template('manager_add_table.html')

    else:
        return redirect(url_for('login'))


@app.route('/Manager/Add/Offers', methods=['POST', 'GET'])
def manager_add_offers():
    if session.get('id') is not None and session.get('type') == 'MNG':
        if request.method == 'POST':
            OfferName = request.form['OfferName']
            OfferDis = request.form['OfferDis']
            Offer_from = request.form['Offer_from']
            Offer_to = request.form['Offer_to']

            db = DatabaseByPyMySQL()

            status = db.addOffer(offerName=OfferName, discount=OfferDis, date_from=Offer_from, date_to=Offer_to)

            if (status):
                return render_template('manager_add_offers.html', msg='success')
            else:
                return render_template('manager_add_offers.html', msg='failed')

        return render_template('manager_add_offers.html')


    else:
        return redirect(url_for('login'))


@app.route('/Manager/Add/Employee')
def manager_add_emp():
    if session.get('id') is not None and session.get('type') == 'MNG':
        return render_template('manager_add_emp.html')
    else:
        return redirect(url_for('login'))


@app.route('/Manager/Add/EmployeeAdd', methods=['POST'])
def manager_add_emp_form():
    if request.method == 'POST':
        EmployeeName = request.form['EmployeeName']
        EmployeePhoneNumber = request.form['EmployeePhoneNumber']
        EmployeeAddress = request.form['EmployeeAddress']
        EmployeeEmail = request.form['EmployeeEmail']
        EmployeePass = request.form['EmployeePass01']

        log = EmployeeName + " " + EmployeePhoneNumber + " " + EmployeeAddress + " " + EmployeeEmail + " " + EmployeePass
        print(log, flush=True)

        db = DatabaseByPyMySQL()

        if db.isEmailExist(EmployeeEmail):
            print(" USER EXIST ", flush=True)
            return render_template('manager_add_emp.html', msg='user_exist')
        else:
            print(" USER IS NEW ", flush=True)
            feedback = db.addNewUser(name=EmployeeName, email=EmployeeEmail, address=EmployeeAddress,
                                     phone=EmployeePhoneNumber, passwd=EmployeePass, userType='EMP')

            if feedback:
                return render_template('manager_add_emp.html', msg='success')
            else:
                return render_template('manager_add_emp.html', msg='failed')


@app.route('/Sales')
def sales_dashboard():
    if session.get('id') is not None and session.get('type') == 'EMP':
        db = DatabaseByPyMySQL()
        RecentOrders, notEmpty = db.getRangeOrdersDetails(page=0, range=20)

        data = {
            'RecentOrders': RecentOrders
        }

        return render_template('salesman.html', data=data)

    else:
        return redirect(url_for('login'))


@app.route('/Sales/Order', methods=['GET', 'POST'])
def sales_order():
    if session.get('id') is not None and session.get('type') == 'EMP':
        return render_template('salesman_order.html')

    else:
        return redirect(url_for('login'))


@app.route('/Sales/Order/LiveSearch', methods=['POST', 'GET'])
def sales_order_live_search():
    searchText = request.form.get('search_text')

    if len(searchText) > 0:
        db = DatabaseByPyMySQL()
        search_result, found = db.getDishByName(searchText)
        if found:
            print('FOUND DISHES =  ' + str(len(search_result)), flush=True)
            return jsonify(search_result)
        else:
            print('NOTTT FOUND ANY DISH!! ', flush=True)
            return jsonify("")
    else:
        print('NOTTT FOUND ANY DISH!! ', flush=True)
        return jsonify("")


@app.route('/Sales/Order/Done', methods=['POST'])
def order_Done():
    if request.method == 'POST':
        order_list_json = request.json

        print(type(order_list_json), flush=True)

        print(order_list_json, flush=True)

        db = DatabaseByPyMySQL()
        db.addOrder(order_list_json)

    return render_template('salesman_invoice.html')


@app.route('/Sales/Stock', methods=['POST', 'GET'])
def sales_stock():

    if session.get('id') is not None and session.get('type') == 'EMP':
        state = ''

        db = DatabaseByPyMySQL()
        allStock, isbool = db.getAllStock();

        data = {
            'stock': allStock
        }

        if request.method == 'POST':
            id = request.form['updateBTN']
            q = request.form['input' + id]

            print('id ' + id + ' Q ' + str(q), flush=True)

            state = db.updateProductQunatity(new_quan=q, p_id=id)

            if state:
                allStock, isbool = db.getAllStock();

                data = {
                    'stock': allStock
                }

        return render_template('salesman_stock.html', data=data, msg=str(state))

    else:
        return redirect(url_for('login'))


@app.route("/search", methods=['POST'])
def search():

    search_text = request.args['search_text']  # get the text to search for
    # create an array with the elements of BRAZIL_STATES that contains the string
    # the case is ignored
    db = DatabaseByPyMySQL()
    result, found = db.getDishByName(search_text)
    # return as JSON
    return json.dumps({"results": result})


@app.route('/Sales/Invoice')
def sales_invoice():

    if session.get('id') is not None and session.get('type') == 'EMP':
        db = DatabaseByPyMySQL()
        RecentOrders, notEmpty = db.getRangeOrdersDetails(page=0, range=50)

        data = {
            'RecentOrders': RecentOrders
        }

        return render_template('salesman_invoice.html', data=data)
    else:
        return redirect(url_for('login'))


@app.route('/Kitchen', methods=['GET'])
def kitchen():
    db = DatabaseByPyMySQL()
    kitchenOrders, isbool = db.getRangeKitchenOrders(0,10)

    for k in kitchenOrders:
        print('k.OrderDetails', flush=True)
        print(k.OrderDetails, flush=True)
        for d in k.DishList:
            print('k.DishList', flush=True)
            print(d, flush=True)


    return render_template('kitchen.html', data = kitchenOrders)

@app.route('/Login')
def login():

    if session.get('id') is not None:
        if session['type'] == 'EMP':
            print('EMP FOUND !!', flush=True)
            return redirect(url_for('sales_dashboard'))

        elif session['type'] == 'MNG':
            print('MNG FOUND !!', flush=True)
            return redirect(url_for('manager_dashboard'))

        elif session['type'] == 'CUS':
            print('CUS FOUND !!', flush=True)
            return redirect(url_for('customer_dashboard'))

        else:
            abort(401)
    else:
        return render_template('login.html')

@app.route('/Login', methods=['POST'])
def login_request():
    if request.method == 'POST':
        EmailOrPhone = request.form['emailOrPhone']
        Password = request.form['pass']

        print(EmailOrPhone+' '+Password, flush=True)

        db = DatabaseByPyMySQL()

        status, user_id = db.Login(email=EmailOrPhone, phone=EmailOrPhone, password=Password)

        if(status):
            user = db.getUserByID(user_id)

            session['id'] = user[0]['user_id']
            session['phone'] = user[0]['phone_no']
            session['mail'] = user[0]['email']
            session['type'] = user[0]['type']
            session['address'] = user[0]['address']
            session['name'] = user[0]['name']

            if session['type'] == 'EMP':
                print('EMP FOUND !!', flush=True)
                return redirect(url_for('sales_dashboard'))

            elif session['type'] == 'MNG':
                print('MNG FOUND !!', flush=True)
                return redirect(url_for('manager_dashboard'))

            elif session['type'] == 'CUS':
                print('CUS FOUND !!', flush=True)
                return redirect(url_for('customer_dashboard'))

            else:
                abort(401)

        else:
            print(status, flush=True)


    return render_template('login.html')

@app.route('/Logout')
def logout():
    session.pop('id', None)
    session.pop('phone', None)
    session.pop('mail', None)
    session.pop('type', None)
    session.pop('address', None)
    session.pop('name', None)

    return redirect(url_for('login'))


@app.route('/Customer')
def customer_dashboard():
    return 'PAGE NOT FOUND'


app.debug = True
app.run()
app.run(debug=True)

if __name__ == '__main__':
    app.run()
