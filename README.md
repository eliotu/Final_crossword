# Final_crossword

# Introduction
This project is part of a CSNLP course, designed to fill crossword grids using sophisticated natural language processing (NLP) and constraint satisfaction techniques. The goal is to automate the process of solving crossword puzzles by interpreting clues, generating candidate solutions, and fitting these solutions into a given crossword grid using a satisfiability modulo theories (SMT) approach.

# 1st part of the project: Question answering
Our dataset is stored in the folder final_submission_question_answering/dataset.

In order to solve the question answering we made three approaches.

The lesk algorithm in [lesk_algo.ipynb](./final_submission_question_answering/lesk_algo.ipynb) and two models: bert ande T5

The code to train our two models are stored in [PARTI_TF5.ipynb](./final_submission_question_answering/PARTI_TF5.ipynb)   and [PART_I_BERT_MASK.ipynb](./final_submission_question_answering/PART_I_BERT_MASK.ipynb) .

You can run it, however we've stored the models in this link https://drive.google.com/drive/folders/1bMcZ1QW2pWtbJtuzKfhETwLVW29vUrtB.

To test the accuracy of our models we have made this notebook [results.ipynb](./final_submission_question_answering/results.ipynb)

# 2nd part of the project : grid filling 
All the following is soterd in the grid_filling folder
# inputs : 
All the inputs are stored in the "data" folder 
- [puzzle2.json](./grid_filling/data/puzzle2.json) : crossword from the NYTimes in json format, you can find a lot of them on this [github repo](https://github.com/doshea/nyt_crosswords)
- [candidates2.json](./grid_filling/data/candidates2.json) : list of candidate words for each clue in JSON format

# processing of the grid filling :
 All the scripts are stored in the "src" folder
- 1st step : Run the script [converter.py](./grid_filling/src/converter.py) to process the puzzle2.json to convert it into a python file crossword_grid containing  a JSON structure with every clue, their direction and the length of the word that matches the clue.
- 2nd step : solve the crossword running the script [solver.py](./grid_filling/src/solver.py), using Z3 solving considering that the grid filling is a SMT problem. 

# output :
The output is sored in the "data" folder
- [crossword_output.txt](./grid_filling/data/crossword_output.txt) : grid of the crossword filled in a .txt format
