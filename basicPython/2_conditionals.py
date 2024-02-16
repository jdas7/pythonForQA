# function isinstance
my_variable = "perro"

if isinstance(my_variable, int):
    print("the result is True")
else:
    print("the result is False")

# logic operators
edad = 27
tiene_trabajo = True
es_estudiante = False
global_age_of_experience = 5


def validacion(age_of_experience=None):
    if age_of_experience < 10 and tiene_trabajo and not es_estudiante:
        print("es un adulto con poca experiencia pero con trabajo y no estudia")
    else:
        print("el man tiene experiencia")


if edad > 18 and tiene_trabajo and not es_estudiante:
    print("es un adulto con trabajo y no estudia ")
    # llamar funcion
    validacion(global_age_of_experience)
else:
    print("fin")
