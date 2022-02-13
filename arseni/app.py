import random

from flask import Blueprint, render_template, redirect, url_for, request, session, Flask
#from interact_with_DB import interact_db

#import requests
#import random


app = Flask(__name__)
app.secret_key = '123'


users ={"user1": {"username": "sapir", "First name": "sap", "Last name":  "bibi" ,"Email": "bibis@post.bgu.ac.il"},
        "user2": {"username": "sapir2","First name": "sap1" , "Last name": "bibi1","Email": "galo@galo.com"},
        "user3": {"username": "sapir3","First name": "sap2", "Last name":  "bibi2","Email": "galo@galo2.com"},
        "user4": {"username": "sapir4","First name": "sap3" , "Last name": "bibi3","Email": "galo@galo3.com"},
        "user5": {"username": "sapir5","First name": "sap4" , "Last name":  "bibi4","Email": "galo@galo4.com"}
        }




@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    #DB
    found=True
    if found:
        return render_template('CVgrid-exersize5.html' ,name='sapir')
    else:
        return render_template('CVgrid-exersize5.html')

@app.route('/assignment8')
#DB
def hello_world2():  # put application's code here
    found=True
    if found:
     return render_template('CVgrid-exersize5.html' ,name='sapir')
    else:
      return render_template('CVgrid-exersize5.html')

@app.route('/aboutme')
def aboutme_func():

    return render_template('aboutme.html',
                           profile={'name': 'sapir'},
                           university='bgu', age='31',
                           degrees=['first', 'second', 'third'])


@app.route('/forms')
def check_forms():
    return render_template('forms.html')


@app.route('/assignment9',methods=['GET','POST'])
def user_func():
        current = request.method
        if current == 'GET':
            if 'username' in request.args:
                username = request.args['username']
                if username is '':
                    return render_template('assignment9.html', search=True, users=users, correctuser=True)
                userlist = {}
                #for user in users.value():
                #    if user in ['username'] ==username:
                 #       userlist[1] = user
               #  if len(userlist) != 0:
                #     return render_template('assignment9.html', search=True, correctuser=True, users=userlist)
                #else:
                 #   return render_template('assignment9.html', correctuser=False, search=True)
            return render_template('assignment9.html')
       #  elif current == 'POST':
            session['login'] = True
            users[request.form['email']] = {'First Name': request.form['firstName'],
                                            'Last Name': request.form['lastName'],
                                            'Email': request.form['email'],
                                            'User Name': request.form['userName']}
            session['userName'] = request.form['userName']
            return render_template('assignment9.html')

   # if 'product' in request.args:
    #    product = request.args['product']
     #   size = request.args['size']
      #       return render_template('assignment9.html', p_name=product, p_size=size)
           # return render_template('assignment9.html')


assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         template_folder='templates')

@assignment10.route('/assignment10')
def assignment10_func():
    query = 'select * from users;'
   # users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    session.clear()
    # get the data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    # validation
    # insert to db
    if first_name != "" and last_name != "" and email != "":
        query = "insert into users(first_name, last_name, email) VALUES('%s', '%s', '%s');" % (first_name, last_name, email)
       # interact_db(query=query, query_type='commit')
        session['insert'] = True
        # come back to users
        return redirect('/assignment10')
    session['insert'] = False
    return redirect('assignment10')


@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    session.clear()
    user_old_email = request.form['old_email']
    user_email = request.form['new_email']
    user_fname = request.form['new_fname']
    user_lname = request.form['new_lname']
    # validation
    if user_email != "" and user_fname != "" and user_lname != "":
        query = "UPDATE users SET email='%s', first_name='%s', last_name='%s' WHERE email='%s';" % (user_email, user_fname, user_lname, user_old_email)
     #   interact_db(query=query, query_type='commit')
        session['update'] = True
        return redirect('/assignment10')
    session['update'] = False
    return redirect('assignment10')

@assignment10.route('/delete_user',  methods=['POST'])
def delete_user_func():
    session.clear()
    user_email = request.form['email']
    # validation
    if user_email != "":
        query = "delete from users where email='%s';" % user_email
     #  interact_db(query=query, query_type='commit')
        session['delete'] = True
        return redirect('/assignment10')
    session['delete'] = False
    return redirect('/assignment10')





@app.route('/logout')
def logout_func():
    session['username'] = ''
    return render_template('CVgrid-exersize5.html')

@app.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # DB
        found = True
        if found:
            session['username'] = username
            return redirect(url_for('aboutme_func'))
        else:
            return render_template('login.html')

@app.route('/CV-SAPIR-BIBI')
def CVGRID_func():
    return render_template('CVgrid-exersize5.html')



@app.route('/assignment12')
def assignment12_func():
    return render_template("assignment12.html")


# @app.route('/assignment12/restapi_users', defaults={'user_id': -1})
#@app.route('/assignment12/restapi_users/<int:user_id>')
#def get_user_func(user_id):
 #   if user_id == -1:
  #      return_dict = {}
   #     query = 'select * from users;'
    #    users = interact_db(query=query, query_type='fetch')
     #   for user in users:
      #      return_dict[f'user_{user.id}'] = {
       #         'id': user.id,
        #        'first name': user.first_name,
         #       'last name': user.last_name,
          #      'email': user.email,
           # }
    #else:
     #   query = 'select * from users where id=%s;' % user_id
     #   users = interact_db(query=query, query_type='fetch')
      #  if len(users) == 0:
       #     return_dict = {
        #        'status': 'failed',
         #       'message': 'user not found'
          #  }
       # else:
        #    return_dict = {
         #       'status': 'success',
            #    'id': users[0].id,
             #   'first_name': users[0].first_name,
             #   'last_name': users[0].last_name,
              #  'email': users[0].email,
          #  }

  #  return jsonify(return_dict)


if __name__ == '__main__':
    app.run(debug=True)


#@app.route('/req_front')
#def req_front():
#    return render_template('req_front.html')


#def get_pockemons(num):
#    pockemons = []
#    for i in range(num):
#        random_n=random.randint(1, 100)
#        res = request.get(f'https://pokeapi.co/api/v2/poclemon/{random_n}')
#        res = res.json()
#        pockemons.append(res)
#    return pockemons

#@app.route('/req_backend')
#def req_backend():
#    num = 3
#    if "number" in request.args:
#        num = int(request.args['number'])
#    pockemons = get_pockemons(num)
#    return render_template('req_backend.html' , pockemons=pockemons)