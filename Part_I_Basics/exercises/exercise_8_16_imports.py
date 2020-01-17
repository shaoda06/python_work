# 8-16. Imports: Using a program you wrote that has one function in it,
# store that function in a separate file. Import the function into your main
# program file, and call the function using each of these approaches:

# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
# ------------------------------------------------------------------------------
import exercise_8_16_imports_module

user_profile = exercise_8_16_imports_module.build_profile('albert', 'einstein',
                                                          location='princeton',
                                                          field='physics')
print(user_profile)

# ------------------------------------------------------------------------------

from exercise_8_16_imports_module import build_profile

user_profile = exercise_8_16_imports_module.build_profile('albert', 'einstein',
                                                          location='princeton',
                                                          field='physics')
print(user_profile)

# ------------------------------------------------------------------------------

from exercise_8_16_imports_module import build_profile as bp

user_profile = bp.build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)

# ------------------------------------------------------------------------------

import exercise_8_16_imports_module as imports_module

user_profile = imports_module.build_profile('albert', 'einstein',
                                            location='princeton',
                                            field='physics')
print(user_profile)

# ------------------------------------------------------------------------------

from exercise_8_16_imports_module import *

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
