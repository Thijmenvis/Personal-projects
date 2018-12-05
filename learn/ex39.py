# create a mapping of state to abbreviation
# dictionary = {
# 'keyOne': 'valueOne',
# 'keyTwo': 'valueTwo',
# }

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# creates a line
def line():
    print '-' * 10

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
line()
# goes back to cities dictionary and takes out the answer to NY
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
line()
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
line()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
line()
for state, abbrev in states.items():
    print "%s is abbreviatiated %s" % (state, abbrev)


line()
for abbrev, city in cities.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

# now do both at the same time
line()
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

line()
# savely get an abbreviation by state that might nog be there
state = states.get('Texas')
print "######### >", not state
if not state:
    print "Sorry no Texas"

# get(key[, default])
# the [] means that its not needed/optional. It defaults to None.
# return the value for key if key is in the dictionary, else default. if default
# is not given, it defaults to None. so that this method never rases a KeyError.
# get a city with a default values
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX': %s" % city
