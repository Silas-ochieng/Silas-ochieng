from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Skills Route
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Projects Route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Documents Route (No verification needed)
@app.route('/documents')
def documents():
    return render_template('documents.html')

# Contact Route
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
