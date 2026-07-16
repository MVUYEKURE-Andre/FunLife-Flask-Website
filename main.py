from flask import Flask, render_template

app = Flask(__name__)


CATEGORIES = [
    {"slug": "travel",  "label": "Travel"},
    {"slug": "food",    "label": "Food"},
    {"slug": "friends", "label": "Friends"},
    {"slug": "nature",  "label": "Nature"},
    {"slug": "events",  "label": "Events"},
    {"slug": "sports",  "label": "Sports"},
]

MEMORIES = [
    {
        "image": "/static/images/dinner.jpg",
        "caption": "Dinner with the crew",
        "location": "Kigali",
        "category_slug": "food",
        "category_label": "Food",
    },
    {
        "image": "/static/images/kumazi.jpg",
        "caption": "Chasing waterfalls",
        "location": "Amazi",
        "category_slug": "nature",
        "category_label": "Nature",
    },
    {
        "image": "/static/images/game.jpg",
        "caption": "Game night chaos",
        "location": "Kigali",
        "category_slug": "friends",
        "category_label": "Friends",
    },
]

FEATURED_STORY = {
    "image": "/static/images/dinner.jpg",
    "title": "The weekend we didn't plan",
    "excerpt": "Four friends, one wrong turn, and the best trip of the year.",
    "url":  "/memories#featured",
}


@app.route("/memories")
def memories():
    return render_template(
        "memories.html",
        categories=CATEGORIES,
        memories=MEMORIES,
        featured=FEATURED_STORY,
    )
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/connect')
def connect():
    return render_template('connect.html')
@app.route('/memories')
# def memories():
#     return render_template('memories.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)