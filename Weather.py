import requests as req
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('API_key.txt', 'r').read()

CITY = input("Enter the name of the city: ")

#Constructing a URL, appid is the API key which authorizes us to use the API
final_url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

#fetching the data from the API
#The get() method makes what's called an HTTP GET request to the URL we constructed
#After we get the response, we call the .json() method on it
#This converts the raw response data (which comes as a string) into a Python dictionary or list

response = req.get(final_url).json()
if response['cod'] == '404':
    print("City not found")
    exit()
elif response['cod'] == '400':
    print("No name entered to search for")
    exit()

#print(response) #Prints the raw response data, the data is stored in a dictionary

def convert_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius
#Extracting information from the dictionary in a readable format
print()
print(f"Select what you want to know about {CITY} :")
print("""1. Temperature
2. Humidity
3. Pressure
4. cordinates
5. feels_like_temp
6. Country
7. Sunrise
8. Sunset
9. timezone
10. max and min temp
""")

print("Enter 0 to exit")
choice = 1
while choice != 0:
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"The temperature in {CITY} is {convert_to_celsius(response['main']['temp'])} degrees Celsius")
    elif choice == 2:
        print(f"The humidity in {CITY} is {response['main']['humidity']}%")
    elif choice == 3:
        print(f"The pressure in {CITY} is {response['main']['pressure']} hPa")
    elif choice == 4:
        print(f"The cordinates in {CITY} is {response['coord']['lon']}, {response['coord']['lat']}")
    elif choice == 5:
        print(f"The feels like temperature in {CITY} is {convert_to_celsius(response['main']['feels_like'])} degrees Celsius")
    elif choice == 6:
        print(f"{CITY} is in {response['sys']['country']}")
    elif choice == 7:
        print(f"The sunrise in {CITY} is {dt.datetime.fromtimestamp(response['sys']['sunrise'])}")
    elif choice == 8:
        print(f"The sunset in {CITY} is {dt.datetime.fromtimestamp(response['sys']['sunset'])}")
    elif choice == 9:
        print(f"The timezone in {CITY} is {response['timezone']}")
    elif choice == 10:
        print(f"The max temperature in {CITY} is {convert_to_celsius(response['main']['temp_max'])} degrees Celsius")
        print(f"The min temperature in {CITY} is {convert_to_celsius(response['main']['temp_min'])} degrees Celsius")
    elif choice == 0:
        print("Thanks for using this Weather App")
        break
    else:
        print("Invalid choice")
