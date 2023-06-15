#Завдання 1
numbers = [4, -9, 8, -11, 8]
negative_count = sum(1 for num in numbers if num < 0)
print(negative_count)
#Завдання 2
players = ['Ешлі Барті', 'Симона Халеп', 'Наомі Осака', 'Кароліна Плішкова', 'Еліна Світоліна']
players[0], players[-1] = players[-1], players[0]
print(players)
#Завдання 3
quote = "Розумна людина пристосовується до світу; в нерозумна людина наполегливо намагається пристосувати світ до себе"
word1 = "розумний"
word2 = "нерозумний"
new_quote = quote.replace(word1, "temp").replace(word2, word1).replace("temp", word2)
print(new_quote)
