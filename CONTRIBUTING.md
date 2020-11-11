# All contributions
Use `pre-commit` to ensure the checks are executed automatically upon commit. To set up `pre-commit`:
```
pip install pre-commit
pre-commit install
```

Code style: `black`

# When changing autocorrection logic
Run this command before and after changes, and paste the output in the comments:
```
python test_all.py quality ; python test_all.py benchmark
```
