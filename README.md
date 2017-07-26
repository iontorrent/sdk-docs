Installing dependencies
-----

```bash
virtualenv --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt
```

Alternatively, you can use Docker. First, create docs builder

```
docker build -t sdk-docs-builder .
```

To build, using the repo as current working directory:

```
docker run -t -v $(pwd):/src sdk-docs-builder
```


Building the docs
-----
Just run `make html` to make the html docs
(on Windows this is make.bat).


Updating the api docs
-----
Create a python file named `settings.py` in the root directory. See `settings.py.dist` for an example.

```python
TS_URL = "http://mytorrentserver"
TS_USERNAME = "user"
TS_PASSWORD = "pass"
```

Run `python generate_api_docs.py` to update the auto generated docs.

After you have ran `python generate_api_docs.py` you don't need to run it again until the api schema changes.

