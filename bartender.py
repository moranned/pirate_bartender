import random

ALL_CUSTOMERS = {}
ANSWERS = ['yes','y']

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
    if answer.lower() in ANSWERS:
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
  @return string of customers name
  '''
  customers = {}
  question = 'Would you like to order a drink? '
  answer = raw_input(question)
  if answer.lower() in ANSWERS:
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

def deliver_drink(customer_info):
  '''
  update customers drink preferences and deliver drink
  :param dictionary of customer_info:
  :return:
  '''
  customer_order = make_drink(get_preferences())
  drink_name = name_drink()
  customer_info["drink name"] = drink_name
  customer_info["ingredients"] = customer_order
  print 'I made you a tasty brew.\nIt is called the %s and has the following ingredients:' %drink_name
  for ingredients in customer_order:
    print 'A %s' %ingredients

def main():
  drinks = True
  while drinks:
    customer_name = customer_management()
    if customer_name:
      update_customer = ALL_CUSTOMERS.get(customer_name)
      if update_customer.get("drink name"):
        question = 'Would you like another %s ? ' %update_customer["drink name"]
        answer = raw_input(question)
        if answer.lower() in ANSWERS:
          print 'One %s, coming right up!' %update_customer["drink name"]
        else:
          deliver_drink(update_customer)
      else:
        deliver_drink(update_customer)
    else:
      drinks = False
  
if __name__ == '__main__':
  main()