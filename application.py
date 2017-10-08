#!/usr/bin/python3

from flask import Flask, render_template
from flask import request, redirect
from flask import url_for, jsonify, flash
from functools import wraps
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog Application"

app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create anti-forgery state token


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', state=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code, now compatible with Python3
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;"'
    '"border-radius: 150px;-webkit-border-radius: 150px;"'
    '"-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    return output
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
        # Obtain authorization code
        request.get_data()

        try:
            # Upgrade the authorization code into a credentials object
            code = request.data.decode('utf-8')
            oauth_flow = flow_from_clientsecrets(
                'client_secret.json', scope='')
            oauth_flow.redirect_uri = 'postmessage'
            credentials = oauth_flow.step2_exchange(code)
        except FlowExchangeError:
            response = make_response(json.dumps(
                'Failed to upgrade the authorization code.'), 401)
            response.headers['Content-Type'] = 'application/json'
            return response

        # Check that the access token is valid.
        access_token = credentials.access_token
        url = (
            'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
            % access_token)
        h = httplib2.Http()
        result = json.loads(h.request(url, 'GET')[1])
        response = h.request(url, 'GET')[1]
        str_response = response.decode('utf-8')
        result = json.loads(str_response)

        # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        result = result
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
        if result['issued_to'] != CLIENT_ID:
            response = make_response(
                json.dumps("Token's client ID does not match app's."), 401)
            print "Token's client ID does not match app's."
            response.headers['Content-Type'] = 'application/json'
            return response

        stored_access_token = login_session.get('access_token')
        stored_gplus_id = login_session.get('gplus_id')
        if stored_access_token is not None and gplus_id == stored_gplus_id:
            response = make_response(json.dumps(
                'Current user is already connected.'), 200)
            response.headers['Content-Type'] = 'application/json'
            return response

    # Store the access token in the session for later use.
        login_session['access_token'] = access_token
        login_session['gplus_id'] = gplus_id

    # Get user info
        userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        params = {'access_token': credentials.access_token, 'alt': 'json'}
        answer = requests.get(userinfo_url, params=params)

        data = answer.json()

        login_session['username'] = data['name']
        login_session['picture'] = data['picture']
        login_session['email'] = data['email']

        # see if user exists, if it doesn't make a new one
        user_id = getUserID(login_session['email'])
        if not user_id:
            user_id = createUser(login_session)
        login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;height: 300px;"'
    '"border-radius:150px;-webkit-border-radius: 150px;">'
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?'
    'token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully logged out.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            flash("You are not allowed to access there")
            return redirect('/login')
        return decorated_function


@app.route('/')
@app.route('/menu')
@app.route('/menu/')
def catalogMenu():
    categories = session.query(Categories).all()
    latest_items = session.query(Items).order_by(
        desc(Items.created_date)).limit(5).all()
    return render_template('menu.html',
                           categories=categories,
                           loggedIn='username' in login_session,
                           latest_items=latest_items)


@app.route('/JSON')
@app.route('/JSON/')
@app.route('/json/')
@app.route('/json')
@app.route('/menu/json')
@app.route('/menu/json/')
@app.route('/menu/JSON')
@app.route('/menu/JSON/')
def catalogMenuJSON():
    categories = session.query(Categories).all()
    return jsonify(categories=[r.serialize for r in categories])


@app.route('/catalog/<string:category_name>')
@app.route('/catalog/<string:category_name>/')
def showMenu(category_name):
    category = session.query(Categories).filter_by(name=category_name).one()
    items = session.query(Items).filter_by(category_id=category.id).all()
    return render_template('category.html',
                           category=category,
                           items=items,
                           loggedin='username' in login_session)


@app.route('/catalog/<string:category_name>/json')
@app.route('/catalog/<string:category_name>/json/')
@app.route('/catalog/<string:category_name>/JSON')
@app.route('/catalog/<string:category_name>/JSON/')
def showMenuJSON(category_name):
    category = session.query(Categories).filter_by(name=category_name).one()
    items = session.query(Items).filter_by(category_id=category.id).all()
    return jsonify(items=[r.serialize for r in items])


@app.route('/catalog/<string:category_name>/<string:item_name>')
def showItems(category_name, item_name):
    category = session.query(Categories).filter_by(name=category_name).one()
    item = session.query(Items).filter_by(
        name=item_name, category_id=category.id).one()
    return render_template('item.html',
                           item=item, loggedin='username' in login_session)


@app.route('/catalog/<string:category_name>/<string:item_name>/json')
@app.route('/catalog/<string:category_name>/<string:item_name>/json/')
@app.route('/catalog/<string:category_name>/<string:item_name>/JSON')
@app.route('/catalog/<string:category_name>/<string:item_name>/JSON/')
def showItemsJSON(category_name, item_name):
    category = session.query(Categories).filter_by(name=category_name).one()
    item = session.query(Items).filter_by(
        name=item_name, category_id=category.id).one()
    return jsonify(items=[item.serialize])


# handles the processing when the edit button is clicked


@login_required
@app.route('/catalog/<string:item_name>/edit',  methods=['GET', 'POST'])
def editItemRenderer(item_name):
    item = session.query(Items).filter_by(name=item_name).one()
    # authorization check
    if item.user_id == login_session['user_id']:
        if request.method == 'POST':
            editedItem = session.query(Items).filter_by(name=item_name).one()
            if request.form['edit_name']:
                editedItem.name = request.form['edit_name']
            if request.form['edit_description']:
                editedItem.description = request.form['edit_description']
            if request.form['edit_category']:
                category = session.query(Categories).filter_by(
                    name=request.form['edit_category']).one()
                editedItem.category = category
            session.add(editedItem)
            session.commit()
            flash('%s Item Successfully Edited' % (item_name))
            return redirect(url_for('catalogMenu'))
        else:
            categories = session.query(Categories).all()
            return render_template('editItem.html',
                                   item=item,
                                   categories=categories,
                                   isEdit=True)
    else:
        flash('No permission to edit')
        return redirect(url_for('catalogMenu'))

# handles the processing when the delete button is clicked


@login_required
@app.route('/catalog/<string:item_name>/delete',  methods=['GET', 'POST'])
def deleteItemRenderer(item_name):
    item = session.query(Items).filter_by(name=item_name).one()
    # authorization check
    if item.user_id == login_session['user_id']:
        if request.method == 'POST':
            session.delete(item)
            session.commit()
            flash('%s Successfully Deleted' % (item_name))
            return redirect(url_for('catalogMenu'))
        else:
            return render_template('deleteItem.html', item=item)
    else:
        flash('No permission to delete')
        return redirect(url_for('catalogMenu'))

# handles the processing when the add item button is clicked


@login_required
@app.route('/catalog/<string:category_name>/addItem',  methods=['GET', 'POST'])
def addItemRenderer(category_name):
    if request.method == 'POST':
        category = session.query(Categories).filter_by(
            name=category_name).one()
        newItem = Items(name=request.form['add_name'],
                        description=request.form['add_description'],
                        category=category, user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        flash('New %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('showMenu', category_name=category_name))
    else:
        return render_template('editItem.html',
                               category_name=category_name, isEdit=False)

# handles the processing when the add category button is clicked


@login_required
@app.route('/catalog/category/add', methods=['GET', 'POST'])
def addCategoryRenderer():
    if request.method == 'POST':
        newCategory = Categories(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('catalogMenu'))
    else:
        return render_template('newCategory.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
