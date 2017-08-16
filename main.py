from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    pw = request.form['pw']
    pver = request.form['pver']
    email = request.form['email']

    username_error = ''
    pw_error = ''  
    pver_error = ''
    email_error = ''

    if username == '':
        username_error = 'Please enter a valid username'
    elif len(username) < 3 or len(username) > 20 or " " in username:
        username_error = 'Username must contain between 3 and 20 characters and cannot contain spaces.'
        
    if pw == '':
        pw_error = 'Please enter a valid password'
    elif len(pw) < 3 or len(pw) > 20 or " " in pw:
        pw_error = 'Password must contain between 3 and 20 characters and cannot contain spaces.'

    if pw != pver:
        pver_error = 'Password does not match.'
        
    if email != '':
        if len(email) < 3 or len(email) > 20 or " " in email or "@" not in email or "." not in email:
            email_error = "Please enter a valid email address."

    if not username_error and not pw_error and not pver_error and not email_error:
        return redirect('/welcome?username={}'.format(username))
    else:
        return render_template('index.html', username_error = username_error, pw_error = pw_error, 
            pver_error = pver_error, email_error = email_error, username = username, email = email)

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)
    
app.run()

