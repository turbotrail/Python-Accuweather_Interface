import requests
import datetime
import json
weather_api="http://dataservice.accuweather.com/currentconditions/v1/"
forecast_api="http://dataservice.accuweather.com/forecasts/v1/daily/1day/"
f=open("cityid.txt","r")
city_id=f.read()
f.close()
f=open("apikey.txt","r")
api_key=f.read()
f.close()
weather_data=requests.get(weather_api+city_id+"?apikey="+api_key+"&details=true")
forecast_data=requests.get(forecast_api+city_id+"?apikey="+api_key+"&details=true&metric=true")
#print(weather_api+city_id+"?apikey="+api_key)
if weather_data.status_code==200 and forecast_data.status_code==200 :
    print("Weather response status: ok")
    print("Forecast response status: ok")
else :
    print("Error fetching weather and forecast :"+str(weather_data.status_code)+" and "+str(forecast_data.status_code))
Weather_list=weather_data.json()
f=open("weather_api.txt","w")  # Saving todays weather response in text file for reference
f.write(str(Weather_list))
f.close()

weather_dict=Weather_list[0]
current_temperature=weather_dict.get("Temperature")
current_weather=weather_dict.get("WeatherText")
print("Current date & time:"+str(datetime.datetime.now()))
print("Citys current temperature:"+str(current_temperature["Metric"].get("Value"))+"^c"+" / "+str(current_temperature["Imperial"].get("Value"))+"^F")
realfeel_temperature=weather_dict.get("RealFeelTemperature")
print("Real feel:"+str(realfeel_temperature["Metric"].get("Value"))+"^c"+" / "+str(realfeel_temperature["Imperial"].get("Value"))+"^F")
print("Weather condition: "+current_weather)
uv_ind=weather_dict.get("UVIndex")
uv_info=weather_dict.get("UVIndexText")
print("UV Index: "+str(uv_ind)+" , "+uv_info)
print("-...............................-")
forecast_main_dict=forecast_data.json()
#print(forecast_main_dict)
f=open("forecast_api.txt","w") # Saving Next day forecast response in text file for reference
f.write(str(forecast_main_dict))
f.close()
forecast_dict=forecast_main_dict.get("DailyForecasts")
#print(forecast_dict)
temperature_forecast= forecast_dict[0].get("Temperature")
#print(temperature_forecast)
minimum_temperature=temperature_forecast["Minimum"]["Value"]
print("Tomorrow's forecast:"+str(datetime.date.today() + datetime.timedelta(days=1)))
print("Minimum Temperature:"+str(minimum_temperature)+" ^c")
maximum_temperature=temperature_forecast["Maximum"]["Value"]
print("Maximum Temperature:"+str(maximum_temperature)+" ^c")
air_forecast= forecast_dict[0].get("AirAndPollen")
air_quality=air_forecast[0].get("Category")
print("Air quality: "+air_quality)
UV_index=air_forecast[5].get("Category")
print("UV Index: "+UV_index)
day_forecast=forecast_dict[0].get("Day")
day_weather=day_forecast.get("LongPhrase")
print("Day time weather: "+day_weather)
night_forecast=forecast_dict[0].get("Night")
night_weather=night_forecast.get("LongPhrase")
print("Night time weather: "+night_weather)
