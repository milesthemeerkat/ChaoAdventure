# ChaoAdventure

The Chao Adventure. Coming soon!

### Installation
Chao Adventure is built with Python 3.7. It's recommended you create a virtual environment of Python 3.7 to install the project.

### Docker setup

1) Install docker on your system
2) `docker build -t chao-adventure .` in the main `/ChaoAdventure` directory.
3) `docker run -it --rm chao-adventure` should play Chao Adventure!

### Local build
Install the requirements:
`pip install -r requirements.txt`

After installing the requirements, it's recommended to setup commit hooks:
`pre-commit install`

This will run each added or changed file with every commit through linters. If all goes well, you should see the following after a good commit:
```
black....................................................................Passed
Flake8...................................................................Passed
pylint...................................................................Passed
```
If `black` detects necessary changes, it will update the file automatically!

Then you can play Chao Adventure:
`python chao_adventure/main.py`

### Running unit tests
`python -m unittest discover -s tests` in the main `/ChaoAdventure` directory.
