# Indirect string matching
with open("example.txt", "r") as f:
    cities = f.read().split("\n")

len(cities)

from fuzzywuzzy import process

def get_matches(query, choices, limit=4):
    results = process.extract(query, choices, limit=limit)
    return results

res = get_matches("Deluxe King Room", cities)
print(res)

# Another way
from fuzzywuzzy import fuzz
res = fuzz.ratio('Deluxe Room, 1 King Bed', 'Deluxe King Room')
print(res)

res = fuzz.partial_ratio('Deluxe Room, 1 King Bed', 'Deluxe King Room')
print(res)

res = fuzz.token_sort_ratio('Deluxe Room, 1 King Bed', 'Deluxe King Room')
print(res)

res = fuzz.token_set_ratio('Deluxe Room, 1 King Bed', 'Deluxe King Room')
print(res)