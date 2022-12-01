from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jewellery'
mysql = MySQL(app)
app.secret_key = 'MY_SECRET_KEY'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
@app.route('/index')
def index():
   return render_template('./logins.html')

@app.route('/loginAsAdmin')
def asAdmin():
   return render_template('./loginAsAdmin.html')
 
@app.route('/loginAsDeliveryGuy')
def asDeliveryGuy():
   return render_template('./loginAsDeliveryGuy.html')

@app.route('/home')
def home_page():
   if session.get('username'):
      cursor = mysql.connection.cursor()
      cursor.execute('''SELECT * FROM inventory ''')
      query_result = cursor.fetchall()
      return render_template('./accounts/home.html', inventory=query_result, user=session['username'])
   else:
      cursor = mysql.connection.cursor()
      cursor.execute('''SELECT * FROM inventory ''')
      query_result = cursor.fetchall()
      return render_template('./accounts/home.html', inventory=query_result)

@app.route('/administration')
def administration():
   if session.get('username'):
      cursor = mysql.connection.cursor()
      cursor.execute('''SELECT * FROM inventory ''')
      query_result = cursor.fetchall()
      return render_template('./adminPage.html', items=query_result, user=session['username'])
   else:
      return render_template('./loginAsAdmin.html')

@app.route('/delivery')
def delivery():
   if session.get('username'):
      cursor = mysql.connection.cursor()
      st = "pending"
      cursor.execute('''SELECT * FROM history WHERE status=%s''', (st,))
      query_result = cursor.fetchall()
      return render_template('./delivery.html', items=query_result, user=session['username'])
   else:
      return render_template('./delivery.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup_page():
   if request.method == 'GET':
      if session.get('username'):
         return redirect(url_for('home_page'))
      else:
         return render_template('./accounts/signup.html')
   if request.method == 'POST':
      try:
         email = request.form['email']
         password = request.form['password']
         password = generate_password_hash(password)
         if not email.strip() or not password.strip():
            return render_template('./accounts/signup.html', message='Email or password is missing!')
         cursor = mysql.connection.cursor()
         my_query = (
             '''INSERT INTO login (username, password) VALUES (%s, %s)''')
         credentials = (email, password)
         cursor.execute(my_query, credentials)
         mysql.connection.commit()
         my_query = (
             '''INSERT INTO profile (loginid) VALUES (%s)''')
         credentials = (email,)
         cursor.execute(my_query, credentials)
         mysql.connection.commit()
         cursor.close()
         session['username'] = email
         return redirect(url_for('home_page'))
      except:
         return render_template('./accounts/signup.html', message='Email Already Exists!')

@app.route('/signin', methods=['POST', 'GET'])
def signin_page():
   if request.method == 'GET':
      if session.get('username'):
         return redirect(url_for('home_page'))
      else:
         return render_template('./accounts/signin.html')
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      if not email.strip() or not password.strip():
         return render_template('./accounts/signin.html', message='Email or password is missing!')
      cursor = mysql.connection.cursor()
      cursor.execute('''SELECT * FROM login WHERE username=%s''', (email,))
      query_result = cursor.fetchone()
      if query_result == None:
         return render_template('./accounts/signin.html', message='Username doesnt exists!')
      elif check_password_hash(query_result[2], password) == False:
         return render_template('./accounts/signin.html', message='Password is incorrect!')
      session['username'] = query_result[1]
      return redirect(url_for('home_page'))

@app.route('/admin_signin', methods=['POST', 'GET'])
def admin_signin():
   if request.method == 'GET':
      if session.get('username'):
         return redirect(url_for('administration'))
      else:
         return render_template('./loginAsAdmin.html')
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      if not email.strip() or not password.strip():
         return render_template('./loginAsAdmin.html', message='Email or password is missing!')
      cursor = mysql.connection.cursor()
      cursor.execute('''SELECT * FROM admin_login WHERE username=%s''', (email,))
      query_result = cursor.fetchone()
      if query_result == None:
         return render_template('./loginAsAdmin.html', message='Username doesnt exists!')
      elif check_password_hash(query_result[2], password) == False:
         return render_template('./loginAsAdmin.html', message='Password is incorrect!')
      session['username'] = query_result[1]
      return redirect(url_for('administration'))

@app.route('/deliverer_signin', methods=['POST', 'GET'])
def deliverer_signin():
   if request.method == 'GET':
      if session.get('username'):
         return redirect(url_for('delivery'))
      else:
         return render_template('./loginAsDeliveryGuy.html')
   if request.method == 'POST':
      email = request.form['email']
      password = request.form['password']
      if not email.strip() or not password.strip():
         return render_template('./loginAsDeliveryGuy.html', message='Email or password is missing!')
      cursor = mysql.connection.cursor()
      cursor.execute('''SELECT * FROM delivery_login WHERE username=%s''', (email,))
      query_result = cursor.fetchone()
      if query_result == None:
         return render_template('./loginAsDeliveryGuy.html', message='Username doesnt exists!')
      elif check_password_hash(query_result[2], password) == False:
         return render_template('./loginAsDeliveryGuy.html', message='Password is incorrect!')
      session['username'] = query_result[1]
      return redirect(url_for('delivery'))

@app.route('/newItem')
def newItem():
   return render_template('/newItem.html')

@app.route('/editprofile',methods=['GET','POST'])
def edit_profile():
   if request.method == 'GET':
      if session.get('username'):
         cursor = mysql.connection.cursor()
         cursor.execute('''SELECT * FROM profile WHERE loginid=%s''', (session['username'],))
         query_result = cursor.fetchone()
         return render_template('./accounts/edit.html',result=query_result)
      else:
         return redirect(url_for('signin_page'))
   if request.method == 'POST':
      name = request.form['name']
      contact = request.form['contact']
      birthday = request.form['birthday']
      gender = request.form['gender']
      cursor = mysql.connection.cursor()
      my_update_query = (
             '''Update profile SET name=%s,contact=%s,birthday=%s,gender=%s WHERE loginid = %s''')
      credentials = (name,contact,birthday,gender,session['username'])
      cursor.execute(my_update_query, credentials)
      cursor.close()
      mysql.connection.commit()
      return redirect(url_for('home_page'))

@app.route('/purchase/<id>')
def purchase_page(id):
   cursor = mysql.connection.cursor()
   cursor.execute('''SELECT * FROM inventory WHERE id=%s''', ([id],))
   query_result = cursor.fetchone()
   if session.get('username'):
      return render_template('./accounts/purchase.html', purchasing_item=query_result, user=session['username'])
   return render_template('./accounts/purchase.html', purchasing_item=query_result)

@app.route('/purchase/<id>/<error>')
def purchase_page_with_error(id, error):
   cursor = mysql.connection.cursor()
   cursor.execute('''SELECT * FROM inventory WHERE id=%s''', ([id],))
   query_result = cursor.fetchone()
   if session.get('username'):
      return render_template('./accounts/purchase.html', purchasing_item=query_result, user=session['username'], error=error)
   return render_template('./accounts/purchase.html', purchasing_item=query_result, error=error)

@app.route('/logout')
def logout_page():
   session['username'] = None
   return redirect(url_for('home_page'))

@app.route('/confirm_purchase', methods=['POST'])
def confirm_page():
   if request.method == 'POST':
      if session.get('username'):
         date = datetime.now()
         item = request.form['item']
         cursor = mysql.connection.cursor()
         cursor.execute('''SELECT * FROM inventory WHERE id=%s''', (item,))
         query_result = cursor.fetchone()
         name = query_result[2]
         size = 'Standard'
         if (query_result[1] == 1):
            size = request.form['size']
         method = request.form['method']
         loc = request.form['loc']
         delivery = request.form['delivery']
         count = request.form['count']
         date = date.strftime("%d/%m/%y")
         price = int(count) * query_result[4]
         status = 'pending'
         if int(count) > query_result[3]:
            return redirect(url_for('purchase_page_with_error', id=query_result[0], error='error'))

         username = session['username']
         cursor.execute('''SELECT * FROM profile WHERE loginid=%s''', (username,))
         res = cursor.fetchone()
         contact = res[3]
         my_query = (
             '''INSERT INTO history (itemId,item, customer,size,method,location,delivery,count,date,price,contact,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''')
         credentials = (query_result[0],name, session['username'], size,
                        method, loc, delivery, count, date, price,contact, status)
         cursor.execute(my_query, credentials)
         mysql.connection.commit()
         my_update_query = (
             '''Update inventory SET count = %s WHERE id = %s''')
         credentials = (query_result[3]-int(count), query_result[0])
         cursor.execute(my_update_query, credentials)
         mysql.connection.commit()
         cursor.close()
         return redirect(url_for('home_page'))
      else:
         return redirect(url_for('signin_page'))

@app.route('/add_item', methods=['POST'])
def add_item():
   if request.method == 'POST':
      if session.get('username'):
         itype = request.form['type']
         name = request.form['name']
         total = request.form['total']
         price = request.form['price']
         cursor = mysql.connection.cursor()
         my_query = (
             '''INSERT INTO inventory (type,name,count,price) VALUES (%s,%s,%s,%s)''')
         credentials = (itype,name, total, price)
         cursor.execute(my_query, credentials)
         mysql.connection.commit()
         cursor.close()
         return redirect(url_for('administration'))
      else:
         return redirect(url_for('administration'))

@app.route('/history/<id>')
def history_page(id):
   if (session.get('username')):
      if (session['username'] == id):
         cursor = mysql.connection.cursor()
         cursor.execute('''SELECT * FROM history WHERE customer=%s''', ([id],))
         query_result = cursor.fetchall()
         if session.get('username'):
            return render_template('./accounts/history.html', purchasing_item=query_result, user=session['username'])
         return render_template('./accounts/history.html', purchasing_item=query_result)
      else:
         return redirect(url_for('home_page'))
   else:
      return redirect(url_for('home_page'))

@app.route('/delete', methods=['POST'])
def deleting_order():
   if session.get('username'):
      try:
         order_id = request.form['deleting']
         if not order_id.strip:
            return redirect(url_for('home_page'))
         cursor = mysql.connection.cursor()
         my_update_query = ('''Update history SET status = %s WHERE id = %s''')
         credentials = ('cancelled', order_id)
         cursor.execute(my_update_query, credentials)
         mysql.connection.commit()
         cursor.close()
         return redirect(url_for('history_page', id=session['username']))
      except:
         return redirect(url_for('home_page'))
   return redirect(url_for('home_page'))

@app.route('/del', methods=['POST'])
def deleting_item():
   if session.get('username'):
      try:
         item_id = request.form['deleting']
         if not item_id.strip:
            return redirect(url_for('administration'))
         cursor = mysql.connection.cursor()
         cursor.execute(f'''DELETE FROM inventory WHERE id = {item_id}''')
         mysql.connection.commit()
         cursor.close()
         return redirect(url_for('administration', id=session['username']))
      except:
         return redirect(url_for('administration'))
   return redirect(url_for('index'))

@app.route('/edit', methods=['GET','POST'])
def editing_order():
      if session.get('username'):
            order_id = request.form['editing']
            if not order_id.strip:
               return redirect(url_for('home_page'))
            cursor = mysql.connection.cursor()
            my_update_query = ('''Select * from history WHERE id = %s''')
            credentials = (order_id,)
            cursor.execute(my_update_query, credentials)
            query_result = cursor.fetchone()
            cursor.close()
            return render_template('/accounts/edithistory.html',old=query_result)
      return redirect(url_for('home_page'))

@app.route('/edit_action', methods=['POST'])
def editing_order_action():
         id = request.form['id']
         cursor = mysql.connection.cursor()
         cursor.execute('''SELECT * FROM inventory WHERE id=%s''', (id,))
         query_result = cursor.fetchone()
         count = request.form['count']
         count_old = request.form['count_old']
         if abs(int(count)-int(count_old)) > query_result[3] and int(count) > int(count_old):
               return redirect(url_for('history_page', id=session['username']))
         loc = request.form['loc']
         delivery = request.form['method']
         history = request.form['historyid']
         my_update_query = (
            '''Update history SET count = %s,location=%s,price=%s,delivery=%s WHERE id = %s''')
         credentials = (count,loc,int(count)*query_result[4],delivery,history)
         cursor.execute(my_update_query, credentials)
         mysql.connection.commit()
         my_update_query = (
             '''Update inventory SET count = %s WHERE id = %s''')
         if int(count_old) > int(count):
            credentials = (query_result[3]+(int(count_old)-int(count)), id)
         else:
            credentials = (query_result[3]-(int(count)-int(count_old)), id)
         cursor.execute(my_update_query, credentials)
         mysql.connection.commit()
         cursor.close()
         return redirect(url_for('history_page', id=session['username']))

@app.route('/edititem', methods=['GET','POST'])
def editing_item():
      if session.get('username'):
            item_id = request.form['editing']
            if not item_id.strip:
               return redirect(url_for('administration'))
            cursor = mysql.connection.cursor()
            my_update_query = ('''Select * from inventory WHERE id = %s''')
            credentials = (item_id,)
            cursor.execute(my_update_query, credentials)
            query_result = cursor.fetchone()
            cursor.close()
            return render_template('/edititem.html',old=query_result)
      return redirect(url_for('administration'))

@app.route('/edit_item_action', methods=['POST'])
def editing_item_action():
   if request.method == "POST":
      id = request.form['id']
      itype = request.form['type']
      name = request.form['name']
      total = request.form['total']
      price = request.form['price']
      cursor = mysql.connection.cursor()
      my_update_query = (
         '''Update inventory SET type = %s,name=%s,count=%s,price=%s WHERE id = %s''')
      credentials = (itype,name,total,price,id)
      cursor.execute(my_update_query, credentials)
      mysql.connection.commit()
      cursor.execute('''SELECT * FROM inventory ''')
      query_result = cursor.fetchall()
      cursor.close()
      return render_template('./adminPage.html', items=query_result, user=session['username'])
   return redirect(url_for('administration'))

@app.route('/successful', methods=['POST'])
def successful():
   if request.method == "POST":
      id = request.form['id']
      cursor = mysql.connection.cursor()
      my_update_query = (
         '''Update history SET status = %s WHERE id = %s''')
      credentials = ("delivered",id)
      cursor.execute(my_update_query, credentials)
      mysql.connection.commit()
      cursor.close()
      return redirect(url_for('delivery'))

@app.route('/failed', methods=['POST'])
def failed():
   if request.method == "POST":
      id = request.form['id']
      cursor = mysql.connection.cursor()
      my_update_query = (
         '''Update history SET status = %s WHERE id = %s''')
      credentials = ("delivery failed",id)
      cursor.execute(my_update_query, credentials)
      mysql.connection.commit()
      cursor.close()
      return redirect(url_for('delivery'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/accounts/bad.html'), 404

if __name__ == '__main__':
   app.run()