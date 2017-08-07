import json

def read_json_from_file(filename, cleanup=False):
	str_data = ""
	with open(filename, "r") as raw_data:
		str_data = raw_data.read()
	return json.loads(str_data)

def create_district_lookup(districts, responsibles):	
	district_responsible_lookup = {}
	for responsible_id in responsibles:
		responsible = responsibles[responsible_id]
		districts = responsible["districts"]
		for district_id in districts:
			district_id_str = str(district_id)
			if not district_id_str in district_responsible_lookup:
				district_responsible_lookup[district_id_str] = []
			district_responsible_lookup[district_id_str].append(responsible_id)
	return district_responsible_lookup

districts = read_json_from_file("precincts.json")
responsibles = read_json_from_file("responsibles.json")
district_responsible_lookup = read_json_from_file("district_responsible_lookup.json")

responsibles_result = district_responsible_lookup["65"]
for responsible_id in responsibles_result:
	responsible = responsibles[responsible_id]
	print(responsible["name"].lower())
	print(responsible["address"])
	print("")