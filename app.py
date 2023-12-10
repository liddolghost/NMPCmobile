from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.route('/nav2/<nav2_param>')
def nav2(nav2_param):
    return render_template('nav2.html', nav2_param=nav2_param)

if __name__ == '__main__':
    app.run(debug=True)
