from collections import Counter

from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary of crystals based on user responses
crystal_suggestions = {
    'health': {'Amethyst': 5, 'Clear Quartz': 5, },
    'career': {'Citrine': 4, 'Pyrite': 5, 'Tiger eye': 4, 'Green Aventurine': 5},
    'relationship': {'Rose Quartz': 5, 'Strawberry Quartz': 5 },
    'personal_development': {'Lapiz lazuli': 3, 'Black Tourmaline': 3, 'Tiger eye': 6 },
    'money': {'Citrine': 5, 'Pyrite': 5, 'Tiger eye': 4, 'Green Aventurine': 3},
    'inner_peace': {'Aquamarine': 5, 'Clear Quartz': 5, 'Black Lava': 5, 'Rose Quartz': 5, 'Selenite': 4, 'Strawberry Quartz': 5},

    'physical_healing': {'Amethyst': 5, 'Red Jasper': 5, 'Red Garnet': 5, 'Rose quartz': 3, 'Strawberry Quartz': 3 },
    'mental_healing': {'Lapiz Lazuli': 5, 'Clear Quartz': 5, 'Amethyst': 5 , 'Howlite': 3 , 'Aquamarine': 4 },
    'spiritual_healing': {'Selenite': 5, 'Black Tourmaline': 2, 'Clear Quartz': 5, 'Green Aventurine': 3 , 'Lapiz Lazuli': 3},

    'blues_reds_greens': {'Amethyst': 3, 'Lapiz Lazuli': 5, 'Aquamarine': 5, 'Clear Quartz': 2},
    'water_colors': {'Citrine': 2, 'Pyrite': 5, 'Green Aventurine': 3},
    'rainbow': {'Rose Quartz': 1, 'Strawberry Quartz': 3, 'Green Aventurine': 1, 'Moonstone': 1, 'Amethyst': 3, 'Lapiz Lazuli': 5, 'Aquamarine': 5, 'Clear Quartz': 2 },
    'earthy_colors': {'Black Tourmaline': 2, 'Black Lava': 3, 'Pyrite': 3, 'Smoky Quartz': 3, 'Black Obsidian': 2, 'Tiger eye': 2},
    'roses_pinks_greens': {'Rose Quartz': 3, 'Strawberry Quartz': 3, 'Green Aventurine': 1, 'Moonstone': 1},

    'owl': {'Amethyst': 5, 'Garnet': 1, 'Black Lava': 5, 'Lapiz Lazuli': 5, 'Red Jasper': 3},
    'dolphin': {'Citrine': 2, 'Pyrite': 5, 'Green Aventurine': 3},
    'butterfly': {'Lapiz lazuli': 5, 'Black Onyx': 3, 'Tiger eye': 3, 'Garnet': 1, 'Red Jasper': 3},
    'wolf': {'Black Tourmaline': 3, 'Black Lava': 5, 'Pyrite': 5, 'Lapiz Lazuli': 3, 'Smoky Quartz': 3, 'Black Obsidian': 2, 'Tiger eye': 3, 'Garnet': 1, 'Red Jasper': 3}
}

@app.route('/')
def index():
    return render_template('index.html')


def suggest_crystals(selected_options):
    # List all selected crystals
    selected_crystals = set()
    for option in selected_options:
        if option in crystal_suggestions:
            selected_crystals.update(crystal_suggestions[option].keys())

    # Apply weightage to crystals based on selected options only
    crystal_weights = Counter()
    for option in selected_options:
        if option in crystal_suggestions:
            for crystal, weight in crystal_suggestions[option].items():
                crystal_weights[crystal] += weight

    # Get the top crystals with the highest total weightage
    top_crystals = crystal_weights.most_common(4)
    return [crystal[0] for crystal in top_crystals]


@app.route('/result', methods=['POST'])
def result():
    answers = request.form

    selected_options = [answers.get(key) for key in answers.keys()]

    suggested_crystals = suggest_crystals(selected_options)

    return render_template('result.html', crystals=suggested_crystals)


if __name__ == '__main__':
    app.run(debug=True)
