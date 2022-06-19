from website import create_app

app = create_app()

if __name__ == '__main__': # only if this file is being run, not if it is imported by another file
# just to make sure the app is created through main.py only
# The entry point for the app
    app.run(debug=True)