# -*- coding: utf-8 -*-
# python

# python nested dictionary/list to JSON

import json

python_object=['x3', {'x4':('8', None, 1.0, 2)}]
json_str=json.dumps(python_object)
print json_str

json_data='["x3", {"x4":["8", null, 1.0, 2]}]'
python_obj=json.loads(json_data)
print python_obj

my_data=json.loads(open("sample.json").read())
print my_data

hh={3:4, 5:6, 7: {9:{8:10}, 11:12}}
print json.dumps(hh, indent=1)


