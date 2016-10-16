cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# my stupid version
# it was with salad before, but with drinks it is much better
bananas = 4
apples = 5
oranges = 6
people = 4
whole_bar = bananas + apples + oranges
drinks_per_person = whole_bar / 3
what_need = people * drinks_per_person

print "There are", people, "people at home now."
print "We can make only", whole_bar, "drinks with what we have."
print "But we would need", what_need, "."
print "What would we need to have drinks for everybody?"
