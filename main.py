from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'PM',
  'location': 'Minsk',
  'salary': 'BYN 5000'
}, {
  'id': 2,
  'title': 'PO',
  'location': 'Polotsk',
}, {
  'id': 3,
  'title': 'SM',
  'location': 'Remote',
  'salary': 'BYN 6000',
}, {
  'id': 4,
  'title': 'BA',
  'location': 'Brest',
  'salary': 'BYN 4500'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Vova')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
