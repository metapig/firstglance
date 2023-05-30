drivers = {
    'leclerc': {
        'country': 'monaco',
        'team': 'Ferrari',
    },
    'zhou': {
        'points': 2,
        'team': 'Alfa Romeo',
        'country': "chinese",
    },
    'monitor': ['Fia', 44, 33],
}
print(drivers['monitor'][2])
unk = drivers.get('ham', 'no such driver')
print(unk)

for driver, info in drivers.items():
    if driver != 'monitor':
        print("\n"+driver)
        print(info)

if 'ver' not in drivers.keys():
    print("\nops!")


drivers['sai'] = {
    'country': 'esp',
    'value': 'unknown',
}

print(drivers['sai'])

drivers['set'] = {34, 23}
print(drivers['set'])

del drivers['zhou']

# print(drivers)

for k, v in drivers.items():
    print("\n"+k, v)
