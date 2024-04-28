from yourapplication import create_app  # Remplacez 'yourapplication' par le nom de votre dossier ou module Flask

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)