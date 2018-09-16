"""

	Title:	run.py
    Pkg:    05_Flask02
	Date:	16.09.2018
	Author:	Eskil Uhlving Larsen

"""
from blog import app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
