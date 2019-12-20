import os
import sys
import json
import requests
import pytz
from datetime import datetime, timedelta
from flask import Flask, request



app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])

def webhook():
    data = request.get_json()#receives all POST information  
    
    '''
    To parse message data into a format that the bot can understand
    '''
    def run_if_flag_is_true(x, y):
        if flag != 1:


            def check_for_digit(a):
                if a[2].isdigit() == True:
                    d = messages.lower().split(" ")[3]
                    a[2] = a[2] + d
                    a[2] =  "".join(a[2]).lower()
                else:
                    a[2] = a[2]
                return a[2]

            def check_for_length(a):

                check_for_digit(a)
                if len(a[2]) == 3:
                    c =  "0" + a[2][0:]
                    a[2] = c
                else:
                    a[2] = a[2]

                return a[2]
                        

            def parse_user_input(split_message):



                check_for_length(a)
                inte = int(a[2][0:2])
                am_pm = a[2][2:]
                to_subtract = ["04am", "07am","10am", "04pm","07pm","10pm"]
                to_add = ["02am", "05am","08am","02pm","05pm","08pm"]
                
                if a[2] in to_subtract:
                    inte = inte - 1 
                elif a[2] in to_add:
                    inte = inte + 1
                elif a[2] == "11am":
                    inte = inte + 1
                    am_pm = "pm"
                elif a[2] == "11pm":
                    inte = inte +1
                    am_pm = "am"
                elif a[2] == "01pm":
                    inte = 12
                    am_pm = "pm"
                elif a[2] == "01am":
                    inte = 12
                    am_pm = "am"
                else:
                    a[2] = a[2]


                compiled_time = str(inte)+am_pm
                a[2] = compiled_time
                check_for_length(a)
                b = a[1:3]
                b = " ".join(b).lower()
                
                return b


            tz = pytz.timezone('US/Eastern')
            ct = datetime.now(tz=tz).strftime("%A %I%P").lower()


            def convert(x):
                converted = datetime.utcfromtimestamp(x).strftime('%A %I%p').lower()

                return converted


            
            
                


            try:

                n = len(json_data['list'])-1


                day_1 = convert(json_data['list'][0]['dt'])
                day_2 = convert(json_data['list'][n-1]['dt'])


                for nums in range(len(json_data['list']) -1):
                    
                    if convert(json_data['list'][nums]['dt'])==parse_user_input(a):
                        day = convert(json_data['list'][nums]['dt'])
                        description = json_data['list'][nums]['weather'][0]["description"]
                        current_temp = json_data['list'][nums]['main']['temp']
                        max_temp = json_data['list'][nums]['main']['temp_max']
                        min_temp = json_data['list'][nums]['main']['temp_min']
                        pressure = json_data['list'][nums]['main']['pressure']

                        humidity = json_data['list'][nums]['main']['humidity']

                        weather_type = json_data['list'][nums]['weather'][0]['main']
                        

                        cloudiness = json_data['list'][nums]['clouds']['all']
                        wind_speed = json_data['list'][nums]['wind']['speed']

                        def degToCompass(x):#To convert weather directions ito a readable format 
                                val=int((wind_speed/22.5)+.5)
                                arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
                                return arr[(val % 16)]

                        wind_direction = degToCompass(json_data['list'][nums]['wind']['deg'])
                        
                        msg = "Hey {}, here is the upcoming weather conditions in the University on {}{} {} \n \nDescription: {}\nTemperature: {} F\n Maximum Temperature: {} F\nMinimum Temperature: {} F\nAir Pressure: {} bars\nHumidity: {}%\nWeather type: {}\ncloudiness: {}% \nwind speed: {} m/h \nwind Direction: {}\n\nTo summon me, send a message starting with 'weather weekday time(am/pm)'.\nThe range of days I can forecast weather at this very moment is from {} to {}. Thank you!".format (data['name'],c,emoji.emojize(":sun_behind_small_cloud:"),emoji.emojize(":cloud_with_rain:"), description, current_temp,max_temp, min_temp,pressure,humidity,weather_type, cloudiness, wind_speed, degToCompass(wind_direction),day_1, day_2)
                        send_message(msg)
                        
                        break

                        
                    else:
                        n = n -1
                        if n == 0:
                            msg = "I cannot access data for that given date. For now, I can forecast weather if the day is between {} to {}".format(day_1, day_2)
                            send_message(msg)
            except NameError:
                msg = "Hey {}, I cannot access weather data. Try again with the information as weather weekday time(ampm). For example: @weather sunday 12pm.".format(data['name'])
                send_message(msg)
            except ValueError:
                msg = "Hey {}, I cannot access weather data. Try again with the information as weather weekday time(ampm). For example: @weather sunday 12pm.".format(data['name'])
                send_message(msg)
            except TypeError:
                try:
                    msg = "Hey {}, some details might be missing. Try again with the format: weather weekday time".format(data['name'])
                    send_message(msg)
                except TypeError:
                    print("cron stops here")

            except Exception as e:
                print("type error:" + str(e))  #function that parses weather data for the next five days and brken down into each hour, data is got from OpenWeatherApi
    

