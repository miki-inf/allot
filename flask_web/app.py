from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1',port=8000)
