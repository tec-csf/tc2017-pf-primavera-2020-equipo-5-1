from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap
import webbrowser
import time
import star_test
from flask_wtf import FlaskForm

app = Flask(__name__)
app.secret_key = "super secret key"
Bootstrap(app)


@app.route('/', methods=['POST'])
def my_form_post():
    num = request.form['a']
    dist = request.form['b']
    fallaPer = request.form['c']
    fallaCen = request.form['d']
    gen = request.form['e']
    reb = request.form['f']

    num_p = int(num)
    delta = int(dist)
    #fallaPerInt = int(fallaPer)
    gamma = int(fallaCen)
    alpha = int(gen)
    reboot = int(reb)

    session['num'] = num_p
    session['delt'] = delta
    session['gam'] = gamma
    session['alph'] = alpha
    session['rebo'] = reboot
    return redirect(url_for('start'))
    #return redirect(url_for('dy1.html'))
    #return redirect(url_for('stuff'))



@app.route('/_stuff', methods = ['GET'])
def stuff():
    num0 = session.get('num', None)
    delt0 = session.get('delt', None)
    gam0 = session.get('gam', None)
    alph0 = session.get('alph', None)
    rebo0 = session.get('rebo', None)

    #print(num0, delt0, gam0, alph0, rebo0)
    c = star_test.Central(num0, delt0, gam0, alph0, rebo0)
    c.turn_on()
    while c.turned_on:

        # if c.status and c.peripherial[0].status:
            # return jsonify(
            #     result = c.status.pop(),
            #     result2 = c.peripherial[0].status.pop()
            # )
             computers = []
             for p in range(len(c.peripherial)):
                 if c.peripherial[p].status:
                     computers.append(c.peripherial[p].status.pop())
                 if computers:
                     return jsonify(result=c.status.pop(), result2=str(computers))
            #return jsonify(result=c.status.pop())

@app.route('/start')
def start():
    return render_template('dy1.html')

@app.route('/')
def index():
    session['num'] = 0
    return render_template('index.html')


if __name__ == '__main__':

    app.run()
    #app.run(debug=True)
