from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # name = 'jose'
    # temp = list(name)
    # pub_dictionary = {'name':'rani'}
    # mylist = range(1,100)
    # return render_template('basic.html',name = name,temp = temp, pub_dictionary = pub_dictionary,mylist = mylist)
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
