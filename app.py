# If you're on VScode run this command in your terminal

# pip install flask
#Make sure you are connected to the internet before you run the command.

#Importing flask, string and random
# random : generates random values assigned to it
from flask import Flask,url_for,render_template,request
import string,random
from random import randint

#Instantiating our application
app = Flask(__name__)

#lask routers
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST","GET"])
def generatePassword():
    # Making a post request to the form
    if request.method == "POST":
        # The result variable will contain the generated password
        result = ""
        # Getting the number entered to input field
        #The input field contains the length of the password to be generate
        password_length = request.form["length"]
        # Looping through the password length
        for num in range(int(password_length)):
            # Searches for random characters within the given range
            random_char = randint(10,94)
            #Appends character to the result variable
            result += string.printable[random_char]
            # Rendering our template and instantiating our result variable to it
        return render_template("index.html", result = result)
    else:
        return render_template("index.html")


        


# Auto debug mode -- a Flask Jinja2 extension
#Runs flask application
if __name__ == "__main__":
    app.run(debug = True)



# TESTING MY THEORY

#import random, string

#def generatePassword(num):
   # password = ""

  #  for n in range(num):
  #      x = random.randint(10,94)
  #      password += string.printable[x]

 #   return password
#print(generatePassword(16))