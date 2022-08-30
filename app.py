from crypt import methods
from webapp import create_app

app = create_app() 

if __name__ == '__main__':
    # Set fo False when running in production
<<<<<<< HEAD
    app.run(debug=True, port = 5001)
=======
    app.run(debug=True, port = 5002)
>>>>>>> 583594d077abb4a7e6e2c11a3a816f9925a62337
