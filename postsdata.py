from flask import Flask, render_template

app = Flask(__name__)

def generate_post_content(post_id):
    return f"Content of post {post_id}"

@app.route('/posts')
def postall():
    # Generate dummy data for demonstration
    num_posts = 5  # Number of posts to generate
    posts = [
        {'id': i, 'title': f'Post {i}', 'content': generate_post_content(i)}
        for i in range(1, num_posts + 1)
    ]
    return render_template('postall.html', posts=posts)

@app.route('/posts/<int:post_id>')
def single_post(post_id):
    # Retrieve data for a single post based on the provided post_id
    post_data = {'id': post_id, 'title': f'Post {post_id}', 'content': generate_post_content(post_id)}
    return render_template('postsingle.html', post=post_data)


if __name__ == '__main__':
    app.run(debug=True)
