#!/usr/bin/env python3
import json

# Dump example-data.json to a DOT graph, but exclude item #33 which
# is the event TLO that everything is related to. This would basically
# diagram an entire event.

g = json.loads(open('example-data.json','rb').read())

print("graph G {")
for o in g['observables']:
    print(" n{id}[label=\"{val}\"]".format(id=o['id'], val=o['value']))
for t in g['targets']:
    print(" n{id}[label=\"{val}\"]".format(id=t['id'], val=t['target_name']))

for r in g['relationships']:
    if r['from'] == 33 or r['to'] == 33:
        continue
    print(" n{id1} -- n{id2}".format(id1=r['from'], id2=r['to']))

print("}")
