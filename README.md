# A Simple Weather Bot for GroupMe 

## Introduction

This was a learning project to get introduced to flask, gunicorn and heroku as a way of running apps online. 

The bot lives in GroupMe and can be called if the text starts with weather dayof week time(am/pm)
For example: Weather Monday 9am which will return anticipated weather for that day and time, the bot cannot get weather for the current day.

The bot also notifies users everyday at a fixed time if rain is expected to fall the next day or if temperature goes below or above a certain temperature 


As of now, the bot's functionality is returning weather conditions :cloud: based on data provided by [OpenWeather API](https://openweathermap.org/api)

I restricted location of the weather API to one place. 

###### screenshots:



![screenshot1](/images/chatbot1.png)

![screenshot2](/images/chatbot2.png)




Credits to [apnorton](http://www.apnorton.com/blog/2017/02/28/How-I-wrote-a-Groupme-Chatbot-in-24-hours/) 