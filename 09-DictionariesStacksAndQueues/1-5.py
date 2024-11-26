countries = [
{"name":"Poland", "population":38000000},
{"name":"Germany", "population":84000000},
{"name":"France", "population":68000000},
{"name":"Spain", "population":48000000},
{"name":"Italy", "population":50000000}
]
print("COUNTRY   POPULATION")
for country in countries:
    print(f'{country["name"]}   {country["population"]}')
