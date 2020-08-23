from flask import Flask, render_template,request

app = Flask(__name__)

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


@app.route('/Add-Device')
def adddevice():
    return render_template('add-device.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
