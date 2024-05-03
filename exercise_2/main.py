def get_cats_info(path):
    cats_list = [] 

    try:
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                cat_info = line.strip().split(',') 
                cat_dict = {
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": cat_info[2]
                }
                cats_list.append(cat_dict) 

        return cats_list
    
    except FileNotFoundError:
        raise FileNotFoundError("Файл не знайдено або недоступний.")
    except Exception as e:
        raise e 
    
# Приклад використання:
try:
    cats_info = get_cats_info("exercise_2/cats_file.txt") 
    print(cats_info) 
except Exception as e:
    print(f"Помилка: {e}")
