import os
import logging
from collections import namedtuple


logging.basicConfig(filename='directory_content.log', level=logging.INFO, format='%(asctime)s - %(message)s')

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_directory'])


def get_directory_content(directory_path):

    content = []

    try:
        items = os.listdir(directory_path)
    except FileNotFoundError:
        logging.error("Директория не найдена: %s", directory_path)
        return content

    for item in items:

        item_path = os.path.join(directory_path, item)

        is_dir = os.path.isdir(item_path)

        extension = os.path.splitext(item)[1] if not is_dir else ""

        parent_directory = os.path.basename(os.path.dirname(item_path))

        content.append(FileInfo(name=os.path.splitext(item)[0], extension=extension, is_dir=is_dir,
                                parent_directory=parent_directory))

        logging.info("Имя: %s, Расширение: %s, Флаг каталога: %s, Название родительского каталога: %s",
                     os.path.splitext(item)[0], extension, is_dir, parent_directory)

    return content


def main():
    # Запрашиваем ОС
    os_choice = input("Выберите вашу операционную систему (Windows/Mac/Linux): ")

    # Запрашиваем путь до директории
    directory_path = input("Введите путь до директории: ")

    directory_content = get_directory_content(directory_path)

    print("Содержимое директории:")
    for item in directory_content:
        item_type = "Каталог" if item.is_dir else "Файл"
        print(
            f"Имя: {item.name}, Расширение: {item.extension}, Тип: {item_type}, Название родительского каталога: {item.parent_directory}")


if __name__ == "__main__":
    main()