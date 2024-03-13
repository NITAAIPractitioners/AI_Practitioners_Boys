from flask import Flask, render_template

app = Flask(__name__)
students = [
{'id':1,
'sname':'Abdalla Alqahtani',
'insterests':'Web scraping'},
 { 'id':2,
  'sname':'Hussain',
  'insterests':'project engineer'},
  { 'id':3,
  'sname':'Ali Alqahtani',
  'insterests':'AI modelling'},
  { 'id':4,
  'sname':'Majed Almutairy',
  'insterests':'Data engineer'}
]

@app.route("/")
def hello_world():
  return render_template('home.html',students=students)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
