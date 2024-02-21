# Курсовая работа № 4

## Задание

Напишите программу, которая будет получать информацию о вакансиях с платформы hh.ru в России, 
сохранять ее в файл и позволять удобно работать с ней: добавлять, фильтровать, удалять.

### Требования к реализации
- Создать абстрактный класс для работы с API сервиса с вакансиями. Реализовать класс, наследующийся от абстрактного класса, для работы с платформой hh.ru. Класс должен уметь подключаться к API и получать вакансии.
- Создать класс для работы с вакансиями. В этом классе самостоятельно определить атрибуты, такие как название вакансии, ссылка на вакансию, зарплата, краткое описание или требования и т. п. (всего не менее четырех атрибутов). Класс должен поддерживать методы сравнения вакансий между собой по зарплате и валидировать данные, которыми инициализируются его атрибуты.
- пределить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл, получения данных из файла по указанным критериям и удаления информации о вакансиях. Создать класс для сохранения информации о вакансиях в JSON-файл. Дополнительно, по желанию, можно реализовать классы для работы с другими форматами, например с CSV- или Excel-файлом, с TXT-файлом.
- Создать функцию для взаимодействия с пользователем. Функция должна взаимодействовать с пользователем через консоль. Возможности этой функции должны быть следующими:
1. ввести поисковый запрос для запроса вакансий из hh.ru;
2. получить топ N вакансий по зарплате (N запрашивать у пользователя);
3. получить вакансии с ключевым словом в описании.
