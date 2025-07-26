from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='app/static', template_folder='app/templates')

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html')

#define the route for the about page
@app.route('/learnlhokay')
def learnlhokay():
    return render_template('learnlhokay.html')

# Define the route for the soundboard
@app.route("/soundboard")
def soundboard():
    # List of tuples: (Tibetan letter, audio filename without .mp3)
    letters = [
        ('ཀ', 'ka'),   ('ཁ', 'kha'),   ('ག', 'ga'),   ('ང', 'nga'),
        ('ཅ', 'ca'),   ('ཆ', 'cha'),   ('ཇ', 'ja'),   ('ཉ', 'nya'),
        ('ཏ', 'ta'),   ('ཐ', 'tha'),   ('ད', 'da'),   ('ན', 'na'),
        ('པ', 'pa'),   ('ཕ', 'pha'),   ('བ', 'ba'),   ('མ', 'ma'),
        ('ཙ', 'tsa'),  ('ཚ', 'tsha'),  ('ཛ', 'dza'),  ('ཝ', 'wa'),
        ('ཞ', 'zha'),  ('ཟ', 'za'),   ('འ', 'a'),    ('ཡ', 'ya'),
        ('ར', 'ra'),   ('ལ', 'la'),   ('ཤ', 'sha'),  ('ས', 'sa'),
        ('ཧ', 'ha'),   ('ཨ', 'ah')
    ]

    return render_template("soundboard.html", letters=letters)

if __name__ == '__main__':
    app.run(debug=True)
