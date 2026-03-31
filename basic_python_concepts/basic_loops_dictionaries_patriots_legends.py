# patriots_legends.py -- loops and dictionaries with new england patriots legends
from typing import TypedDict


class Legend(TypedDict):
    name: str
    position: str
    college: str


patriots_legends: list[Legend] = [
    {"name": "John Hannah",       "position": "Offensive Guard",       "college": "Alabama"},
    {"name": "Tom Brady",         "position": "Quarterback",           "college": "Michigan"},
    {"name": "Andre Tippett",     "position": "Linebacker",            "college": "Iowa"},
    {"name": "Gino Cappelletti",  "position": "Wide Receiver/Kicker",  "college": "Minnesota"},
    {"name": "Steve Grogan",      "position": "Quarterback",           "college": "Kansas State"},
]

# example 1: loop over dicts, f-string output
for legend in patriots_legends:
    print(f"{legend['name']} | {legend['position']} | {legend['college']}")

print()

# example 2: list comprehension + enumerate (replaces range(len(...)))
names: list[str] = [legend["name"] for legend in patriots_legends]
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")