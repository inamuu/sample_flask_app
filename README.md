sample_flask_app
---

## Reference Book

「ゼロからFlaskがよくわかる本」

## Setup

Setup python virtual environment.

```sh
python -m venv ~/.venv/sample_flask_app
source ~/.venv/sample_flask_app/bin/activate
```

Install python libraries.

```sh
pip install -U pip
pip install -r requirements.txt
```

## How to Run server

```sh
FLASK_APP=flask_blog
flask run
```

## UnitTest

```sh
python test_flask_blog.py
```

## coverage test

Run coverage test

```sh
coverage run -m unittest
.
----------------------------------------------------------------------
Ran 1 test in 0.094s

OK

```

Report test coverage

```sh
coverage report -m
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
flask_blog/__init__.py            15      0   100%
flask_blog/config.py               6      0   100%
flask_blog/models/entries.py      14      4    71%   12-14, 17
flask_blog/scripts/db.py           8      0   100%
flask_blog/views/__init__.py       0      0   100%
flask_blog/views/entries.py       51     22    57%   19-27, 32, 36-37, 42-43, 48-54, 59-63
flask_blog/views/views.py         32      1    97%   38
------------------------------------------------------------
TOTAL                            126     27    79%

```

Export coverage results to html files

```sh
coverage html
```
