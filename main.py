from webapp import create_app

app = create_app()

if __name__ == '__main__':
    # Turn off when running in production
    app.run(debug=True, port = 5004)

