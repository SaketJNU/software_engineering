import flask
from flask import Flask,request , jsonify
from xyz import AddTwo as ad


app = Flask(__name__)

@ app.route('/')
def test():
    return jsonify({"status":"ok"})




@ app.route('/parsename',methods=['GET'])
def test_name():

    var_name = request.args.get("name")
    return jsonify({"Entered name = ": var_name})




@ app.route('/twopara',methods=['GET'])
def two_para():
    n=request.args.get('name')
    r=request.args.get('rollno')
    output="Roll No{}has the name:{}".format(r,n)
    return output

@ app.route('/addtwo',methods=['GET'])
def add_two_num():
    fno = request.args.get("fn")
    sno = request.args.get("sn")

    a = ad()
    s = a.add_Two(fno,sno)

    return "Sum of {} and {} is : {}".format(fno,sno,s)

if __name__ == '__main__':
    app.run(port=50001) 