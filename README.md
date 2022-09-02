<div align="center">

# Strava stats api for athelete monitoring

</div>

**NOTE: This repo is work in progress**

## Why? [![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)](http://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action)

The purpose of this api is to track multiple athlete's stats via their strava profile and aggerate their data to track and monitor their performance over time.

The data can be used to compare peformance over a period of time to tweak atheletes training plan.

## Directory structure

```
|_virtualenv
    |_Include
    |_Lib
    |_Scripts
|_StravaStats
    |_api
    |_libs
    |_models
|_setup.py
|_requirements.txt

```

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)

- [Strawberry](https://strawberry.rocks/)

- [pydantic](https://pydantic-docs.helpmanual.io/)

- [terraform](https://www.terraform.io/)

## Strava API

Strava API can be accessed [here](https://developers.strava.com/docs/reference/).

If you wish to fork this repo, please create an app [here](https://developers.strava.com/docs/reference/) to get an API key.
