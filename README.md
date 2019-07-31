# _AccuWeather_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)
[![Build Status](https://travis-ci.com/omg-services/accuweather.svg?branch=master)](https://travis-ci.com/omg-services/accuweather)
[![codecov](https://codecov.io/gh/omg-services/accuweather/branch/master/graph/badge.svg)](https://codecov.io/gh/omg-services/accuweather)

An OMG service to access the AccuWeather APIs.

## Direct usage in [Storyscript](https://storyscript.io/):

##### Forecast
```coffee
weather = accuweather forecast location: "Amsterdam, Netherlands"
log info msg: weather.WeatherText
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### Forecast
```shell
$ omg run forecast -a location=<LOCATION> -e API_KEY=<API_KEY>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/accuweather/blob/master/LICENSE).
