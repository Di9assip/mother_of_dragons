from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        action = request.form['action']
        if action == 'attack':
            message = "Ты сразилась с драконом и победила! 🐉🔥"
        elif action == 'run':
            message = "Ты убежала от дракона. Он остался доволен и не тронул тебя. 💨"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
