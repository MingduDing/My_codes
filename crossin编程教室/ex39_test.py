# -*- coding: UTF-8 -*-
from ex39_hashmap import *


# create a mapping of state to abbreviation
states = new()
set(states, 'Oregon', 'OR')
set(states, 'Florida', 'FL')
set(states, 'California', 'CA')
set(states, 'New York', 'NY')
set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = new()
set(cities, 'CA', 'San Francisco')
set(cities, 'MI', 'Detroit')
set(cities, 'FL', 'Jacksonville')

# add some more cities
set(cities, 'NY', 'New York')
set(cities, 'OR', 'Portland')

# print out some cities
print '-' * 20
print "NY State has: %s" % get(cities, 'NY')
print "OR State has: %s" % get(cities, 'OR')

# print some states
print "Michigan's abbreviation is: %s" % get(states, 'Michigan')
print "Florida's abbreviation is: %s" % get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 20
print "Michigan has: %s" % get(cities, get(states, 'Michigan'))
print "Florida has: %s" % get(cities, get(states, 'Florida'))

# print every state abbreviation
print '-' * 20
list(states)

# print every city in state
print '-' * 20
list(cities)

print '-' * 20
state = get(states, 'Texas')

if not state:
	print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line
city = get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city