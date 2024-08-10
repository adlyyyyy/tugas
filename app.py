from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/igs')
def igs():
    data = ["I", "G", "S"]
    return render_template('igs.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)