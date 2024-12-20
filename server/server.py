from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def randomiser():
    r = random.randrange(0, 1000)
    if r == 177:
        return f'<b>Congrats!!! You found the number {r}!</b>'
    else:
        return f'<b>Sorry, you got {r}</b>'

#
# # Exercise 2
# @app.route('/welcome')
# def welcome():
#     return '''Welcome to Flask Development!
# <br>
# This is Labwork 3: Flask/MySQL/API
# '''
#
# # Exercise 3
# @app.route('/table')
# def table():
#     data = [{'name': 'Alice', 'age': 22},
#             {'name': 'Bob', 'age': 19},
#             {'name': 'Charlie', 'age': 25},
#             {'name': 'David', 'age': 24},
#             {'name': 'Eve', 'age': 21}]
#     return render_template('table.html', students=data)
#
# # Exercise 4
# @app.route('/factorial/<number>')
# def calc(number):
#     return str(factorial(int(number)))+"\n"
#
# # Exercise 5
# @app.route('/is_prime/<number>')
# def prime(number):
#     if isprime(int(number)):
#         return "Prime"
#     else:
#         return "Not prime"
#
# # Exercise 6
# @app.route("/sort")
# def sort_flask():
#     numbers = request.args.get("numbers").split(",")
#     return str(sorted(numbers))

if __name__ == '__main__':
    app.run(debug=True)