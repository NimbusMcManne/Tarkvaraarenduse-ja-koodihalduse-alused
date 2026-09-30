from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kilometers to Miles Converter</title>
    </head>
    <body>
        <h1>Kilometers to Miles Converter</h1>
        <form method="POST" action="/convert">
            <label for="kilometers">Enter kilometers:</label>
            <input type="number" step="any" name="kilometers" id="kilometers" required>
            <button type="submit">Convert</button>
        </form>
    </body>
    </html>
    '''

@app.route("/convert", methods=["POST"])
def convert():
    try:
        kilometers = float(request.form.get("kilometers"))
        factor = 0.621371
        miles = kilometers * factor
        return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Kilometers to Miles Converter</title>
        </head>
        <body>
            <h1>Kilometers to Miles Converter</h1>
            <p>{kilometers} kilometers is equal to {miles} miles</p>
            <a href="/">Convert another</a>
        </body>
        </html>
        '''
    except:
        return "Error: Please enter a valid number"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