#function to check for rain and temperature data and determine whether

    def check_rain_and_temp():


        payload ={'q': "Columbia", 'units': 'imperial', 'APPID':'30cdffc331ee3350cc4a2a433f4f195d'}
        json_data =requests.get('https://api.openweathermap.org/data/2.5/forecast?',params=payload).json()
        cold_days = []
        def convert(x):
            converted = datetime.utcfromtimestamp(x).strftime('%A %I%p').lower()
            return converted
        for nums in range(len(json_data['list']) -1):
            if (json_data['list'][nums]["main"]["temp_min"]) < 50:
                cold_days.append(convert(json_data['list'][nums]['dt']))

        all_rainy_times = []
        for nums in range(len(json_data['list']) -1):
            if json_data['list'][nums]["weather"][0]["main"].lower() == "rain": #check for other ways weather api sends out data 
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
        
 


        if rain:

            d = []
            
            for day in all_rainy_times:

                if day[0:2] == tommorow[0:2]:
                    d.append(day)

                    
                    
                    msg = "Tommorow: {}  will be raining {}. \n\nIf you plan to walk outside remember to carry an umbrella{} or a raincoat".format( ', '.join(d), "\N{Umbrella With Rain Drops}", "\N{Umbrella}" )
            print(msg)


        if temp:
            c = []
            for cold in cold_days:
                if cold[0:2] == tommorow[0:2]:
                    c.append(cold)
                    msg = "Tommorow: {}. \nTemperatures will also fall to below 40Fs. \n\nHave something warm on!{}".format(', '.join(c), "\N{Coat}" )
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

            msg = "Tommorow: {} will be raining {}. \n\nIf you plan to walk outside remember to carry an umbrella{} or a raincoat.\n\nOn the same day, {} temperatures may also fall to below 40F. \n\nSomething warm may suffice{}.".format(', '.join(d), "\N{Umbrella With Rain Drops}", '\N{Umbrella}', ', '.join(c), "\N{Coat}")
            print(msg)

        send_message(msg)

    try:
        



        if request.method == 'POST' and data['name'] != 'claflin-weather ':
            payload = {'q': "Orangeburg", 'units': 'imperial', 'APPID':'30cdffc331ee3350cc4a2a433f4f195d'}
            json_data = requests.get('https://api.openweathermap.org/data/2.5/forecast?', params=payload).json()
            ##For scheduling of check_rain and temp function 
            
            


            messages = data['text']
            a = messages.lower().split(" ")[0:3]
            

            weekdays = ['monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']
            


            def empty_response():
                print("ok")
            flag = 0

            if a[0] == "weather" and a[1] in weekdays and len(a) > 1:
                c = (a[1] + " at " + a[2]).lower()

                
                
                run_if_flag_is_true(a,c)

            else: 
                if a[0] == "weather":
                    msg = "Hey {}, some details might be missing. Try again with the format: weather weekday time".format(data['name'])
                    send_message(msg)
                else:
                    empty_response()
        else:
            print("The data returned was either empty or came from a cron job")

    

            
#error handling for mistakes the user might input 
    except IndexError:
        msg = "Hey {}, some details might be missing. Try again with the format: weather weekday time".format(data['name'])
        send_message(msg)
    except TypeError:
        try:
            msg = "Hey {}, some details might be missing. Try again with the format: weather weekday time".format(data['name'])
            send_message(msg)
        except TypeError:
            print("before function")
            check_rain_and_temp()
            print("Error within an error but OK. after function")
            

    except Exception as e:
        print("type error:..... " + str(e))
    
    return 'OK'

#handles all the messages being sent back to groupme
def send_message(msg):


    url  = 'https://api.groupme.com/v3/bots/post'
    print(msg)
    data = {
            'bot_id' : os.getenv('BOT_ID'),
            'text'   : msg,
             }
    request = requests.post(url, json = data)
  
