from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    @app.route('/')
    def index():
        return render_template('index.html', TITLE='Flask-101')

    @app.route('/about')
    def about():
        return render_template('about.html', TITLE='Flask-101')

    @app.route('/testdb')
    def testdb():
        import psycopg2
        con = psycopg2.connect('dbname=flask101 user=griezdev password=ridertime! host=postgres')
        cur = con.cursor()
        cur.execute('select * from page')
        id, title = cur.fetchone()
        con.close()
        return 'Output table page: {} - {}'.format(id, title)

    return app

#app.run('127.0.0.1', debug=True)
