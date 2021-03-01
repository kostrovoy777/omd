# coding=utf-8
def step1():
    print(
        'Утка киллер вышла на задание. '
        "Какое оружие ей взять?"
    )
    gun = ""
    guns = {'винтовку', 'нож', 'резиновую уточку'}
    while gun not in guns:
        print("{}/{}/{}".format(*guns))
        gun = input()
    print("Утка взяла " + gun)
    return gun


def step2():
    print(
        'Утка обнаружила свою цель. '
        'Какую позицию ей занять?'
    )
    location = ""
    locations = {'крыша здания', 'подобраться поближе'}
    while location not in locations:
        print("{}/{}".format(*locations))
        location = input()
    return location


def step3(gun, location):
    messages1 = {
        "винтовку": "и одним точным выстрелом устранила цель.",
        "нож": "бросила нож, но он не долетел!",
        "резиновую уточку": "бросила резиновую уточку перед целью, которая подскользьнулась на уточке, и расшибла "
                            "себе голову!",
    }
    messages2 = {
        "винтовку": "расшибла ей голову прикладом. Но это многие увидели",
        "нож": " тихо устранила цель ножом как ассасин!",
        "резиновую уточку": "бросила резиновую уточку перед целью, которая подскользьнулась на уточке, и расшибла "
                            "себе голову!",
    }

    if location == "крыша здания":
        print(
            'Утка забралась на крышу, выждала момент, '
            + messages1.get(gun)
        )
    else:
        print(
            'Утка незаметно подошла к цели в притык, и '
            + messages2.get(gun)
        )

    print(
        'Теперь утке-киллеру нужно уходить. '
        'Как она покинет территорию?'
    )
    vehicle = ''
    vehicles = {'пешком', 'на машине', 'на метро'}
    while vehicle not in vehicles:
        print("{}/{}/{}".format(*vehicles))
        vehicle = input()
    return vehicle


def step4():
    print(
        'Утка смогла скрыться с места преступления. '
        'Как ей действовать дальше?'
    )
    option = ""
    options = {'идти домой', 'сходить в супермаркет за хлебными крошками'}
    while option not in options:
        print("{}/{}".format(*options))
        option = input()
    return option


def step5(option):
    if option == "сходить в супермаркет за хлебными крошками":
        print("Утку нашли по горячим следам, и арестовали! The end")
        return

    print(
        'Утка добралась до дома. '
        'Что ей делать дальше?'
    )
    option = ""
    options = {'залечь на дно', 'закатить вечерику'}
    while option not in options:
        print("{}/{}".format(*options))
        option = input()
    if option == "закатить вечеринку":
        print("Утка сильно шумела, соседи вызвали копов, и ее арестовали! The end")
    else:
        print("Утка залегла на дно, и вскоре ей пришла оплата за задание. Довольная утка стала дожидаться следующего "
              "задания. The end")
    return


if __name__ == '__main__':
    gun = step1()
    location = step2()
    vehicle = step3(gun, location)
    step5(step4())

