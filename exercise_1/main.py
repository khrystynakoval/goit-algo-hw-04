def total_salary(path):
    total_salary = 0
    num_employees = 0

    try:
        with open(path, 'r', encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(',') 
                total_salary += int(salary)
                num_employees += 1 

        if num_employees == 0:
            raise ValueError("Файл не містить жодних даних про заробітну плату.")
        
        avarage_salary = total_salary/num_employees 
        return total_salary, avarage_salary 

    except FileNotFoundError:
        raise FileNotFoundError("Файл не знайдено або недоступний.")
    except Exception as e:
        raise e 

# Приклад використання:

try:
    total, avarage = total_salary("exercise_1/salary_file.txt") 
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avarage}") 
except Exception as e:
    print(f"Помилка: {e}") 