from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nookala3656@gmail.com'
app.config['MAIL_PASSWORD'] = 'pjuyhgioilukcyjq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'nookala3656@gmail.com', recipients = ['shashankgowtham12@gmail.com'])
   msg.body = "Hello team server was down"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=8000)