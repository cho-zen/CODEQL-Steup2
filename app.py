from flask import Flask, request, render_template

num = eval(input("Enter num"))

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

