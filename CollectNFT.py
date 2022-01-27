import requests
import json
import shutil

url = "https://api.opensea.io/api/v1/assets?owner=0xb0439622f93f7349d6307c56a32b0d5aa42b7940&order_direction=desc&offset=0&limit=20"

headers = {
	"Accept": "application/json",
	"X-API-KEY": ""
}

response = requests.request("GET", url, headers=headers)

formatted = response.text
temp = json.loads(formatted)

ids = []
for item in temp['assets']:
    ids.append(item['image_url'])

index = 1
for id in ids:
	res = requests.get(id, stream=True)
	if res.status_code == 200:
		with open('id#'+str(index)+'.jpg', 'wb') as f:
			shutil.copyfileobj(res.raw, f)
		print('Image sucessfully Downloaded')
		index+=1
	else:
		print('Image Couldn\'t be retrieved')
