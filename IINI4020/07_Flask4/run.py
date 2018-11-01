"""

	Title:	run.py
    Pkg:    07_Flask04
	Date:	01.11.2018
	Author:	Eskil Uhlving Larsen

"""
from multimedia import app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
