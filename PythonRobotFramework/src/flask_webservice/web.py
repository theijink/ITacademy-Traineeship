from flask import Flask
from time import sleep
from random import choice

# reconfigure the app file with: $ export FLASK_APP=<name>.py

app = Flask(__name__)

@app.route("/")
def hallo_wereld():
	return '''
    <html>
    <head>
    <style>
    .button {
    border: none;
    color: white;
    padding: 16px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
    }
    .button1 {
    background-color: #008CBA; 
    color: black; 
    border: 2px solid #008CBA;
    }
    .button1:hover {
    background-color: #008CBA;
    color: white;
    }
    }
    </style>
    </head>
    <body>
    
    <h1>Welcome to the server</h1><br>
    <a>Click a button to do something</a><br>
    <button class="button button1">Visit home page</button><br><br>
    
    
    </body>
    </html>
        
    
    '''