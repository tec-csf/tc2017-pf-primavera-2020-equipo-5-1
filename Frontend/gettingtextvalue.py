from flask import Flask, request, render_template

app = Flask(__name__)

#class TestDatos():

@app.route('/')
def my_form():
    return render_template('from_ex.html')

@app.route('/', methods=['POST'])
def my_form_post():
    num = request.form['a']
    dist = request.form['b']
    fallaPer = request.form['c']
    fallaCen = request.form['d']
    gen = request.form['e']
    reb = request.form['f']

    numInt = int(num)
    distInt = int(dist)
    fallaPerInt = int(fallaPer)
    fallaCenInt = int(fallaCen)
    genInt = int(gen)
    rebInt = int(reb)

    print "Numero de computadoras: ", numInt
    print "Distribucion de trabajos: ", distInt
    print "Falla en comp perifericas: ", fallaPerInt
    print "Falla en comp central: ", fallaCenInt
    print "Generacion de trabajos: ", genInt
    print "Recuperacion despues de falla: ", rebInt

    return (numInt, distInt, fallaPerInt, fallaCenInt, genInt, rebInt)


if __name__ == "__main__":
    app.run()
