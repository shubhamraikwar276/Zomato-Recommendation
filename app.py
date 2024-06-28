from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/explore-top-restaurants')
def top_restaurants():
    return render_template('explore-top-restaurants.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 6500)


