from flask import Flask
app = Flask(__name__) #create Flask object


'''
@app.route("/occupations") #assign following fxn to run in response to a root request
def hello_world():
    return "No hablo queso!"
'''


@app.route("/1")
def a():
    return "<a href = '/2'> Page2 </a>"

@app.route("/2")
def b():
    return "<a href = '/3'> Page3 </a>"

@app.route("/3")
def c():
    return "<a href = '/1'> Page1 </a>"


if __name__ == "__main__": #do not run if this file is imported as module
    app.run()

