import json


with open("topics") as f:
    lines = f.readlines()

topics = {}
it = iter(lines)
try:
    while True:
        l = next(it)
        if l == '<top>\n':
            num = int(next(it).split("<num> Number: ")[1].rstrip())
            title = next(it).split("<title> ")[1].rstrip()
            next(it)
            next(it)
            desc = next(it).rstrip()
            next(it)
            next(it)
            narr = next(it).rstrip()

            topic = {
                "num": num,
                "title": title,
                "desc": desc,
                "narr": narr
            }
            topics[num] = topic
except StopIteration:
    pass


# reformat to
# [
#   {
#     "model": "topic.topic",
#     "pk": 1,
#     "fields": {
#       "number": 336,
#       "title": "Black Bear Attacks",
#       "seed_query": "Black Bear Attacks Black Bear Attacks",
#       "description": "Black Bear Attacks",
#       "narrative": "Black Bear Attacks",
#       "created_at": "2017-06-22T20:18:35.279Z",
#       "updated_at": "2017-06-22T20:18:35.279Z"
#     }
#   },
#   ...
# ]
l = []
pk = 1
for t in topics:
    d = {
        "model": "topic.topic",
        "pk": pk,
        "fields": {
            "number": t,
            "title": topics[t]["title"],
            "seed_query": "{} {}".format(topics[t]["title"], topics[t]["desc"]),
            "description": topics[t]["desc"],
            "narrative": topics[t]["narr"],
            "created_at": "2017-06-22T20:18:35.279Z",
            "updated_at": "2017-06-22T20:18:35.279Z"
        }
    }
    pk += 1
    l.append(d)

print(json.dumps(l))
