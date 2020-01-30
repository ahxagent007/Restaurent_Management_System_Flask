from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
   return 'INDEX'


@app.route('/Manager')
def manager_dashboard():
   return render_template('manager.html')

app.debug = True
app.run()
app.run(debug = True)


if __name__ == '__main__':
   app.run()
