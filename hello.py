from flask import Flask , url_for , request , render_template
import random

app = Flask(__name__,template_for="templates") #(template_folder)

@app.route("/")
def main():
    age = 18
    names = ["amir" , "honey" , "arshia" , "elham"]
    return render_template("main.html", age = age , names = names) 
            
@app.route("/burgera")
def burgera():
    return render_template("index.html")

@app.route("/hello")
def hello():
    name = "amir"
    numbers = [1,2,3,4,5,6,32,312,12,34]
    number = 1
    return render_template("hello.html", name = name, numbers = numbers, number = number)

@app.route("/login")
def login():
    return "welcome to login page"

@app.route("/register", methods=["POST", "GET"])
def register():
        if request.method == "POST":
            return "this is POST web page"
        return f"welcome to registration page!"
    
@app.template_filter()
def khodi(data):
    return data + 10

@app.route("/passmaker/<int:length>")
def maker(length):
    character = "fdjwofhrewovclwf49485r2349817@!$$%#^&%*&^gbvmdl,tGEGHYNUY"
    password = " ".join(random.choice(character) for characters in range (length))
    return f"your password is {password}"

@app.route("/data")
def data():
    username = request.args.get("username")
    password = request.args.get("password")
    return f"welcome {username} , your pass is {password}"

if __name__ == "__main__":
    app.run(debug=True)  