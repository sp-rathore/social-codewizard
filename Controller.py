import web
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False

urls = [
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'PostRegistration',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity'
]
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': None})
session_data = session._initializer

render = web.template.render("Views/Templates/", base="MainLayout", globals = {'session': session_data, 'current_user': session_data["user"]})
#classes, routes

class Home:
    def GET(self):
        data = type('obj', (object,), {"username": "Ruchita", "password" : "jaiambe1234"})
        print("Control passed to Home screen for :", data.username, " and" , data.password)
        login = LoginModel.LoginModel()

        isCorrect = login.check_user(data)
        print("Control passed to Home screen for 2 :", data.username, " and", data.password)

        post_model = Posts.Posts()
        posts = post_model.get_all_posts()

        return render.Home(posts)

class Register:
    def GET(self):
        print("Posting the Register details")
        return render.Register()

class Login:
    def GET(self):
        return render.Login()

class PostRegistration():
    def POST(self):
        data = web.input()
        print("Posting the Register details into database")
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username

class CheckLogin():
    def POST(self):
        data = web.input()
        print("Checking Login details:   ", "Username is : ", data.username, "and password is : ", data.password)
        login = LoginModel.LoginModel()
        isCorrect = login.check_user(data)

        if isCorrect:
            print ("User :", data.username, " , matches and logged in")
            session_data["user"] = isCorrect
            return isCorrect

        return "error"

class PostActivity():

    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"



class Logout():
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "User logged out successfully"

if __name__ == "__main__":
    app.run()