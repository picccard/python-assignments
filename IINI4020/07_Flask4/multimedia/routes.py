import os
from flask import render_template, request, url_for
from multimedia import app
# {% include svg_file %}


@app.route('/')
def index():
    videos = [f for f in os.listdir(os.path.join(
        app.static_folder, 'video')) if f.endswith('mp4')]
    videos_count = len(videos)

    svg = [f for f in os.listdir(os.path.join(
        app.static_folder, 'svg')) if f.endswith('svg')]
    svg_count = len(svg)
    return render_template("index.html", title='Home', videos=videos, videos_count=videos_count, svg=svg, svg_count=svg_count)


@app.route('/video/<filename>')
def show_video(filename):
    video = url_for('static', filename='video/' + filename)
    return render_template('video.html', title=filename, video=video)


@app.route('/svg/<filename>')
def show_svg(filename):
    svg = url_for('static', filename='svg/' + filename)
    return render_template('svg.html', title=filename, svg_file=svg)
