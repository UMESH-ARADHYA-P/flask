
from flask import Flask  ,redirect
app = Flask(__name__) 
@app.route('/')
def index():
    return redirect('https://www.w3schools.com/html/default.asp')
if __name__ =="__main__":  
    app.run(debug = True)