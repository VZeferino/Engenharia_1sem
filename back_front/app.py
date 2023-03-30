from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coordinates.db'
db = SQLAlchemy(app)

class Coordinate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    z = db.Column(db.Float)
    r = db.Column(db.Float)

@app.cli.command()
def createdb():
    db.create_all()

@app.route('/')
def index():
    coordinates = Coordinate.query.all()
    return render_template('index.html', coordinates=coordinates)

@app.route('/coords', methods=['POST'])
def coords():
    coor = Coordinate(
        x = request.form['x'],
        y = request.form['y'],
        z = request.form['z'],
        r = request.form['r']
    )
    db.session.add(coor)
    db.session.commit()
    return redirect('/')

@app.route('/godot', methods=["GET", "POST"])
def godot_coords():
    coordenadas = Coordinate.query.all()
    if coordenadas:
        x = coordenadas[-1].x
        y = coordenadas[-1].y
        z = coordenadas[-1].z
        r = coordenadas[-1].r
        godotstring = f"{x}/{y}/{z}/{r}"
        return godotstring

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)