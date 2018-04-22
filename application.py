import os
from flask import Flask,request, render_template, random

points = []

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("https://adriandarian.github.io/blindsight", code=302)

@app.route('/live', methods=['POST'])
def live():
	req_data = request.get_json(force=True)
	points.append([req_data["angle"], req_data["distance"]])
	print points
	return render_template('live.html', bot=points)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port, debug=True)
