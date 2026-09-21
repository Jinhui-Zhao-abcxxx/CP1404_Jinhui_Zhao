from prac_06.guitar import Guitar

gibson_l5_ces = Guitar("Gibson L-5 CES",1922,16035.40)
another_one = Guitar("another one",2013)

print(gibson_l5_ces.get_age())
print(another_one.get_age())
print(gibson_l5_ces.is_vintage())
print(another_one.is_vintage())