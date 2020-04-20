class Character:

    name = ''
    age = 0
    sex = ''

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def information(self):
        print("{}는 {}세이고, {}입니다.".format(self.name,self.age,self.sex))


zg = Character("짱구",5,"남자")
dm = Character("도라에몽",14,"남자")
cn = Character("코난",8,"남자")
cl = Character("쇼콜라",15,"여자")
am = Character("아무",12,"여자")
gy = Character("가영",16,"여자")

zg.information()
dm.information()
cn.information()
cl.information()
am.information()
gy.information()
              
              
