from flask import Flask, render_template, request, redirect, url_for
from store import Post, PostStore
from supabase import create_client, Client

app = Flask(__name__)

# إعداد Supabase
url = "https://biytrshphtxlywabygcc.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJpeXRyc2hwaHR4bHl3YWJ5Z2NjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzczMTE4NjEsImV4cCI6MjA1Mjg4Nzg2MX0.G63kILbsKfvbtHzgMkJjZb8hAoPQG_S1FClE01GBTLY"
supabase: Client = create_client(url, key)

# متغيرات 
post_store = PostStore()
app.current_id = 2

# تحميل المنشورات من Supabase عند بدء التشغيل
def load_posts():
    response = supabase.table('posts').select('*').execute()
    posts = response.data
    for post in posts:
        new_post = Post(id=post['id'],
                        photo_url=post['photo_url'],
                        name=post['name'],
                        date=post['date'],
                        body=post['body'])
        post_store.add(new_post)
        app.current_id = max(app.current_id, new_post.id + 1)

load_posts()

@app.route('/')
def sport():
    return render_template('index2.html')

@app.route('/takafa')
def takafa():
    return render_template('takafa.html')

@app.route('/arabec')
def arabec():
    return render_template('arabec.html')

@app.route('/page1')
def home():
    return render_template('page1.html', posts=post_store.get_all())

@app.route('/post/add', methods=['GET', 'POST'])
def post_add():
    if request.method == 'POST':
        new_post = Post(id=app.current_id,
                        photo_url=request.form['photo_url'],
                        name=request.form['name'],
                        date=request.form['date'],
                        body=request.form['body'])
        post_store.add(new_post)
        app.current_id += 1

        # حفظ البيانات في Supabase بدون id
        data = {
            "photo_url": new_post.photo_url,
            "name": new_post.name,
            "date": new_post.date,
            "body": new_post.body
        }
        response = supabase.table('posts').insert(data).execute()
        print(response)

        print(post_store.get_all())  # طباعة للتأكد من إضافة المنشور الجديد
        return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('post-add.html')

if __name__ == '__main__':
    app.run()