from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource

app = Flask(__name__)

#전체 계시글을 불러오는 api
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
   # return jsonify({'result':'success', 'data': {"feed1":"data", "feed2":"data2"}})
	return {'result':'success', 'data': {"feed1":"data", "feed2":"data2"}}

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
   print(feed_id)
   return jsonify({'result':'success', 'data': {"feed1":"data"}})

