# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
# Store the classes User, Privileges, and Admin in one module. Create a separate
# file, make an Admin instance, and call show_privileges() to show that
# everything is working correctly.


from exercise_9_11_privileges import Admin

my_admin = Admin('shaoda', 'liu', 25, 'male')
my_admin.privileges.show_privileges()
