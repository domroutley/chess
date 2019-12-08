# chess

## Python version
Version 3.8.*  
To install this specific version of Python use `apt install python3.8`  
You can run it with `python3.8`, or use a virtual env

### Virtual environment for development
To create a virtual environment for python3.8 in a subfolder of your current directory called .venv, you can run
```bash
apt install python3.8-venv
python3.8 -m venv .venv
```

## Testing
```bash
# Run tests and generate report
coverage run -m unittest
# View report
coverage report
# Generate html report
coverage html
```
coverage run and report are bundled in the test script in scripts/test  
Run it with `scripts/test`

### Manual Testing
Create a file called `.test.py` in the root of the repository. You can then import and test stuff manually.  
```python
## .test.py
import game
print(game.board.chess_board())
```
