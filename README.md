# Final_crossword
# 2nd part of the project : grid filling 
# inputs : (stored in data folder)
- [puzzle2.json](./grid_filling/data/puzzle2.json) : crossword from the NYTimes in json format, you can find a lot of them on this [github repo](https://github.com/doshea/nyt_crosswords)
- [candidates2.json](./grid_filling/data/candidates2.json) : list of candidate words for each clue in JSON format

# processing of the grid filling : (scripts stored in the src folder)
- 1st step : Run the script [converter.py](./grid_filling/src/converter.py) to process the puzzle2.json to convert it into a python file crossword_grid containing  a JSON structure with every clue, their direction and the length of the word that matches the clue.
- 2nd step : solve the crossword running the script [solver.py](./grid_filling/src/solver.py), using Z3 solving considering that the grid filling is a SMT problem. 

# output (stored in the data folder):
- [crossword_output.txt](./grid_filling/datacrossword_output.txt) : grid of the crossword filled in a .txt format
