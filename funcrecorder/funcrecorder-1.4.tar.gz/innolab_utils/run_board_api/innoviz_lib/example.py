import json

from innoviz_lib.jsjson import JsJson

example_path = './example.json'

with open(example_path, 'r') as f:
    meta = json.load(f)

out = JsJson(meta)

print(out)
print("out.a : %d" % out.a)
print("out.d.b : %.2f" % out.d.b)
