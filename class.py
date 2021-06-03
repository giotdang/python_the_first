
class Sieunhan:
    def __init__(self,name,weapon,color):
        self.name=name
        self.color=color
        self.weapon=weapon
    def xinchao(self):
        return "Toi la sieu nhan " + self.name
    @classmethod
    def from_string(cls,s): #normally these method have name from_...
        lst=s.split('-')
        new_lst=[st.strip() for st in lst]
        name=new_lst[0]
        weapon=new_lst[1]
        color=new_lst[2]
        return cls(name,weapon,color)

info="samset-sung-vang"
sieu_nhan_A=Sieunhan.from_string(info)

class member:
    def __init__(self,ho,ten):
        self.ho= ho
        self.ten=ten
        self.email=ho+'.'+ten+'@gmail.com'
    def ho_va_ten(self):
        return f"{self.ho} {self.ten}"

member_A=member("Vu","Quang")
print(member_A.ho_va_ten())

