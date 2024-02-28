from flask import Flask, render_template, request
from BLL import BusinessLogic


app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def hello():
    text = 'Incorrect login or password'

    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        business_logic = BusinessLogic()
        successfully_signed_in = business_logic.get_user_by_login_password(login, password)

        if successfully_signed_in == True:
            return render_template('index.html', error="")
        else:
            return render_template('index.html', error=text)
        
    return render_template('index.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")

        business_logic = BusinessLogic()
        business_logic.register_user(login, password)
    
        

        return redirect('/')

    return render_template('register.html')
