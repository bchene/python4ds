from new_student import Student


student = Student(name="Edward", surname="agle")
print(student, end="\n\n")

student = Student(name="ba")
print(student, end="\n\n")

student = Student()
print(student, end="\n\n")

student = Student(name="perso", surname="one", active=False)
print(student, end="\n\n")

# EXPECTED OUTPUT
#
# Student(name='Edward', surname='agle', active=True, login='edward.agle', \
# id='qawxdtanefwqjbw')
#
# Student(name='ba', surname='unknown_surname', active=True, \
# login='ba.unknown_surname', id='hduhjdgugezquka')
#
# Student(name='unknown_name', surname='unknown_surname', active=True, \
# login='unknown_name.unknown_surname', id='rknfwlufxiwjzic')
#
# Student(name='perso', surname='one', active=False, login='perso.one', \
# id='txikczvpedceccz')
