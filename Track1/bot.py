import re


def load_faq(filename):
    faq = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    for i in range(0, len(lines), 2):
        question = lines[i].replace("Вопрос: ", "")
        answer = lines[i + 1].replace("Ответ: ", "")
        faq.append((question, answer))

    return faq


def get_keywords(text):
    words = re.findall(r"\b[а-яёa-z0-9]+\b", text.lower())

    stop_words = {
        "когда", "какой", "какие", "кто", "будет", "будут",
        "нужно", "можно", "ли", "мы", "в", "на", "и", "до",
        "для", "про", "это", "как"
    }

    return set(word for word in words if word not in stop_words)


def find_answer(user_question, faq):
    user_keywords = get_keywords(user_question)

    best_answer = None
    best_score = 0

    for question, answer in faq:
        question_keywords = get_keywords(question)
        score = len(user_keywords & question_keywords)

        if score > best_score:
            best_score = score
            best_answer = answer

    if best_score >= 1:
        return best_answer

    return "Не знаю."


def main():
    faq = load_faq("faq.txt")

    print("FAQ-бот запущен.")
    print("Введите вопрос или 'exit' для выхода.")

    while True:
        user_question = input("> ")

        if user_question.lower() == "exit":
            print("До свидания!")
            break

        answer = find_answer(user_question, faq)
        print(answer)


if __name__ == "__main__":
    main()