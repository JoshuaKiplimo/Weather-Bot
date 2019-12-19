from datetime import datetime, timedelta
from apscheduler.schedulers.background import BlockingScheduler
import requests
import json 
import os
import sys

import pytz









def check_rain_and_temp():
  payload ={'q': "Columbia", 'units': 'imperial', 'APPID':'30cdffc331ee3350cc4a2a433f4f195d'}
  json_data =requests.get('https://api.openweathermap.org/data/2.5/forecast?',params=payload).json()
  cold_days = []




  def convert(x):
    converted = datetime.utcfromtimestamp(x).strftime('%A %I%p').lower()

    return converted
  for nums in range(len(json_data['list']) -1):

      if (json_data['list'][nums]["main"]["temp_min"]) < 40:
          cold_days.append(convert(json_data['list'][nums]['dt']))

  all_rainy_times = []
  for nums in range(len(json_data['list']) -1):
      
          
      if json_data['list'][nums]["weather"][0]["main"] == "Rain":
          all_rainy_times.append(convert(json_data['list'][nums]['dt']))

  
  def unique_elements_in_order(sequence):




    seen = set()
    sequence = [x for x in sequence if not (x in seen or seen.add(x))]
    return sequence



    specific_days_with_rain = []
    for days in all_rainy_times:
        specific_days_with_rain.append(days[0:-5])
        specific_days_with_rain = unique_elements_in_order(specific_days_with_rain)


    specific_cold_days= []
    for cold in cold_days:
        specific_cold_days.append(cold[0:-5])
        specific_cold_days = unique_elements_in_order(specific_cold_days)
        
    tz = pytz.timezone('US/Eastern')
    tommorow = (datetime.now(tz=tz)+ timedelta(days=1)).strftime("%A").lower()
    rain = tommorow in specific_days_with_rain and tommorow not in specific_cold_days
    temp = tommorow in specific_cold_days and tommorow not in specific_days_with_rain
    temp_and_rain = tommorow in specific_cold_days and tommorow in specific_days_with_rain
    #none = tommorow not in specific_cold_days and tommorow not in specific_days_with_rain

    if rain:
        d = []
        
        for day in all_rainy_times:

            if day[0:2] == tommorow[0:2]:
                d.append(day)

                
                
                msg = "Hey {}, \ntommorow: {} will be raining {}, if you plan to walk outside remember to carry an umbrella or a raincoat".format('honors class of 2023', ', '.join(d), "\N{Umbrella With Rain Drops}" )
        print(msg)


    if temp:
        c = []
        for cold in cold_days:
            if cold[0:2] == tommorow[0:2]:
                c.append(cold)
                msg = "Hey {}, \ntommorow: {}, Temperatures will also fall to below 40F {}. Have something warm on!".format('honors class of 2023', ', '.join(c), "\N{Freezing Face}" )
        print(msg)

    if temp_and_rain:
        d = []
        for day in all_rainy_times:
            if day[0:2] == tommorow[0:2]:
                d.append(day)
        c = []
        for cold in cold_days:
            if cold[0:2] == tommorow[0:2]:
                c.append(cold)
        msg = "Hey {}, \ntommorow: {} will be raining {}, if you plan to walk outside remember to carry an umbrella or a raincoat.\n On the same day, {} temperatures may also fall to below 40F {}, so something warm may suffice".format('Honors Class of 2023', ', '.join(d), "\N{Umbrella With Rain Drops}", ', '.join(c), "\N{Freezing Face}")
        print(msg)

    send_message(msg)

##For scheduling of check_rain and temp function 

    
def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  print(msg)
  data = {
          'bot_id' : os.getenv('BOT_ID'),
          'text'   : msg,
         }
  request = requests.post(url, json = data)

if __name__ == '__main__':

  sched = BlockingScheduler(timezone ='US/Eastern')
  sched.daemonic = False
  job =sched.add_job(check_rain_and_temp, 'interval', seconds=15)

  #print(job)
  #sched.add_job(job_function, 'interval', hours=2)
  a = sched.get_jobs()
  print(a)
  #print_jobs()
  

while True:
  sched.start()
  time.sleep(10)
  sched.shutdown()
  
  


