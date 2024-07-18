import random

def ages():
    
    return random.randint(18, 65)

def salaries():

    return random.uniform(10000, 50000)

import random


def experiences(max_experience):
    return random.randint(0, max_experience)


def check_age():
    age = ages()
    experience = experiences(age)
    print(f"Yosh: {age}")
    print(f"Tajriba: {experience}")

    if age < 18:
        raise ValueError("Yosh 18 dan kichik bo'lishi mumkin emas")

    first_max_experience = age - 18
    max_experience = first_max_experience if first_max_experience > 0 else 2
    if experience <= max_experience:
        print(f"Tajriba mos keldi: {experience}")
        return experience
    else:
        while True:
            func_experience = experiences(max_experience)
            print(f"Tasodifiy tajriba: {func_experience}")
            if func_experience <= max_experience and func_experience > 0:
                return func_experience

print(check_age())
