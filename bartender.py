import random

ALL_CUSTOMERS = {}
ANSWERS = ['yes','y']
INVENTORY = {
    "glug of rum" : 10, "slug of whisky": 10, "splash of gin": 10,
    "olive on a stick": 10, "salt-dusted rim": 10, "rasher of bacon": 10,
    "shake of bitters": 10, "splash of tonic": 10, "twist of lemon peel": 10,
    "sugar cube": 10, "spoonful of honey": 10, "spash of cola": 10,
    "slice of orange": 10, "dash of cassis": 10, "cherry on top": 10
  }
DRINK_LIMIT = 5
PROMPTS = {
  "drink" : "Would you like to order a drink? ",
  "name" : "What is your name, matey? ",
  "more" : "Would you like another "
}

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

def manage_inventory(order_ingredients):
  '''
  @param list of ingredients
  decrement ingredient stock
  re-stock ingredients when supply runs low
  :return None:
  '''
  for ingredient in order_ingredients:
    if INVENTORY[ingredient] < 2:
      print 'Shiver me timbers, I need to restock %s!' %ingredient
      INVENTORY[ingredient] = 10
    else:
      INVENTORY[ingredient] -= 1

def name_drink():
  nouns = ["Dog", "Seagull", "Pirate", "Cannonball", "Scallywag", "Anchor", "Diamond", "Breeze", "Sunshine", "Paradise", "Cocktail"]
  adjectives = ["Rusty", "Dirty", "Black", "Pink", "Salty", "Fruity", "Fluffy", "Flaming", "Royal", "Happy"]
  name = '%s %s' %(random.choice(adjectives),random.choice(nouns))
  return name

def customer_management(customer_name):
  '''
  greet customer and store name and number of drinks in global dictionary
  @return string of customers name
  '''
  customers = {}
  if ALL_CUSTOMERS.has_key(customer_name):
    ALL_CUSTOMERS[customer_name]['total drinks'] += 1
  else:
    ALL_CUSTOMERS[customer_name] = {
      'name': customer_name,
      'total drinks': 1
    }
  return customer_name

def deliver_drink(customer_info,order_ingredients):
  '''
  update customers drink preferences and deliver drink
  :param dictionary of customer_info:
  :return:
  '''
  drink_name = name_drink()
  customer_info["drink name"] = drink_name
  customer_info["ingredients"] = order_ingredients
  print '\nI made you a tasty brew.\nIt is called the %s and has the following ingredients:' %drink_name
  for ingredients in order_ingredients:
    print 'A %s' %ingredients

def prompt_user(question,drink):
  if question == PROMPTS["more"]:
    question = question + drink + '? '
    answer = raw_input(question)
  else:
    answer = raw_input(question)
  return answer

def main():
  while True:
    answer = prompt_user(PROMPTS['drink'],ALL_CUSTOMERS)
    if answer.lower() in ANSWERS:
      customer_name = raw_input(PROMPTS['name'])
      customer_management(customer_name)
      if ALL_CUSTOMERS[customer_name]['total drinks'] > DRINK_LIMIT:
        print 'Youve had enough my friend. Have a glass of water.'
        continue
      else:
        if ALL_CUSTOMERS[customer_name].has_key('drink name'):

          answer = prompt_user(PROMPTS['more'],ALL_CUSTOMERS[customer_name]["drink name"])
          if answer.lower() in ANSWERS:
            print '\nOne %s, coming right up!' %ALL_CUSTOMERS[customer_name]["drink name"]
            manage_inventory(ALL_CUSTOMERS[customer_name]["ingredients"])
            continue
        customer_prefs = get_preferences()
        order_ingredients = make_drink(customer_prefs)
        manage_inventory(order_ingredients)
        deliver_drink(ALL_CUSTOMERS[customer_name],order_ingredients)
    else:
      break
  
if __name__ == '__main__':
  main()