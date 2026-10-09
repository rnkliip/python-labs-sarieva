#Лабораторная работа №1
#Студент: Сариева Арина
#Группа: ОИБАС-21
#Вариант: 3

"""
Задание 1.1. validate_navigation_status — описание статуса навигации AIS
Задание 1.2. calculate_risk_score       — расчёт интегральной оценки риска
Задание 1.3. anonymize_ip               — маскирование IP-адреса


=============================================
Задание 1.1. Название функции
=============================================
"""

def validate_navigation_status(status_code):
    """
    Проверка и описание статуса навигации AIS.
    Параметры:
        status_code (int): код статуса навигации (0–15)
    Возвращает:
        str: текстовое описание статуса или "Неизвестный статус"
    Пример:
        >>> validate_navigation_status(1)
        'На якоре'
        >>> validate_navigation_status(99)
        'Неизвестный статус'
    """
    #словарь описаний статусов навигации AIS
    NAVIGATION_STATUSES={
        0: "В плавании",
        1: "На якоре",
        2: "Не на ходу",
        3: "Ограниченная манёвренность",
        4: "Ограничено осадкой",
        5: "Пришвартован",
        6: "На буксире",
        7: "На тралении",
        8: "Рыболовство",
        9: "В плавании (резерв)",
        10: "В плавании (резерв)",
        11: "В плавании (резерв)",
        12: "В плавании (резерв)",
        13: "В плавании (резерв)",
        14: "В плавании (резерв)",
        15: "Не определён",
    }

    #проверка типа данных
    if not isinstance(status_code, int):
        return "Неизвестный статус"

    #проверка диапазона
    if status_code < 0 or status_code > 15:
        return "Неизвестный статус"

    #возврат описания (если код отсутствует в словаре — "Неизвестный статус")
    return NAVIGATION_STATUSES.get(status_code, "Неизвестный статус")


"""
=============================================
Задание 1.2. Название функции
=============================================
"""

def calculate_risk_score(threat, vulnerability, asset):
    """
    Расчёт интегральной оценки риска.

    Формула: risk = (threat * vulnerability * asset) / 1000

    Параметры:
        threat (float): уровень угрозы (0–10)
        vulnerability (float): уровень уязвимости (0–10)
        asset (float): ценность актива (0–10)

    Возвращает:
        dict: словарь с ключами:
            - score (float): числовое значение риска
            - level (str): уровень риска
                «Низкий» (< 20), «Средний» (20–50), «Высокий» (> 50)

    Пример:
        >>> calculate_risk_score(8, 7, 9)
        {'score': 50.4, 'level': 'Высокий'}
    """
    #проверка на корректность входных данных
    try:
        threat = float(threat)
        vulnerability = float(vulnerability)
        asset = float(asset)
    except (ValueError, TypeError):
        return {"score": 0.0, "level": "Некорректные данные"}

    #расчёт риска по формуле
    score = (threat * vulnerability * asset) / 1000

    #классификация уровня риска
    if score < 20:
        level = "Низкий"
    elif score <= 50:
        level = "Средний"
    else:
        level = "Высокий"

    return {"score": round(score, 3), "level": level}


"""
=============================================
Задание 1.3. Название функции
=============================================
"""

def anonymize_ip(ip, mask="XXX"):
    """
    Маскирование последнего октета IP-адреса.

    Параметры:
        ip (str): IP-адрес в формате "x.x.x.x"
        mask (str): маска для последнего октета (по умолчанию "XXX")

    Возвращает:
        str: замаскированный IP-адрес или сообщение об ошибке

    Пример:
        >>> anonymize_ip("192.168.1.100")
        '192.168.1.XXX'
        >>> anonymize_ip("10.0.0.1", mask="***")
        '10.0.0.***'
        >>> anonymize_ip("abc")
        'Ошибка: некорректный IP-адрес'
    """
    #проверка типа
    if not isinstance(ip, str):
        return "Ошибка: некорректный IP-адрес"

    #разбиение на октеты
    parts = ip.split(".")
    if len(parts) != 4:
        return "Ошибка: некорректный IP-адрес"

    #проверка каждого октета
    for octet in parts:
        if not octet.isdigit():
            return "Ошибка: некорректный IP-адрес"
        if not (0 <= int(octet) <= 255):
            return "Ошибка: некорректный IP-адрес"

    #замена последнего октета на маску
    return f"{parts[0]}.{parts[1]}.{parts[2]}.{mask}"


"""
=============================================
Демонстрация работы функций
=============================================
"""

if __name__ == "__main__":
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ФУНКЦИЙ (ВАРИАНТ 3)")
    print("=" * 60)

    #Задание 1.1. validate_navigation_status
    print("\n--- Задание 1.1. validate_navigation_status ---")
    test_statuses = [0, 1, 3, 5, 8, 15, 99, -1, "abc"]
    for code in test_statuses:
        result = validate_navigation_status(code)
        print(f"validate_navigation_status({code!r}) → {result}")

    #Задание 1.2. calculate_risk_score
    print("\n--- Задание 1.2. calculate_risk_score ---")
    test_cases = [
        (2, 3, 4),    #низкий
        (5, 6, 7),    #средний
        (8, 7, 9),    #высокий
        (10, 10, 10), #высокий
    ]
    for t, v, a in test_cases:
        result = calculate_risk_score(t, v, a)
        print(f"calculate_risk_score({t}, {v}, {a}) → {result}")

    #Задание 1.3. anonymize_ip
    print("\n--- Задание 1.3. anonymize_ip ---")
    test_ips = [
        "192.168.1.100",
        "10.0.0.1",
        "255.255.255.255",
        "0.0.0.0",
    ]
    for ip in test_ips:
        result = anonymize_ip(ip)
        print(f"anonymize_ip({ip!r}) → {result}")

    #тест с другой маской
    print(f"anonymize_ip('192.168.1.100', mask='***') → "
          f"{anonymize_ip('192.168.1.100', mask='***')}")

    #некорректные IP
    print("\n--- Проверка некорректных IP ---")
    for bad in ["abc", "192.168.1", "192.168.1.256", "192.168.1.abc", ""]:
        print(f"anonymize_ip({bad!r}) → {anonymize_ip(bad)}")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)
