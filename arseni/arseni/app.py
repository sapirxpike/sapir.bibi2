from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

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




@app.route('/CV-SAPIR-BIBI')
def CVGRID_func():
    return render_template('CVgrid-exersize5.html')



if __name__ == '__main__':
    app.run(debug=True)
