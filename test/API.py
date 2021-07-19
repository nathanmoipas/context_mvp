from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

first_launch = False
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable = False)
    url = db.Column(db.String(1000), nullable = False)
    duration = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return "Video(id=(%d), name=(%s), url(%s), duration(%d))" % (id,name,url,duration)
if first_launch == True:
    db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument('name', type= str, help="Name of the video")
video_put_args.add_argument('url', type= str, help="Url of the video")
video_put_args.add_argument('duration', type= float, help="Duration of the video")

videos = {
}

def abort_if_videos_id_doesnt_exist(videos,video_id):
    if video_id not in list(videos.keys()):
        abort(404,message = "video_id doesn't exist")

def abort_if_video_id_exist(videos,video_id):
    if video_id in videos:
        abort(409, message= "Video already exist")

class Video(Resource):
    def get(self, video_id):
        abort_if_videos_id_doesnt_exist(videos,video_id)
        return videos[video_id]
    def put(self, video_id):
        abort_if_video_id_exist(videos,video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
    def delete(self,video_id):
        abort_if_videos_id_doesnt_exist(videos,video_id)
        del videos[video_id]
        

    


api.add_resource(Video,'/Video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug = True)