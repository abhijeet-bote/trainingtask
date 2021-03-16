from flask import Flask,request,render_template

app = Flask(__name__,template_folder='template')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
       # return 'succesfull'
       user = request.form['nm']
       id = request.form['am']
       return 'welcome '+user+id
    return render_template('login.html')

if __name__ == '__main__':
    app.run('127.0.0.1' , '8080', debug = True)