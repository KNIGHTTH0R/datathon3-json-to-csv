import json
import csv

with open('districts_daily_may_15.json') as json_file:
    data = json.load(json_file)

data_file = open('districts_daily_may_15.csv', 'w')

csv_writer = csv.writer(data_file)

# I'm not sure if this is correct syntax

csv_writer.writerow(['State', 'district', 'date', 'confirmed', 'active', 'recovered', 'deceased'])

districtsDaily = data['districtsDaily']
for district in districtsDaily.keys():
    current_district_data = districtsDaily[district]
    for city in current_district_data.keys():
        city_data = current_district_data[city]
        for case in city_data:
            csv_writer.writerow([district, city, case.get('date'), case.get('confirmed'), case.get('active'), case.get('recovered'), case.get('deceased')])

data_file.close()
