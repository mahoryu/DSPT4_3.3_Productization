# DSPT4 Twitoff Web App

## Installation

TODO: instructions for git clone

## Setup

TODO: instructions for virtual environment

Also setup a database (Linux/Mac):

```shell script
FLASK_APP=web_app flask db init
FLASK_APP=web_app flask db migrate
FLASK_APP=web_app flask db upgrade
```
(ignore ```shell script FLASK_APP=web_app``` on Windows)

## Usage

```shell script
# Mac:
FLASK_APP=web_app flask run

# Windows:
export FLASK_APP=web_app # one-time thing, to set the env var
flask run
```
