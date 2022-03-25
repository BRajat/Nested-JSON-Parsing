import json
from extract import json_extract
from main_output import output

print(output)

result = json_extract(output, 'text')

print(result)

duration = result[1::2]
distance = result[::2]

print(duration)
# ['3 hours 54 mins', '1 hour 44 mins', '1 day 18 hours', '18 hours 43 mins', '1 day 2 hours', '1 day 18 hours']

print(distance)
# ['227 mi', '94.6 mi', '2,878 mi', '1,286 mi', '1,742 mi', '2,871 mi']
