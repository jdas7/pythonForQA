# function isinstance
my_variable = "dog"

if isinstance(my_variable, int):
    print("the result is True")
else:
    print("the result is False")

# logic operators
age = 27
has_work = True
is_student = False
global_age_of_experience = 5


def validation(age_of_experience=None):
    if age_of_experience < 10 and has_work and not is_student:
        print("is an adult with little experience but with a job and not in education")
    else:
        print("the man has experience")


if age > 18 and has_work and not is_student:
    print("is a working adult and does not study")
    # call function
    validation(global_age_of_experience)
else:
    print("fin")
