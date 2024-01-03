import json
users = {
    'id' : 1,
    'name' : 'Leanne Graham',
    'username' : 'Bret',
    'email' : 'Sincere@april.biz',
    'address' : {
        'street' : 'kulas light',
        'suite' : 'Apt 567',
        'city' : 'Las vegas'
     }

}
print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address'])
print(users['address']['street'])



print('\n Pengunaan json dump dan dumps')

# output berupa string
result = json.dumps(users)
print(result)
print(type(result))

with open('result.json', 'w') as file:
    json.dump(users, file)