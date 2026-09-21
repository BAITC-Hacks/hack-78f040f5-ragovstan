def classify_message(message):
    text = message.lower()

    if any(word in text for word in ["справка", "где", "как получить"]):
        return "справка", "Здравствуйте! Информацию можно получить в учебном офисе."

    if any(word in text for word in ["очередь", "холодная"]):
        return "жалоба", "Здравствуйте! Спасибо за обращение. Мы передадим информацию ответственным сотрудникам столовой."

    if any(word in text for word in ["записаться", "консультацию"]):
        return "справка", "Здравствуйте! Для записи на консультацию обратитесь в учебный офис или воспользуйтесь системой записи."

    if "wi-fi" in text or "wifi" in text:
        return "жалоба", "Здравствуйте! Спасибо за сообщение. Мы передадим информацию о проблеме с Wi-Fi технической службе."

    if "парковка" in text:
        return "справка", "Здравствуйте! Парковка для гостей находится возле главного корпуса."

    return "другое", "Здравствуйте! Спасибо за обращение. Мы рассмотрим ваш запрос."


def main():
    with open("messages.txt", "r", encoding="utf-8") as file:
        messages = [line.strip() for line in file if line.strip()]

    for i, message in enumerate(messages, 1):
        category, answer = classify_message(message)

        print(f"{i}) {message}")
        print(f"Категория: {category}")
        print(f"Ответ: {answer}")
        print()


if __name__ == "__main__":
    main()