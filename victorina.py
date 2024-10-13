from random import choice

student = input('представтьсь пожалуйста')
try:
    level = int(input('выберите уровень сложности 1-5:'))
except:
    level = 1
    print('установлен первый уровень смложности')
if level < 1 or level > 3:
    level = 1
    print('утстановлен первый уровень сложности')

print(f'хорошо, {student}. давай поиграем в угадай в животное')
animals = {
    1: [('это большое серое живоьтное с хобоотом', 'слон'),
        ('этот коричневый мохнатый зверь люит мед', 'медведь')],
    2:[('этот хищник - король джунглей', 'Лев'),
       ('это живоьтное живет в антарктиде и умеет плавать', 'пингвин')],
    3:[('это млекопитающее обитает в океане и явл самым большим животным', 'синий кит'),
       ('этот ночной хищник охотиится в пустыне и может выживать без воды', 'фенек')]
}
points = 0
for i in range(3):
    description, correct_answer = choice(animals[level])
    print(f'{student}, что это за животное: {description}? ', end='')
    student_answer = input().strip(). lower()
    if student_answer == correct_answer.lower():
        points += 1
        print(f'правильно', points)
    else:
        print(f'не правильно, это было{correct_answer}')

if points == 3:
    print(f'ты настоящий знаток животных, {student}')
elif points == 2:
    print(f'неплохо, {student}, но нужно улучшать зания')
else:
    print(f'ты плохо знаешь живоьтных, {student}.')



