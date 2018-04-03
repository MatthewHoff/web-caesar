from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True


form ="""<!DOCTYPE html>

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
        <form action="/" method='POST'>
            <label>Rotate by
                <input name="rot" type="text" value ="0" />
            </label>
            <br>
            <label>
                <input type="textarea" name="textarea" value="{0}" />
            </label>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form
    
@app.route("/", methods=["POST"])
def encrypt():
    rotation_value = int(request.form['rot'])
    text_value = request.form['textarea']
    encrypted = rotate_string(text_value,rotation_value)

    return form.format(encrypted)
    #return '<h1>' + encrypted + '</h1>'

app.run()

#request.args['id'] - similar value for forms

