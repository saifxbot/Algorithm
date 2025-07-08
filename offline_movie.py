from flask import Flask, request, render_template_string

app = Flask(__name__)

movies = [  # Your 30-movie list remains unchanged
    {"name": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": 8.8, "thumbnail": "https://m.media-amazon.com/images/I/51x3Q5Y+XlL._AC_SY445_.jpg"},
    {"name": "The Shawshank Redemption", "genre": "Drama", "year": 1994, "rating": 9.3, "thumbnail": "https://m.media-amazon.com/images/I/51NiGlapXlL._AC_SY445_.jpg"},
    {"name": "The Dark Knight", "genre": "Action", "year": 2008, "rating": 9.0, "thumbnail": "https://m.media-amazon.com/images/I/51T8ox4WfKL._AC_SY445_.jpg"},
    {"name": "Interstellar", "genre": "Sci-Fi", "year": 2014, "rating": 8.6, "thumbnail": "https://m.media-amazon.com/images/I/91kFYg4fX3L._AC_SY679_.jpg"},
    {"name": "Forrest Gump", "genre": "Drama", "year": 1994, "rating": 8.8, "thumbnail": "https://m.media-amazon.com/images/I/61+oDDeD34L._AC_SY741_.jpg"},
    {"name": "Pulp Fiction", "genre": "Crime", "year": 1994, "rating": 8.9, "thumbnail": "https://m.media-amazon.com/images/I/51xYQKZrz9L._AC_SY445_.jpg"},
    {"name": "Fight Club", "genre": "Drama", "year": 1999, "rating": 8.8, "thumbnail": "https://m.media-amazon.com/images/I/81D+KJkO5-L._AC_SY679_.jpg"},
    {"name": "The Matrix", "genre": "Sci-Fi", "year": 1999, "rating": 8.7, "thumbnail": "https://m.media-amazon.com/images/I/51vpnbwFHrL._AC_SY445_.jpg"},
    {"name": "Gladiator", "genre": "Action", "year": 2000, "rating": 8.5, "thumbnail": "https://m.media-amazon.com/images/I/51A9M3ZzVML._AC_SY445_.jpg"},
    {"name": "Whiplash", "genre": "Drama", "year": 2014, "rating": 8.5, "thumbnail": "https://m.media-amazon.com/images/I/71VZHqkRnhL._AC_SY741_.jpg"},
    {"name": "Parasite", "genre": "Thriller", "year": 2019, "rating": 8.6, "thumbnail": "https://m.media-amazon.com/images/I/91oTApYb-ML._AC_SY741_.jpg"},
    {"name": "Joker", "genre": "Drama", "year": 2019, "rating": 8.4, "thumbnail": "https://m.media-amazon.com/images/I/71xZ3ykIcrL._AC_SY679_.jpg"},
    {"name": "The Godfather", "genre": "Crime", "year": 1972, "rating": 9.2, "thumbnail": "https://m.media-amazon.com/images/I/71xBLRBYOiL._AC_SY741_.jpg"},
    {"name": "Avengers: Endgame", "genre": "Superhero", "year": 2019, "rating": 8.4, "thumbnail": "https://m.media-amazon.com/images/I/81ExhpBEbHL._AC_SY679_.jpg"},
    {"name": "Django Unchained", "genre": "Western", "year": 2012, "rating": 8.4, "thumbnail": "https://m.media-amazon.com/images/I/61iOXz+G8mL._AC_SY741_.jpg"},
    {"name": "Avengers: Infinity War", "genre": "Superhero", "year": 2018, "rating": 8.4, "thumbnail": "https://m.media-amazon.com/images/I/81p+xe8cbnL._AC_SY679_.jpg"},
    {"name": "Titanic", "genre": "Romance", "year": 1997, "rating": 7.9, "thumbnail": "https://m.media-amazon.com/images/I/71c05lTE03L._AC_SY741_.jpg"},
    {"name": "The Prestige", "genre": "Mystery", "year": 2006, "rating": 8.5, "thumbnail": "https://m.media-amazon.com/images/I/51o5dnjk07L._AC_SY445_.jpg"},
    {"name": "The Lion King", "genre": "Animation", "year": 1994, "rating": 8.5, "thumbnail": "https://m.media-amazon.com/images/I/81MeQRwL2dL._AC_SY679_.jpg"},
    {"name": "WALL·E", "genre": "Animation", "year": 2008, "rating": 8.4, "thumbnail": "https://m.media-amazon.com/images/I/81m0N6I9hjL._AC_SY741_.jpg"},
    {"name": "Toy Story", "genre": "Animation", "year": 1995, "rating": 8.3, "thumbnail": "https://m.media-amazon.com/images/I/81R6utKhGUL._AC_SY679_.jpg"},
    {"name": "Up", "genre": "Animation", "year": 2009, "rating": 8.2, "thumbnail": "https://m.media-amazon.com/images/I/81G+oWQ2MwL._AC_SY679_.jpg"},
    {"name": "Inside Out", "genre": "Animation", "year": 2015, "rating": 8.1, "thumbnail": "https://m.media-amazon.com/images/I/71wZ-9xEX-L._AC_SY741_.jpg"},
    {"name": "Coco", "genre": "Animation", "year": 2017, "rating": 8.4, "thumbnail": "https://m.media-amazon.com/images/I/91yj63h7-KL._AC_SY741_.jpg"},
    {"name": "Ratatouille", "genre": "Animation", "year": 2007, "rating": 8.1, "thumbnail": "https://m.media-amazon.com/images/I/61Nwz5W1j7L._AC_SY741_.jpg"},
    {"name": "Finding Nemo", "genre": "Animation", "year": 2003, "rating": 8.1, "thumbnail": "https://m.media-amazon.com/images/I/81PSt9mfdwL._AC_SY679_.jpg"},
    {"name": "The Incredibles", "genre": "Animation", "year": 2004, "rating": 8.0, "thumbnail": "https://m.media-amazon.com/images/I/81AfzZkHD1L._AC_SY679_.jpg"},
    {"name": "Monsters, Inc.", "genre": "Animation", "year": 2001, "rating": 8.1, "thumbnail": "https://m.media-amazon.com/images/I/91TW-SU9UGL._AC_SY741_.jpg"},
    {"name": "Braveheart", "genre": "History", "year": 1995, "rating": 8.3, "thumbnail": "https://m.media-amazon.com/images/I/71L3WGK2whL._AC_SY741_.jpg"},
    {"name": "The Pianist", "genre": "War", "year": 2002, "rating": 8.5, "thumbnail": "https://m.media-amazon.com/images/I/91HJ1f8jbnL._AC_SY741_.jpg"}
]

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>🎬 Movie Library</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
        .header {
            background: linear-gradient(to right, #1f4037, #99f2c8);
            color: white;
            padding: 40px 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            border-bottom: 3px solid #fff;
        }
        .header h1 {
            font-size: 36px;
            font-weight: 600;
            margin: 0;
            letter-spacing: 1px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }
        .form-container { text-align: center; margin: 20px; }
        .form-container input, .form-container select {
            padding: 10px;
            font-size: 16px;
            margin-right: 10px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            padding: 30px;
            max-width: 1300px;
            margin: auto;
        }
        .card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: 0.3s ease;
        }
        .card:hover { transform: translateY(-5px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .card img { width: 100%; height: 320px; object-fit: cover; }
        .card-body { padding: 15px; }
        .card-body h3 { margin: 0; font-size: 18px; color: #333; }
        .info { font-size: 14px; color: #777; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Movie Library</h1>
    </div>
    <div class="form-container">
        <form method="get">
            <input type="text" name="search" placeholder="Search by name" value="{{ request.args.get('search', '') }}">
            <select name="sort">
                <option value="">-- Sort By --</option>
                <option value="year" {% if request.args.get('sort') == 'year' %}selected{% endif %}>Year</option>
                <option value="rating" {% if request.args.get('sort') == 'rating' %}selected{% endif %}>Rating</option>
            </select>
            <input type="submit" value="Apply">
        </form>
    </div>
    <div class="grid">
        {% for m in movies %}
        <div class="card">
            <img src="{{ m.thumbnail }}" alt="{{ m.name }}">
            <div class="card-body">
                <h3>{{ m.name }}</h3>
                <div class="info">{{ m.genre }} | {{ m.year }} | ⭐ {{ m.rating }}</div>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    filtered = movies[:]
    search_query = request.args.get("search", "").lower()
    sort_by = request.args.get("sort", "")

    if search_query:
        filtered = [m for m in filtered if search_query in m["name"].lower()]
    if sort_by == "year":
        filtered = sorted(filtered, key=lambda x: x["year"])
    elif sort_by == "rating":
        filtered = sorted(filtered, key=lambda x: x["rating"], reverse=True)

    return render_template_string(html_template, movies=filtered, request=request)

if __name__ == "__main__":
    app.run(debug=True)
