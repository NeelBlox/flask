import instaloader
from flask import  Flask, request, redirect, url_for, render_template
app = Flask(__name__)
L = instaloader.Instaloader()
@app.route('/')
def load_form():
	return render_template('flask.html')
@app.route('/',methods=['POST'])
def upload_image():
    name=request.form['name']
    post_shortcode = request.form['text']
    
    post = instaloader.Post.from_shortcode(L.context, post_shortcode)

    print(post)
    L.download_post(post, target=f'{name}')
    return render_template('flask.html')
if __name__=="__main__":
	app.run()
