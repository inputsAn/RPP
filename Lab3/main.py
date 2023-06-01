import directory_processing
import data_processing


def add_new_data(d):
    try:
        data_flag = input("Вы хотите добавить новые данные? y/n ")
        data = input("Введите дату ")
        fio = input("Введите ФИО ")
        grant = input("Введите стипендию ")
        destination = input("Укажите, куда берете справку ")
        data_processing.add_new_data(d,"".join(data), "".join(fio), "".join(grant), "".join(destination))
        new_d = data_processing.reading_csv_file()
        print(f"Обновленный словарь:{new_d}")
        print()
    except KeyError:
        print("Попробуйте заново.")
        add_new_data(d)


if __name__ == "__main__":
    directory_processing.processing()
    d = data_processing.reading_csv_file()
    print(f"Словарь с данными:{d}")
    print(f"Сортировка по фио: {data_processing.fio_sorting(d)}")
    print(f"Сортировка по стипендии: {data_processing.grant_sorting(d)}")
    print(f"Сортировка по стипендии, которая больше value {data_processing.grant_more_than_sorting(d, 2000)}")
    add_new_data(d)
