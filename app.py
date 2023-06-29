from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This function handles the route for the home page.
    # It renders the index.html template.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
