import random

users = []

def is_even(user_id):
    return user_id % 2 == 0

def generate_message(user_id, name):
    if is_even(user_id):
        messages = [
            f'{name}, вам доступна скидка ❤️',
            f'{name}, скидка ваша ❤️',
        ]
        return random.choice(messages)
    else:
        messages = [
            f'{name}, к сожалению в скидке отказано',
            f'{name}, приходите за скидкой завтра',
        ]
        return random.choice(messages)

while True:
    name = input("Введите имя: ")
    user_id = int(input("Введите ID: "))

    users.append({
        "id": user_id,
        "name": name
    })

    print(generate_message(user_id, name))

    answer = input("Добавить ещё? (да/нет): ")
    if answer == "нет":
        break

print(users)

count_vip = 0
count_normal = 0

for user in users:
    if is_even(user["id"]):
        count_vip += 1
    else:
        count_normal += 1

print("VIP:", count_vip)
print("Обычные:", count_normal)