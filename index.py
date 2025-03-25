from flask import Flask, render_template, url_for, request,redirect

app=Flask(__name__)

#route==link==url

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/simple")
def simple():

    return render_template("simple.html")


@app.route("/calculate", methods=["post"])
def calculate():
    first_number=int(request.form["firstNumber"])
    operation=request.form["operation"]
    second_number=int(request.form["secondNumber"])
    if operation=="+":
        result= first_number+second_number
    elif operation=="-":
        result= first_number-second_number
    elif operation=="x":
        result= first_number*second_number
        
    elif operation=="/":
        result= first_number/second_number


    else:
        result= -1
        
    return render_template("/simple.html",result=result)
    

if __name__=="__main__":
    app.run(debug=True)