from flask import Flask,request,render_template,session,url_for,redirect,flash
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,RadioField,DateTimeField,
                     SelectField,TextField,TextAreaField,SubmitField,PasswordField)

from wtforms.validators import IPAddress,DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class Adddevice(FlaskForm):

    ipaddress = StringField('Enter the Device Ipaddress',validators=[IPAddress()],render_kw={'placeholder': 'Ipaddress'})
    username = StringField('Enter the Device Username', validators=[DataRequired()],render_kw={'placeholder': 'Device Username'})
    password = PasswordField('Enter the Device Password',validators=[DataRequired()],render_kw={'placeholder': 'Password'})
    Groupname = SelectField(u'Select the Group name for the Device',choices=[('Cisco_router','Cisco_IOS'),
                                                  ('Cisco_Switch','Cisco_nxos'),('Fortigate','Fortios')])

    submit = SubmitField('Submit')


@app.route('/')
def index():
    # name = 'jose'
    # temp = list(name)
    # pub_dictionary = {'name':'rani'}
    # mylist = range(1,100)
    # return render_template('basic.html',name = name,temp = temp, pub_dictionary = pub_dictionary,mylist = mylist)
    return render_template('login.html')

@app.route('/Welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/confirmation')
def confirmation():

    ip_address = request.args.get('ip address')
    # print(ip_address)
    # print(type(ip_address))
    ip_address = ip_address.split(".")
    # print(type(ip_address))
    # print(ip_address)
    # print(ip_address[0])
    # print(type(ip_address[0]))

    oct_numberic = False
    ip_address_lenth = False
    oct_num_range = False

    oct_numeric = all(c.isnumeric() for c in ip_address)

    print(ip_address_lenth)
    if oct_numeric:
        oct_num_range = all(0 < int(c) <= 255 for c in ip_address)

        if len(ip_address) == 4:
            ip_address_lenth = True
        print(oct_num_range)
        print(type(ip_address_lenth))







    # if oct_numberic:
    #     ip_address_lenth = len(ip_address)
    #     ip_address_lenth = 4
    #
    #     print(ip_address_lenth)




        # print(oct_num_range)



    confirm = ip_address_lenth and oct_numeric and oct_num_range
    print(confirm)




    # for octate in ip_address:
    #     if octate.isnumeric() = False:
    #         num_message = "Ip address can only have numeric values"
    #
    #     elif len(octate) != 4:
    #         len_message = "Ipv4 address requires four octate i.e - 192.168.20.1"
    #
    #     elif 0 < octate <=255:
    #         oct_message = "One octate should be between 1 -- 255"


    return render_template('confirmation.html',confirm = confirm, num_check = oct_numeric, ip_len_check = ip_address_lenth, ip_range_check = oct_num_range)


@app.route('/Add-Device',methods=['GET','POST'])
def adddevice():
    form = Adddevice()

    if request.method == 'POST':
        oct_numberic = False
        ip_address_lenth = False
        oct_num_range = False
        ipaddress = request.form['ipaddress']
        ipaddress = ipaddress.split('.')
        oct_numeric = all(c.isnumeric() for c in ipaddress)
        if oct_numeric:
            oct_num_range = all(0 < int(c) <= 255 for c in ipaddress)

            if len(ipaddress) == 4:
                ip_address_lenth = True


        if (not oct_numeric or not ip_address_lenth or not oct_num_range) :
            flash("Provide the correct ip address as per the IPV4 Rules!")
            return redirect(request.url)

    if form.validate_on_submit():

        session['ipaddress'] = form.ipaddress.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['Groupname'] = form.Groupname.data

        return redirect(url_for('thankyou'))
    return render_template('add-device-1.html',form=form)

    # return render_template('add-device.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
