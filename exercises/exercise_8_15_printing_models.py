import exercise_8_15_printing_functions


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    # Display all completed models.
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'root pendant', 'dodecahedron']
completed_models = []
exercise_8_15_printing_functions.print_models(
    unprinted_designs[:], completed_models)

show_completed_models(completed_models)
