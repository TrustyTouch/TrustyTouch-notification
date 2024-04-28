from . import create_app

app = create_app()

app.config['DB_NAME'] = 'postgres'
app.config['DB_USER'] = 'postgres'
app.config['DB_PASSWORD'] = 'postgres'
app.config['DB_HOST'] = 'localhost'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)