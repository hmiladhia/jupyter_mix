import copy
import json

def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_ipynb(notebook, notebook_path):
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f)

# Reading the notebooks
first_notebook = read_ipynb('first_notebook.ipynb')
second_notebook = read_ipynb('second_notebook.ipynb')

# Copying the notebook
final_notebook = copy.deepcopy(first_notebook)

# Concatenating the notebooks
final_notebook['cells'] = first_notebook['cells'] + second_notebook['cells']

# Saving the new notebook 
write_ipynb(final_notebook, 'final_notebook.ipynb')