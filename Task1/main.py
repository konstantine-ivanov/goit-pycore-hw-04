

def total_salary(path):
    total_salary = 0
    counter = 0

    try: #checking if file exists
        with open(path, 'r', encoding='UTF-8') as f:
            for line in f: #file to list
                try: #checking if formating is correct
                    name, salary = line.split(',')
                    total_salary += int(salary)
                    counter += 1
                except ValueError:
                    print (f"Wrong file formating in line {counter}: {line}")
                    continue
        if counter == 0:
            print ("There are no correct data in file")
            return None, None
        
        average_salary = total_salary / counter
        return total_salary, average_salary
    except FileNotFoundError:
        print ("File not found")
        return None, None


#total, average = total_salary("Task1/salaries_wrong_format.txt") #testing wrong format file
total, average = total_salary("Task1/salaries.txt") #testing correct file
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

