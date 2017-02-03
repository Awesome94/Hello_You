from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome'

@app.route('/helo/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

# the first route will take you to the home page which displays welcome.
# the second route allows to to give any name you want and it will give back hello
# with the name or word u fed in.
