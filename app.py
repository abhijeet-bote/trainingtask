from flask import Flask
# ... other required imports ...
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore


app = Flask(__name__)

app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': '1163520467436459',
    'consumer_secret': '7633675af0971a60de63e0a5e0b961fc'
}



# ... create the app ...

app.config['SECURITY_POST_LOGIN'] = '/profile'

db = SQLAlchemy(app)

# ... define user and role models ...

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)

Security(app, SQLAlchemyUserDatastore(db, User, Role))
Social(app, SQLAlchemyConnectionDatastore(db, Connection))

@app.route('/profile')
@login_required
def profile():
    return render_template(
        'fb_profile.html',
        content='Profile Page',
        twitter_conn=social.twitter.get_connection(),
        facebook_conn=social.facebook.get_connection(),
        foursquare_conn=social.foursquare.get_connection())

if __name__ == '__main__':
    app.run('localhost' , '5000', debug = True)