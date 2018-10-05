"""

	Title:	run.py
    Pkg:    06_Flask03
	Date:	xx.xx.2018
	Author:	Eskil Uhlving Larsen

"""
from blog import app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
