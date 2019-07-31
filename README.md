# AccuWeather
An OMG service to access the AccuWeather APIs.

# Usage
```coffeescript
# Storyscript
weather = accuweather forecast location: "Amsterdam, Netherlands"
log info msg: weather.WeatherText
```
