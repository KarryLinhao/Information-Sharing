from flask import Flask , render_template, url_for
from forms import RegistrationForm, LoginForm


app = Flask(__name__, template_folder='template')  #template floder default name is "templates"

app.config['SECRET_KEY'] = '8bd1e12af07330a9bc78ecfc52bafb50'

#post information
post = [
    {
        'author': 'karry',
        'title': "karry's post",
        'content': 'first post content',
        'dataPosted': 'Nov 23, 2023'
    }, {

        'author': 'Le',
        'title': "Le's post",
        'content': 'first post content',
        'dataPosted': 'Nov 23, 2023'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('homePage.html', posts=post)



@app.route("/about")
def about():
    return render_template('aboutPage.html', title = "About")

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title = "Register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = "Login", form = form)


if __name__ == '__main__':
    app.run(debug=True)



