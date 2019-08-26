### Requirements

* Python 3.7
* PostgreSQL
* Node.js/npm

### Setup

Clone the repo:
``` bash
git clone
```

Create virtual environment:
``` bash
python3.7 -m venv .env
```

Activate the virtual environment:
``` bash
source ./env/bin/activate
```

Install all python dependencies:
``` bash
pip install -r requirements.txt
```

Install all javascript dependencies:
``` bash
npm install
```

### Deploy

``` bash
heroku apps:create -a my-app
heroku buildpacks:set heroku/python
heroku buildpacks:add --index 1 heroku/nodejs

git push heroku master
```
