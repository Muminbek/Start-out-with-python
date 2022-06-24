import patient
import procedure

patient0 = patient.Patient('John','Pika','Doe','Nice street 30',
                               'New York','NY','NY10503',
                               '12341234','Yellow-white','13241235')

procedure1 = procedure.Procedure('Laser correction','5/5/1990',
                                    'Dr. Smith','30.000 euro.')
procedure2 = procedure.Procedure('Physiotherapy', '10/9/2000','Dr. Kostovskiy',
                                    '500 euro')
procedure3 = procedure.Procedure('Surgery', '23/12/2018',
                                    'Dr Frankenstein', '50.000 euro')
procedures = [procedure1, procedure2, procedure3]

print(f'Petient information\n------------------\n{patient0}')
count = 1
for i in procedures:
    print(f'Procedure #{count}\n------------------')
    print(i)
    count +=1


