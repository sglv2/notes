import json, yaml

d = {
    "k1": "v1",
    "k2": ["v20", "v21", "v22"],
    "k3": {"k30": "v30"}
}

s = json.dumps(d)
print(s)
print(json.dumps(d, indent=2, sort_keys=True))
print(json.loads(s)["k1"])

print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print(yaml.dump(d))

with open(r'output.yaml', 'w') as f:
    print(yaml.dump(d, f))
