from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

@app.route('/users')
def read_all():
    users = User.get_all_users()
    return render_template('read_all.html', users = users)

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/process', methods=['POST'])
def create():
    User.create_user(request.form)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
