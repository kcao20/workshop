# Team Pirap: Kevin Cao, Han Zhang
# SoftDev
# K19: A RESTful Journey Skyward
# 2021-11-23

# Q0: What happens if you remove render_template from this line?
from flask import Flask, render_template
import urllib3
import json

app = Flask(__name__)


@app.route("/")
def home_page():
    http = urllib3.PoolManager()
    r = http.request(
        'GET', 'https://api.nasa.gov/planetary/apod?api_key=PxL3Eff2wvlbpZ9B6gF6Z1ORyovxbYCMdarvELIz')
    data = json.loads(r.data.decode('utf-8'))
    return render_template('main.html', image=data["hdurl"], title=data["title"], description=data["explanation"])


if __name__ == "__main__":
    app.debug = True
    app.run()
