

def get_cats_info(path):
    try: #checking if file exists
        cats =  []

        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                try: #checking if formatin is correct. This is a basic check only. For purely proper check there should be regex validation of each
                    cat_id, cat_name, cat_age = line.strip().split(',') #file to line and to values
                    one_cat_dict = {'id': cat_id, 'name': cat_name, 'age': int(cat_age)} # values to dict and age validation
                    cats.append(one_cat_dict)
                except ValueError:
                    print(f"Wrong file formatting in line: {line}")
                    continue
        return cats
    
    except FileNotFoundError:
        print("File path is wrong")
        return []  



#testing
correct_cats_list = "Task2/cats.txt"
wrong_cats_list = "Task2/wrong_cats.txt"

print(get_cats_info(correct_cats_list))
