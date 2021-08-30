from website import create_app

app = create_app()

#Run app only if this file main.py is executed not if imported to another
if __name__ == '__main__':
    app.run(debug=True) #To auto restart app when change in python code

