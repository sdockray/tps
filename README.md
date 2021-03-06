The Public School
=================

# Pre-installation

1. Install MongoDB (instructions for OSX are [http://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/](here))

2. Make sure pip is installed (for OSX: "sudo easy_install pip")

3. Make sure virtualenv is installed. If not: "pip install virtualenv"

# Installation

```
git clone https://github.com/sdockray/tps.git
cd tps
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Before starting the server

Before starting the server, you need some data. There are various command line utilities to populate the database with fake data. Run the following commands:

```
python manage.py user create_admin
```
creates an admin with name "tps" and password "tps"

```
python manage.py school create
python manage.py school create -s berlin
python manage.py school create -s brussels
python manage.py school create -s la
```
creates 3 schools plus the default school. You can omit any of the last 3 or add as many more as you want.

```
python manage.py user fake_users -n 25
```
creates 25 fake users. all of them will have "tps" for a password
```
python manage.py proposal fake_proposals -n 40
```
creates 40 fake proposals with randomized people interested in each proposal.
```
python manage.py event fake_places -n 10
python manage.py event fake_events -n 10
```
creates 10 fake places and 10 fake class events.
```
python manage.py event fake_discussions -n 30
```
creates 30 fake discussions

# Starting the server

At this point, you can start the server and play around. That is simply:

```
python wsgi.py
```

Now visit http://localhost:5000/


# Configuring things

If you need to delete all the users, places, events, or proposals, do the following:

```
python manage.py event delete_events
python manage.py event delete_places
python manage.py proposal delete_all
python manage.py user delete_all
```

You will probably have noticed that the development server is already running in "multi-school" mode. (Each school is run as its own application, but they all share the same database. More on this later, but for now, if you want to add more schools, simply add to the list in _wsgi.py_!) You can add a user to the committee for a school by doing, for example:

```
python manage.py dan add_user -u sdockray -s la
```

and then the following commands to remove a user or clear out all committees

```
python manage.py dan remove_user -u username -s schoolname
python manage.py dan delete_all
```