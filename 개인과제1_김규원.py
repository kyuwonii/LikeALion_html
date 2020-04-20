mutsa_dict = dict()

mutsa_dict['이화여대 멋사 대표님'] = '은진'
mutsa_dict['멋사 대장'] = '두희'
mutsa_dict['이화여대 멋사 튜터님'] = '유진'
mutsa_dict['이화여대 멋사 회장님'] = '연주'


for key in mutsa_dict.keys() :
    print("다음은 누구에 대한 설명일까요?")
    print("\""+ key +"\"")
    print("(1)은진 (2)연주 (3)두희 (4)유진")
    name = input()
    if name == mutsa_dict[key] :
        print("정답입니다!")
    else:
        print("오답입니다!")

    print("")
