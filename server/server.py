from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def randomiser():
    r = random.randrange(0, 1000)
    if r == 177:
        return f'<b>Congrats!!! You found the number {r}!</b>\n'
    else:
        return f'<b>Sorry, you got {r}</b>\n'


if __name__ == '__main__':
    app.run(debug=True)
