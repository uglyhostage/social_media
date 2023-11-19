from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///network.db"
db = SQLAlchemy(app)
class Post(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    title = db.Column(db.String(50),nullable = False)
    content = db.Column(db.Text())

    def __repr__(self):
        return f"postid {self.id}, post title {self.title}"

@app.route("/")
def index():
    #db.session.add(Post(id = 1,title = "myfirstpost", content = "content"))
    #db.session.commit()
    posts = Post.query.all()
    #return redirect(url_for("indexx"))
    #return "<a href='http://127.0.0.1:3333/boo'>press me</a>" 
    return f"{posts}"


@app.route("/boo")
def indexx():
    return render_template("index.html")


with app.app_context():
    db.create_all()
app.run(port=3333,debug=True)

