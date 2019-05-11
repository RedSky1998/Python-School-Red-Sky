#Hi this is the First episode of Python School!
#Variables and basic calculations
cars = 90
space_in_each_car = 4
drivers = 40
turists = 100
#Variables in more details! 
cars_driven = drivers
cars_not_driven = cars - drivers
those_people_that_are_actually_travelling = space_in_each_car * cars_driven #THIS INCLUDES THE DRIVERS!
those_turists_that_are_actually_travelling = those_people_that_are_actually_travelling - drivers
turists_that_fit_in_a_car_without_the_driver = turists / drivers
those_turists_that_fit_in_a_single_car = turists_that_fit_in_a_car_without_the_driver + (turists_that_fit_in_a_car_without_the_driver%1)
#this will give 3 again
# We use the % symbol in cases where you are interested for the remaining part of an expression!
#For example X divided by Y and you get Z as the remaining! So
# X = 100 divided by Y which is 40 and you get Z which is 0.5 because 100/4 = 2.5 but you aren't interested
#for the so the 2.0 is taken away so Z = 2.5 - 2 = 0.5 :)
print("In a car only", those_turists_that_fit_in_a_single_car, "turists can fit because we need the last space for the driver!")
print("There are only", cars, "cars available!")
print("There are only", drivers, "drivers working today!")
print("There will be", cars_not_driven, "cars left in the garage!")
print("Maximum",those_people_that_are_actually_travelling, "people can travell including the drivers!")
print("")
print("Make sure to Hit Like and Subscribe for more content on youtube:")
print("https://www.youtube.com/channel/UCIYfz3yaGydlI2oDD4NDj2Q?view_as=subscriber")
