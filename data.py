import requests
import html

params = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url= "https://opentdb.com/api.php", params= params)
response.raise_for_status()
question_data = response.json()["results"]
#unescape html code
for question in question_data:
    question["question"] = html.unescape(question["question"])