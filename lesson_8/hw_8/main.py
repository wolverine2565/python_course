from os import path

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Телефонная книга:\n"
                        "1. Показать данные\n"
                        "2. Добавить запись\n"
                        "3. Найти запись\n"
                        "4. Изменить запись\n"
                        "5. Удалить запись\n"
                        "6. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_rec()
            case "3":
                search()
            case "4":
                chenge()
            case "5":
                delete()
            case "6":
                play = False
            case _:
                print("Повторите, неверный пункт!\n")

def read_records():
    global all_data, id
    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if all_data:
            id = int(all_data[-1][0])
        return all_data

def show_all():
    if not all_data:
        print("Данных нет")
    else:
        print(*read_records(), sep="\n")

def add_rec():
    global id
    data = ['Фамилия','Имя','Отчество','Телефон']
    rec = ''
    for  i in data:
        rec += input("Введите "+ i + ": ") + " "
    with open(file_base, 'a', encoding="utf-8") as f:
        id += 1
        f.write("\n" + str(id) + " " + rec)

def search():
    text = input("Введите данные для поиска: ")
    all_rec = read_records()
    for rec in all_rec:
        if text in rec:
            print(f"{rec}")
    
def delete():
    show_all()
    piple_id = input("Выберите идентификатор записи для удаления: ")
    file_data = read_records()
    new_data = []
    for i in file_data:
        if i[0] != piple_id:
            new_data.append(i)
    with open(file_base, 'w', encoding='utf-8') as f:
        f.writelines(line + '\n' for line in new_data)
        
def chenge():
    show_all()
    piple_id = input("Выберите идентификатор записи для изменения: ")
    file_data = read_records()
    global id
    data = ['Фамилию', 'Имя', 'Отчество', 'Телефон']
    rec = ''
    for i in data:
        rec += input("Введите " + i + ": ") + " "
    with open(file_base, 'w', encoding='utf-8') as f:
        for i in file_data:
            if i[0] != piple_id:
                f.write(i + '\n')
            else:
                id = i[0]
                f.write(id + ' ' + rec + '\n')
show_all()