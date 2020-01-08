<p align="center"><img src="app/static/img/horizontal.png" alt="BookLibrary" height="200px"></p>

# BookLibrary
Simple Book library application written on flask with SQLite database.

## Features
* user login, logout, register, change password, update about-me information
* user borrow/return books, write/delete comments
* administrator add/delete book, update book information
* administrator delete comments

## Screen Shot
Index page:
![index page](https://cloud.githubusercontent.com/assets/7829098/18173715/3e9ccc62-709d-11e6-820d-1cad1e6822b7.png)

User detail page:
![user detail page](https://cloud.githubusercontent.com/assets/7829098/18173713/3e324018-709d-11e6-9a64-b8c7e87b1f2d.png)

Book list page:
![book list page](https://cloud.githubusercontent.com/assets/7829098/18173712/3defdba6-709d-11e6-99f4-aa0471c75af0.png)

Book detail page:
![book detail page](https://cloud.githubusercontent.com/assets/7829098/18173711/3dbdfe92-709d-11e6-8a63-85c64717ac70.png)

## Installation
```sh
git clone https://github.com/magic-akari/BookLibrary.git
cd BookLibrary
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
python3 ./run.py
```

Press CTRL+C to terminate the server.  
use `deactive` to quit the virtual environment.

Python 3 is recommend, meanwhile this project is compatible with python 2.

### Run with Docker

You can run this project with docker by running the following commands:
```sh
docker build -t booklibrary:latest .

docker run -ti -v `pwd`:/app -p 4000:4000 booklibrary:latest
```

By adding the `-v` above, you can make changes in the local files and they will
be reflected inside the docker container. If you want to run it in
"production" mode, skip the above `-v` option.

## Dependencies

- [Flask](https://github.com/mitsuhiko/flask)
- [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)
- [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy)
- [Flask-Login](https://github.com/maxcountryman/flask-login)
- [Flask-WTF](https://github.com/lepture/flask-wtf)
- [Bootstrap](http://getbootstrap.com/)
- [Flask-Bootstrap](https://github.com/mbr/flask-bootstrap)
- [Markdown](https://pythonhosted.org/Markdown/)
- [Flask-PageDown](https://github.com/miguelgrinberg/Flask-PageDown)
- [Flask-Uploads](https://packages.python.org/Flask-Uploads/)
- [Bootstrap File Input](https://github.com/kartik-v/bootstrap-file-input)

## LICENSE
The MIT License (MIT)

Copyright (c) 2016 阿卡琳

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
