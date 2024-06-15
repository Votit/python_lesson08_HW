def work_with_phonebook():

    choice = show_menu()

    phone_book = read_txt("c:/Users/titov/OneDrive/Desktop/GeekBrains/Python/lesson08_HW/phone.txt")

    while (choice != 7):

        if choice == 1:

            print_result(phone_book)

        elif choice == 2:

            last_name = input('lastname ')
            print(*find_by_lastname(phone_book, last_name))

        elif choice == 3:

            last_name = input('lastname ')
            new_number = input('new  number ')
            print(change_number(phone_book, last_name, new_number))
	    	
        elif choice == 4:

            lastname = input('lastname ')
            print(delete_by_lastname(phone_book, lastname))

        elif choice == 5:

            number=input('number ')
            print(find_by_number(phone_book,number))

        elif choice == 6:

            user_data = input('new data')
            add_user(phone_book, user_data)
            write_txt('phone.txt', phone_book)

        choice = show_menu()
    
    print("Работа программы завершена.")


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по фамилии и изменить его номер\n"
          "4. Найти абонента по фамилии и удалить запись\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить нового абонента\n"
          "7. Завершение работы")
    choice = int(input())
    return choice



def read_txt(filename): 

    phone_book = []

    fields = ['Фамилия:', 'Имя:', 'Телефон:', 'Описание:']

    with open(filename, 'r', encoding = 'utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(',')))

            if record['Фамилия:'] != '\n':
                phone_book.append(record)	

    return phone_book



def write_txt(filename, phone_book):

    with open(filename,'w',encoding = 'utf-8') as phout:

        for i in range(len(phone_book)):

            s = ''

            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')


def print_result(phone_book):
    
    for item in phone_book:
        
        for i in item:
            print(i, item[i])



def find_by_lastname(phone_book, last_name):
    
    result = list()

    for item in phone_book:
        
        if last_name == item['Фамилия:']:

            for i in item:
                result.append(i)
                result.append(item[i])
    
    return result



def change_number(phone_book, last_name, new_number):
    pass


def delete_by_lastname(phone_book, lastname):
    pass

def find_by_number(phone_book, number):
    pass

def add_user(phone_book, user_data):
    pass

work_with_phonebook()