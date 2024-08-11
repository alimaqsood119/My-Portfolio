from flask import Flask, request, render_template

app = Flask(__name__)

# Route for the home page that serves the HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Process the data (you can save it to a database, send an email, etc.)
    # For this example, we'll just print it
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return f"Thank you, {name}! Your message has been received."

if __name__ == '__main__':
    app.run(debug=True)
