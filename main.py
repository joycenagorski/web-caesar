from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;                    
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method="POST">
            <label for="rot">Rotate By:</label>
            <input type="text" name="rot" value="0" />
            <textarea name="text" type="text">{0}</textarea>
            <input type="submit" />
            </form>  
        </body>
    </html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rotation = int(rot)
    not_encrypt = str(text)

    encrypt_text = rotate_string(not_encrypt, rotation)

    return '<h1>' + form.format(encrypt_text) + '</h1>'



@app.route("/")
def index():
    return form.format('')


app.run()