import json

if __name__ == "__main__":
	with open('hpi.json') as jsonfile:
		db = json.load(jsonfile)
		print(db['info']['title'])
