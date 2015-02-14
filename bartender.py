import random

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

def main():
  orders = 0
  drinks = True
  while drinks:
    if orders == 0:
      customer_name = raw_input('Ahoy matey, what is yer name? ')
      question = 'Would you like to order a drink %s ? ' %customer_name
      answer = raw_input(question)
    elif orders > 0 and orders < 6:
      question = 'Would you like to order another drink, %s ? ' %customer_name
      answer = raw_input(question)
    else:
      print 'Youre cut off my friend. How about a glass of water?'
      break
    if answer.lower() == 'yes' or answer.lower() == 'y':
      orders += 1
      customer_order = make_drink(get_preferences())
      print '\nYour drink is ready.\nIt is called The %s.\nIt has some good stuff:' %name_drink()
      for i in customer_order:
        print '> a %s ' %i
    else:
      drinks = False
  
if __name__ == '__main__':
  main()