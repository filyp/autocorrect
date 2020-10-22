# All contributions
Keep the code clean with `flake8`. Use `pre-commit` to ensure the checks are executed automatically upon commit. To set up `pre-commit`:
```
pip install pre-commit
pre-commit install
```

# When changing autocorrection logic
Run this command before and after changes, and paste the output in the comments:
```
python tests.py quality ; python tests.py benchmark
```
