from flask import Flask, render_template


#create a flask instance
app = Flask(__name__)
favorite_pizza = ['pepperoni', 'catupiry', 'caligula', '5 queijos']
#create a route decorator
@app.route('/')
def index():
    return render_template("index.html", fav_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", e=e), 404



if __name__ == '__main__':
    app.run()
