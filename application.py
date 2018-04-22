import os
from flask import Flask,redirect

try:

	app = Flask(_name_)

	@app.route('/')
	def hello():
	    return redirect("https://adriandarian.github.io/blindsight", 
code=302)

	@app.route('/live', methods=['POST'])
	def info():
		req_data = request.get_json()
		print req_data

	if _name_ == '_main_':
	    # Bind to PORT if defined, otherwise default to 5000.
	    port = int(os.environ.get('PORT', 5000))
	    app.run(host='127.0.0.1', port=port)


except Exception as e:
	with open("logg.txt", "w") as logfile:
		logfile.write(str(e.what()))
