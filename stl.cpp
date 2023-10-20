#include <iostream>
#include <string>
#include <list>

int main() {

    setlocale(LC_ALL, "Russian");

    std::string input;
    std::cout << "Введите строку: ";
    std::getline(std::cin, input);

    std::list<char> charList;

    // Заполняем список символами из введенной строки
    for (char c : input) {
        charList.push_front(c);
    }

    // Выводим символы в обратной последовательности
    std::cout << "Строка в обратной последовательности: ";
    for (char c : charList) {
        std::cout << c;
    }
    std::cout << std::endl;

    return 0;
}
