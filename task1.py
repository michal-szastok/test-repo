# Create good script to create new list, which only contains users from Poland. Try to do it with List Comprehension.
# users = [{"name": "Kamil", "country":"Poland", {"name":"John", "country": "USA"}, {"name": "Yeti"}]
users = [{"name": "Kamil", "country": "Poland"}, {"name": "John", "country": "USA"}, {"name": "Yeti"}, ]
print(f"Users: \n {users} \n")

users_from_poland = [user for user in users if user.get('country', '') == 'Poland']
print(f"Name(s) of user(s) from Poland: \n {users_from_poland} \n")
