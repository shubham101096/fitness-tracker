import requests
import datetime
import os

APP_ID = os.environ.get('APP_ID')
APP_KEY = os.environ.get('APP_KEY')

APP_URL ="https://trackapi.nutritionix.com"

headers = {"x-app-id": APP_ID,
                        "x-app-key": APP_KEY,
                        "x-remote-user-id": "1"}


post_api_endpoint = f"{APP_URL}/v2/natural/exercise"

workouts = input("Tell me which exercises you did: \n") # Eg: walked 2 miles and ran 4km
post_data = {"query": workouts}

post_data = {
 "query": workouts,
 "gender": "male",
 "weight_kg": 80,
 "height_cm": 190,
 "age": 25
}

response = requests.post(post_api_endpoint, json=post_data, headers=headers)
row_sheet = response.json()

SHEET_URL = os.environ.get('SHEET_URL')

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")
exercise = row_sheet['exercises'][0]['user_input']
duration = row_sheet['exercises'][0]['duration_min']
calories = row_sheet['exercises'][0]['nf_calories']

row_data = {"workout": {
                    "date": date,
                    "time": time,
                    "exercise": exercise,
                    "duration": duration,
                    "calories": calories}
            }

headers = {"Authorization": f"Basic {os.environ.get('TOKEN')}"}

response = requests.post(SHEET_URL, json=row_data, headers=headers)
print(response.text)