import random

# Словник челенджів для різних настроїв
challenges = {
    "happy": [
        "Придумай назву для своєї гри",
        "Напиши 3 речі, які сьогодні вдалися"
    ],
    "tired": [
        "Зроби перерву на 5 хвилин",
        "Намалюй простий план свого дня"
    ],
    "bored": [
        "Придумай нове правило для улюбленої гри",
        "Зміни щось маленьке у своїй кімнаті"
    ]
}

# Список челенджів спеціально для навчального режиму (study)
study_challenges = [
    "Повторити 3 нові Python-команди",
    "Пояснити другу, що таке змінна",
    "Знайти одну помилку в маленькому коді",
    "Написати 3 рядки коду з print()"
]

# Стандартні челенджі, якщо настрій невідомий
default_challenges = [
    "Випий води",
    "Запиши одну маленьку ціль на сьогодні"
]


def choose_challenge(mood, energy, mode):
    # Якщо обрано режим навчання
    if mode.lower() == "study":
        challenge = random.choice(study_challenges)
    # Якщо введений настрій є у словнику
    elif mood.lower() in challenges:
        challenge = random.choice(challenges[mood.lower()])
    # Якщо введено невідомий настрій — безпечний нейтральний вибір
    else:
        challenge = random.choice(default_challenges)

    # Якщо рівень енергії високий, додаємо мотиваційний хвіст
    if energy > 7:
        challenge = challenge + " і зроби це просто зараз!"

    return challenge


def calculate_points(energy, mode):
    # Якщо енергія не в діапазоні від 1 до 10 — повертаємо 0 балів
    if energy < 1 or energy > 10:
        return 0

    # Базово нараховуємо 5 балів
    points = 5

    # Додаткові бали за рівень енергії
    if 7 <= energy <= 10:
        points += 3
    elif 1 <= energy <= 3:
        points += 1

    # Додатковий бонус за режим study
    if mode.lower() == "study":
        points += 2

    return points


# Головна точка входу в програму
if __name__ == "__main__":
    print("=== Генератор міні-челенджів ===")
    name = input("Як тебе звати? ")
    mood = input("Який у тебе настрій? happy / tired / bored: ")

    raw_energy = input("Скільки в тебе енергії від 1 до 10? ")
    # Безпечне перетворення введеного значення на ціле число
    if raw_energy.isdigit():
        energy = int(raw_energy)
    else:
        energy = 0

    mode = input("Обери режим fun або study: ")

    # Отримуємо завдання та рахуємо бали
    challenge = choose_challenge(mood, energy, mode)
    points = calculate_points(energy, mode)

    # Виводимо результат
    print()
    print(f"{name}, твій челендж:")
    print(challenge)
    print(f"Бали за виконання: {points}")