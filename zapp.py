from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/result',methods=['POST'])
def result():
    name = request.form["name"]
    add = request.form['add']
    phno = request.form['phno']
    Hobb = request.form['Hobb']
    
    return render_template("result.html",result=name,result1=add,result2=phno,result3=Hobb)


if __name__ == '__main__':
    app.run(debug = True)
    



