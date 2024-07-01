import json

# Load the JSON data from the file
with open('../data/puzzle2.json', 'r') as f:
    data = json.load(f)

# Extract the required sections
gridnums = data['gridnums']
clues_across = data['clues']['across']
clues_down = data['clues']['down']
answers_across = data['answers']['across']
answers_down = data['answers']['down']

# Create a dictionary to hold the final result
CROSSWORD_GRID = {}

# Helper function to get clue and answer based on number
def get_clue_answer(clue_number, clues, answers):
    for clue in clues:
        if clue.startswith(f"{clue_number}. "):
            answer = answers[clues.index(clue)]
            return clue, answer
    return None, None

# Analyze each value in gridnums
for i, value in enumerate(gridnums):
    if value != 0:
        row, col = divmod(i, 15)
        clue_across, answer_across = get_clue_answer(value, clues_across, answers_across)
        clue_down, answer_down = get_clue_answer(value, clues_down, answers_down)
        
        if clue_across:
            CROSSWORD_GRID[f"{value}A"] = {
                "start": (row, col),
                "direction": "A",
                "length": len(answer_across)
            }
        
        if clue_down:
            CROSSWORD_GRID[f"{value}D"] = {
                "start": (row, col),
                "direction": "D",
                "length": len(answer_down)
            }

# Function to save to a Python file
def save_to_python_file(data, filename):
    with open(filename, 'w') as f:
        f.write("CROSSWORD_GRID = {\n")
        for key, value in data.items():
            f.write(f'    "{key}": {{"start": {value["start"]}, "direction": "{value["direction"]}", "length": {value["length"]}}},\n')
        f.write("}\n")

# Save the result to a Python file
save_to_python_file(CROSSWORD_GRID, 'crossword_grid.py')

# Print the result to verify
for key, value in CROSSWORD_GRID.items():
    print(f'"{key}": {{"start": {value["start"]}, "direction": "{value["direction"]}", "length": {value["length"]}}}')
