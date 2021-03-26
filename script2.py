import nbformat

first_notebok = nbformat.read('first_notebok.ipynb', 4)
second_notebok = nbformat.read('second_notebok.ipynb', 4)

nb.cells = first_notebok.cells + second_notebok.cells

nbformat.write(nb, 'final_notebook.ipynb')
