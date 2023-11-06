import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def do():
    if request.method=='POST':
        city=request.form.get('city')
        url = "http://api.weatherapi.com/v1/current.json?key=ff0f42eedc474440891205842230311&q="+city
        response = requests.get(url)
        response2=response.json()
        c=response2['current']['temp_c']
        return render_template("index.html",city=city,temperature=c,id="hide")
    else:
        return render_template("index.html")
app.run()
