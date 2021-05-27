from flask import Flask, render_template, jsonify, request
from model import connect_to_db
import crud
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"

###################################################
# First, we list routes that are for AJAX requests.
# These routes will return JSON.
# Since we want React to do most of the frontend work,
# we'll mainly be using our Flask app as an API.
@app.route('/api/login', methods=['POST'])
def login():
    email = request.json.get('email') #thanks to that content-type header!
    password = request.json.get('password')
    user = crud.get_user_by_email(email)
    user_info = None
    if user and user.password == password:
        user_info = {
            'name': user.name,
            'email': user.email,
            'user_id': user.user_id
            }
    print('*' * 20)
    print(user_info)
    return jsonify(user_info)


# need to work on the front end of bidding for this route
@app.route('/api/bid', methods=['POST'])
def place_bid():
    listing_id = request.json.get('listingId')
    user_id = request.json.get('userId')
    bid_amount = request.json.get('bidAmount')
    timestamp = datetime.now()
    listing = crud.get_melon_by_id(listing_id)
    result = None
    if timestamp < listing.end_date:
        bid = crud.create_bid(user_id, listing_id, bid_amount, timestamp)
        print(bid)
        result = {'listingId': listing_id, 
                'userId': user_id,
                'bidAmount': bid_amount,
                'status': 'Oh yeah! Juicy goodness is in your future!'
                }
    else:
        result = {'status': 'You missed out. Our condolences. :(  Try another bid!'}
    return jsonify(result)


@app.route('/api/listings')
def get_listings():
    listings = crud.get_melon_listings()
    result = []
    
    for listing in listings:        
        top_bid_record = crud.get_top_bid(listing.melon_id)
        top_bid = None
        top_bidder = None
        print(top_bid_record)
        if top_bid_record:
            top_bid = top_bid_record.bid_amount
            top_bidder = top_bid_record.bidder.name
                
        listing_info = {
            'listing_id': listing.melon_id,
            'image_url': listing.category.melon_img_url,
            'category': listing.category.name,
            'color': listing.category.color,
            'is_seedless': listing.category.is_seedless,
            'name': listing.name,
            'seller': listing.seller.name,
            'end_date': listing.end_date,
            'description': listing.description,
            'start_price': listing.start_price,
            'top_bid': top_bid,
            'top_bidder': top_bidder, 
        }
        result.append(listing_info)
        
    return jsonify(result)


###################################################
# Our Flask app only has one route that renders HTML.
# React Router handles the rest of the route logic for us instead of Flask
# so that we can have a single-page app with no page refreshes.
# The logic below makes sure that our app displays main.html 
# no matter which url the user used to get to our site.
# For more information about the Flask routing rules used below, see...
# https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('main.html')

###################################################
if __name__ == "__main__":
    # connect_to_db(app)
    connect_to_db(app, "postgresql:///test_db")
    app.run(debug=True, host='0.0.0.0')