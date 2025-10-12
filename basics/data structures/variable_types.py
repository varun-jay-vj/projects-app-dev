#### LISTS - series of items in a particular order.
print("Lists")
plan = ['ZeroWolf', 'Retail Strategy', 2024] # a list of attributes of one object
print(f"{plan[0]} has a {plan[1]} for {plan[2]}.")
first_item = plan[0] # first item in a list
print(f"first item in plan: {first_item}")
last_item = plan[-1] # last item in a list
print(f"last item in plan: {last_item}")
plan.append('Varun') # adding a new item to the end of the list
for item in plan: # Looping through all items in the list
    print(f"{item} is part of the plan.")
#### DICTIONARIES - store connections between pieces of information. Each item is a key-value pair
print("Dictionaries")
plans = {'company':'ZeroWolf', 'strategy':'Retail Strategy', 'year':2024} # a list of attributes of one object
print(f"{plans['company']} has a {plans['strategy']} for {plans['year']}.")
plans['year'] = 2025 # modifying an existing key-value pair item
plans['owner'] = 'Varun' # adding a new key-value pair item
for key, value in plans.items(): # Looping through all key-value pairs
    print(f"{key} --> {value}")
for keys in plans.keys(): #Looping through all keys
    print(f"{keys} is defined in plans.")
for values in plans.values(): #Looping through all values
    print(f"{values} exists in plans.")
