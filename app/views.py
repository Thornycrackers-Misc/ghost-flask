from app import app, db
from app.models import Post
from flask import render_template, request, jsonify, url_for, redirect


# pylint: disable=E1101
# no member


@app.route('/')
@app.route('/posts')
def posts_index():
    """
    Returns a page that lists all of the posts
    """
    posts = Post.query.all()
    return render_template('posts.html', posts=posts, post=None)


@app.route('/posts/<post_id>')
def posts_index_single(post_id=None):
    """
    When you click on a post from the post listing this
    will pass back the post to render the html. This should
    be done with AJAX to stop reloading
    """
    posts = Post.query.all()
    post = Post.query.get(post_id)
    return render_template('posts.html', posts=posts, post=post)


@app.route('/editor/<post_id>')
def editor_edit_post(post_id=None):
    """
    Returns a post to be edited inside
    of the editor
    """
    post = Post.query.get(post_id)
    return render_template('ghostdown.html', post=post)


@app.route('/editor')
def editor():
    """
    Renders the editor for creating a new post
    """
    return render_template('ghostdown.html')


@app.route('/editor/save', methods=['POST'])
def editor_save():
    """
    This is where the AJAX call from the editor
    comes to save the post. It will either update
    an existing post or it will create a new one
    """
    markdown = request.form.get('markdown')
    html = request.form.get('html')
    title = request.form.get('title')
    if 'post_id' in request.form:
        post_id = int(request.form.get('post_id'))
        edit_post = Post.query.get(post_id)
        edit_post.markdown = markdown
        edit_post.html = html
        edit_post.title = title
        db.session.add(edit_post)
        db.session.commit()
        return jsonify(saved_success=True, new_post=None, post_id=None)
    else:
        new_post = Post(markdown=markdown, html=html, title=title);
        db.session.add(new_post)
        db.session.commit()
        return jsonify(saved_success=True, new_post=True, post_id=new_post.id)



@app.route('/posts/delete/<int:post_id>')
def post_delete(post_id):
    """
    Deletes a post
    """
    delete_post = Post.query.get(post_id)
    db.session.delete(delete_post)
    db.session.commit()
    return redirect(url_for('posts_index'))



@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response 
