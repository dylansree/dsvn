from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def write_to_file(data):
    with open('database.csv', mode='a') as database:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{name}, {email}, {subject}, {message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect(request.referrer)
        # return 'did it werk?'
    else:
        return 'ah shit what happen'


if __name__ == '__main__':
    app.run(debug=True)
