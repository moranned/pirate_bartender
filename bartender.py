import random

ALL_CUSTOMERS = {}

def get_preferences():
  '''
  ask customer a series of predefinied questions to determine drink ingredients
  @param none
  @return dictionary of customer preferences
  '''
  customer_preferences = {}
  questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? "
  } 
  for k,v in questions.iteritems():
    answer = raw_input(v)
    if answer.lower() == 'yes' or answer.lower() == 'yes':
      customer_preferences[k] = True
    else:
      customer_preferences[k] = False
  return customer_preferences 

def make_drink(prefs):
  '''
  construct a drink order
  @param dictionary of customer preferences
  @return list of order ingredients
  '''
  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
  }
  order_ingredients = []
  for k,v in prefs.iteritems():
    if v is True:
      order_ingredients.append(random.choice(ingredients.get(k)))
  return order_ingredients

def name_drink():
  nouns = ["Dog", "Seagull", "Pirate", "Cannonball", "Scallywag", "Anchor", "Diamond", "Breeze", "Sunshine", "Paradise", "Cocktail"]
  adjectives = ["Rusty", "Dirty", "Black", "Pink", "Salty", "Fruity", "Fluffy", "Flaming", "Royal", "Happy"]
  name = '%s %s' %(random.choice(adjectives),random.choice(nouns))
  return name

def customer_management():
  '''
  greet customer and store name and number of drinks in global dictionary
  @return boolean
  '''
  customers = {}
  question = 'Would you like to order a drink? '
  answer = raw_input(question)
  if answer.lower() == 'yes' or answer.lower() == 'y':
    customer_name = raw_input('What is your name, matey? ')
    for customer, info in ALL_CUSTOMERS.iteritems():
      if customer == customer_name:
        update_customer = ALL_CUSTOMERS.get(customer_name)
        update_customer["total drinks"] += 1
        return customer_name
    customers["name"] = customer_name
    customers["total drinks"] = 1
    ALL_CUSTOMERS[customer_name] = customers
    return customer_name
  else:
    return None

def main():
  drinks = True
  while drinks:
    customer_name = customer_management()
    if customer_name:
      update_customer = ALL_CUSTOMERS.get(customer_name)
      if update_customer.get("drink name"):
        print 'Would you like another %s? ' %update_customer["drink name"]
      else:
        customer_order = make_drink(get_preferences())
        update_customer["drink name"] = name_drink()
        update_customer["ingredients"] = customer_order
        print ALL_CUSTOMERS
    else:
      drinks = False
  
if __name__ == '__main__':
  main()