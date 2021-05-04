# ChaoAdventure

The Chao Adventure. Coming soon!

### Installation
Requires Python. Docker build available. No other current requirements - just run.

### Docker setup

1) Install docker on your system
2) `docker build -t chao-adventure .` in the main `/ChaoAdventure` directory.
3) `docker run -it --rm chao-adventure` should play Chao Adventure!

### Local build
`python chao_adventure/main.py` should play Chao Adventure!

### Running unit tests
`python -m unittest discover -s tests` in the main `/ChaoAdventure` directory.
