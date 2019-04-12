# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'root pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    # Display all completed models.
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
