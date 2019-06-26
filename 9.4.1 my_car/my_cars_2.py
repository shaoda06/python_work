# Importing a Module into a Module

# from only_car import Car


# my_beetle = Car('volkswagen','beetle',2016)
# print(my_beetle.get_descriptive_name())


from only_electri_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
