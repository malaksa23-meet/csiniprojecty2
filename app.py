from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config = {
    "apiKey": "AIzaSyDQKyj4e1V9o_3ifD-hlce40akA9IDJhtQ",
    "authDomain": "miniproject-3ca13.firebaseapp.com",
    "projectId": "miniproject-3ca13",
    "storageBucket": "miniproject-3ca13.appspot.com",
    "messagingSenderId": "904870936143",
    "appId": "1:904870936143:web:b208ece871d5d2aa76f43a",
    "measurementId": "G-6G128XP3TV",
    "databaseURL" :"https://miniproject-3ca13-default-rtdb.europe-west1.firebasedatabase.app/"}

 
firebase = pyrebase.initialize_app(config)
auth=firebase.auth()
db = firebase.database()





app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # try:
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        return redirect(url_for('add_posts'))
        # except:
            # error = "Authentication failed"
    return render_template("signin.html")

   
    return render_template("signin.html", error= error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        bio= request.form['bio']
        user_name = request.form['uname']
        #try:
        login_session['user'] =auth.create_user_with_email_and_password(email, password)
        user = {"name": name,"email":email, "password":password,"bio":bio,"user_name":user_name}
        db.child("Users").child(login_session['user']['localId']).set(user)
        return redirect(url_for('add_posts'))
       # except:
            #error = "Authentication failed" 
            #return render_template("signup.html", error=error)
    return render_template("signup.html", error=error)



@app.route('/add_posts', methods=['GET', 'POST'])
def add_posts():
    error = ""
    if request.method == 'POST':
        try:
            text= request.form['text']
            title= request.form['title'] 
            post={"text":text,"title":title}
            # , "uid":login_session['user']['localId']
            db.child("Posts").push(post)
            all_posts=db.child("Posts").get().val().values()
            return redirect(url_for('all_posts'), all_posts=all_posts)
        except:
            error:"error - can't add the posts"
            return render_template("add_posts.html", error = error, all_posts=all_posts)
    else:
        all_posts=db.child("Posts").get().val().values()
        return render_template("add_posts.html", all_posts=all_posts)



@app.route('/sign_out', methods=['GET', 'POST'])
def sign_out():
    return redirect(url_for('signin'))


@app.route('/all_posts', methods=['GET', 'POST'])
def all_posts():
    error=""
    try:
        all_posts=db.child("Posts").get().val().values()
        return render_template ("posts.html",all_posts=all_posts)
    except:
        error:"error - can't show all the posts"
        return error
        return render_template("posts.html",all_posts=all_posts)

    return render_template("posts.html",all_posts=all_posts)






if __name__ == '__main__':
    app.run(debug=True,
        port = 5001)