def main():
    courses_clasrroms = {'CS101':'3004','CS102':'4501',
                    'CS103':'6755','CS104':'1244','CS105':'1411'}
    courses_teachers = {'CS101':'Hainz','CS102':'Alvardo','CS103':'Rich',
                        'CS104':'Berk','CS105':'Li'}
    courses_times = {'CS101':'8:00','CS102':'9:00','CS103':'10:00',
                        'CS104':'11:00','CS105':'13:00'}
    
    print_info(courses_clasrroms, courses_teachers, courses_times)
    
def print_info(classroom, teachers, times):   
    status = 'y'
    while status.lower() == 'y':
        try:
            choice = input('Enter the course to view information: ')
            print(f'Course {choice}\nClassroom: {classroom[choice]}\nTeacher: {teachers[choice]}\nTime: {times[choice]}.')
        except KeyError:
            print("Invalid Course, try again")
            
        status = input('Do you want to get another info? Enter y/n?')
main()