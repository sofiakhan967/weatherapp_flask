from flask import Flask ,json , render_template,request
import requests
import math
app = Flask(__name__)

@app.route('/' , methods=['POST' , 'GET'])
def weather():
	#if request.method=="POST":
		#cityname=(request.form['cityname'])
		#temperature=request.form['temperature']

	baseurl='https://api.openweathermap.org/data/2.5/weather?'
	apikey="03c01b50813d8c770b33ac1cfc3fc15d"
	cityname= 'delhi'
	url = baseurl + "q=" + cityname + "&appid=" +apikey
	response=requests.get(url).json()
	weather_data={
							'temperature':math.floor(response['main']['temp']-275.15),
							'humidity' :(response['main']['humidity']),
							'description' :(response['weather'][0]['description']) 
							}
		#sreturn weather_data
	return render_template('index.html' , weather_data= weather_data , cityname=cityname) 		

	#else:
		#return 'check internet'

if __name__ == '__main__':
	app.run(debug=True , port=8000)



