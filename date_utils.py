"""
Модуль работы с датами.
Содержит функции для парсинга дат, проверки срока действия сертификата
и расчёта количества дней между датами.
Автор: Сариева Арина
Дата: 03.10.26
"""

from datetime import datetime, date

#формат даты, используемый в системе
DATE_FORMAT="%d.%m.%Y"


def parse_date(date_str):
    """
    Парсинг даты в формате "DD.MM.YYYY".

    Параметры:
        date_str (str): строка с датой

    Возвращает:
        datetime | None: объект datetime или None при ошибке
    """
    if not isinstance(date_str, str):
        return None
    try:
        return datetime.strptime(date_str, DATE_FORMAT)
    except ValueError:
        return None


def check_certificate_expiry(date_str):
    """
    Проверка срока действия сертификата.

    Параметры:
        date_str (str): дата окончания действия сертификата в формате "DD.MM.YYYY"

    Возвращает:
        tuple: (bool, str) — результат и сообщение
            - True, если сертификат действителен
            - False, если сертификат просрочен или дата некорректна
    """
    expiry=parse_date(date_str)
    if expiry is None:
        return False, "Некорректный формат даты"

    today=datetime.now()
    if expiry >= today:
        return True, f"Сертификат действителен до {expiry.strftime(DATE_FORMAT)}"
    else:
        return False, f"Сертификат просрочен {expiry.strftime(DATE_FORMAT)}"


def days_between(date1_str, date2_str):
    """
    Расчёт количества дней между двумя датами.

    Параметры:
        date1_str (str): первая дата в формате "DD.MM.YYYY"
        date2_str (str): вторая дата в формате "DD.MM.YYYY"

    Возвращает:
        int | None: количество дней (может быть отрицательным) или None при ошибке
    """
    d1=parse_date(date1_str)
    d2=parse_date(date2_str)
    if d1 is None or d2 is None:
        return None
    return (d2 - d1).days


#тестирование модуля при прямом запуске
if __name__ == "__main__":
    print("=== Тестирование date_utils ===")

    #тесты parse_date
    print(parse_date("01.01.2025"))       #datetime(2025, 1, 1, 0, 0)
    print(parse_date("32.13.2025"))       #None
    print(parse_date("2025-01-01"))       #None

    #тесты check_certificate_expiry
    print(check_certificate_expiry("01.01.2030"))  #(True, ...)
    print(check_certificate_expiry("01.01.2020"))  #(False, 'Сертификат просрочен ...')
    print(check_certificate_expiry("abc"))         #(False, 'Некорректный формат даты')

    #тесты days_between
    print(days_between("01.01.2025", "10.01.2025"))  #9
    print(days_between("10.01.2025", "01.01.2025"))  #-9
    print(days_between("abc", "01.01.2025"))         #None
