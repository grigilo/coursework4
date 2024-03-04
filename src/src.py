from abc import ABC
import requests
import json


# class Request_attribute:
#     def __init__(self, name, quantity):
#         self.name = input("Введите искомые вакансии")
#         self.quantity = input("Какое количество вакансий отобразить?")


class HH_API:
    # url = "https://api.hh.ru"

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.url = "https://api.hh.ru"

    @property
    def api_hh(self):
        data = requests.get(f"{self.url}/vacancies",
                            params={'text': self.name,
                                    'area': 113,
                                    'enable_snippets': "true",
                                    'only_with_salary': "true",
                                    'per_page': self.quantity}).json()
        return data
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(date, f, ensure_ascii=False)

    def get_json(self):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(self.api_hh, f, ensure_ascii=False)


# print(date)
# class HH_API(ABC):
#
#     pass
#
# class Vacancy(HH_API):
#     def __init__(self):
#
#         pass
q = HH_API('бухгалтер', 50)
q.get_json()
