from src import create_app

app = create_app()

# Run the app from this file!
if __name__ == '__main__':
    app.run(debug=True)