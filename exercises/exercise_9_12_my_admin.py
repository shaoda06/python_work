# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly.


from exercise_9_12_admin import Admin

my_admin = Admin('shaoda', 'liu', 25, 'male')
my_admin.privileges.show_privileges()
