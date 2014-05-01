Install the python packages
-----
sudo easy_install pip
sudo aptitude install virtualenv
virtualenv --no-site-packages venv
source venv/bin/activate
pip install -r requirements.txt

Install pandoc
-----
http://johnmacfarlane.net/pandoc/installing.html

Make a settings file
-----
Create a python file nameed `settings.py` in the root directory.

```python
TS_URL = "http://mytorrentserver"
TS_USERNAME = "user"
TS_PASSWORD = "pass"
```

Build
-----
Now you can build the docs.

Run `python build.py` to build the auto generated docs.

This scrapes the REST api docs, and Django model docs.

After you have ran `python build.py` to build the auto docs,you don't need to run it again until the REST api or Django models change.

From this point on you can just run `make html` to make the html docs
(on Windows this is make.bat)



