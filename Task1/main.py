

def total_salary(path):
    total = 0
    counter = 0

    try: #checking if file exists
        with open(path, 'r', encoding='utf-8') as f:

            for line in f: #file to list
                try: #checking if formating is correct
                    name, salary = line.split(',')
                    total += int(salary)
                    counter += 1
                except ValueError:
                    print(f"Wrong file formatting in line {counter}: {line}")
                    continue

        if counter == 0:
            print("There are no correct data in file")
            return None, None
        
        average = total / counter
        return total, average
    except FileNotFoundError:
        print("File not found")
        return None, None


correct_salaries_list = "Task1/salaries.txt"
wrong_salaries_list = "Task1/salaries_wrong_format.txt"

total, average = total_salary(correct_salaries_list)
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

