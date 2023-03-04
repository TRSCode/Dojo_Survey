from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def success():
    return render_template('result.html')

@app.route('/survey', methods=['POST'])
def create_survey():
    print("Got Post Info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True) 