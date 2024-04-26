from collections import Counter

from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary of crystals based on user responses
crystal_suggestions = {
    'mental_health': {'Amethyst': 30},
    'career_growth': {'Citrine': 2, 'Pyrite': 1, 'Green Aventurine': 3},
    'relationship': {'Rose Quartz': 2, 'Rhodonite': 3, 'Emerald': 1},
    'thrive_ability': {'Amethyst': 1, 'Smoky Quartz': 5},
    'inner_self': {'Labradorite': 3, 'Selenite': 2, 'Moonstone': 1},
    'identity_wellbeing': {'Carnelian': 2, 'Garnet': 1, 'Red Jasper': 3},
    'blues_reds_greens': {'Amethyst': 3, 'Lepidolite': 1, 'Clear Quartz': 2},
    'water_colors': {'Citrine': 2, 'Pyrite': 1, 'Green Aventurine': 3},
    'rainbow': {'Rose Quartz': 1},
    'earthy_colors': {'Black Tourmaline': 1, 'Smoky Quartz': 3, 'Obsidian': 2},
    'roses_pinks_greens': {'Labradorite': 3, 'Selenite': 2, 'Moonstone': 1},
    'sea_turtle': {'Amethyst': 5, 'Garnet': 1, 'Red Jasper': 3},
    'blue_whale': {'Carnelian': 2, 'Tester': 1, 'Red Jasper': 3},
    'peacock': {'Carnelian': 2, 'Garnet': 1, 'Red Jasper': 3},
    'lioness': {'Carnelian': 2, 'Garnet': 1, 'Red Jasper': 3}
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
