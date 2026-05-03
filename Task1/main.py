

def total_salary(path):
    with open(path, 'r', encoding='UTF-8') as f:
        return f.read()

print (total_salary('Task1/salaries.txt'))

#testing
