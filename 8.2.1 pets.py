# --- Positional Arguments ---
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")
	
describe_pet("hamster", "harry")

# Mutiple Function Calls
describe_pet("dog", "willie")

# Order Matters in Positional Arguments
describe_pet("harry", "hamster")

# --- Keyword Arguments ---
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")

# --- Default Values ---
def describe_pet(pet_name, animal_type="dog"):
	"""Display information about a pet."""
	print("I have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".\n")
	
describe_pet("willie")

# Equivalent Function Calls
# A dog named Willie.
describe_pet("willie")
describe_pet(pet_name = "willie")
# A hamster named Harry
describe_pet("hamster", "willie")
describe_pet(pet_name="willie", animal_type="hamster")
describe_pet(animal_type="hamster", pet_name="willie")


