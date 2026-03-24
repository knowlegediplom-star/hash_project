from hash_table import HashTable
from string_hash import simple_string_hash
from string_hash_dict import StringHashDictionary


def main():
    lines = []

    lines.append("1. Проверка класса HashTable")
    lines.append("")

    table = HashTable(size=5)
    elements = [
        ("apple", 10),
        ("banana", 20),
        ("orange", 30),
        ("grape", 40),
        ("melon", 50),
        ("kiwi", 60),
        ("pear", 70),
        ("plum", 80),
        ("peach", 90),
        ("mango", 100),
    ]

    lines.append(f"Начальный размер таблицы: {table.size}")
    lines.append("Добавляем 10 элементов...")
    lines.append("")

    for key, value in elements:
        table.insert(key, value)
        lines.append(f"Добавлен элемент: {key} -> {value}")

    lines.append("")
    lines.append(f"Размер таблицы после resize: {table.size}")
    lines.append("")
    lines.append("Содержимое таблицы:")
    lines.append(str(table))
    lines.append("")

    lines.append("2. Проверка поиска")
    search_key = "orange"
    search_result = table.search(search_key)
    lines.append(f"Поиск ключа '{search_key}': {search_result}")
    lines.append("")

    lines.append("3. Проверка удаления")
    delete_key = "banana"
    deleted_value = table.delete(delete_key)
    lines.append(f"Удален ключ '{delete_key}', значение: {deleted_value}")
    lines.append(f"Повторный поиск '{delete_key}': {table.search(delete_key)}")
    lines.append("")

    lines.append("4. Хеш-функция для строки")
    text = "hello"
    hash_value = simple_string_hash(text)
    lines.append(f"Строка: {text}")
    lines.append(f"Хеш-значение: {hash_value}")
    lines.append("")

    lines.append("5. Словарь строк и их хешей")
    hash_dict = StringHashDictionary()
    words = ["cat", "dog", "house", "tree", "python"]

    for word in words:
        hash_dict.add(word)
        lines.append(f"Добавлено: {word} -> {hash_dict.find(word)}")

    lines.append("")
    find_key = "tree"
    lines.append(f"Поиск значения по ключу '{find_key}': {hash_dict.find(find_key)}")

    result_text = "\n".join(lines)

    with open("results.txt", "w", encoding="utf-8") as file:
        file.write(result_text)

    print(result_text)


if __name__ == "__main__":
    main()
