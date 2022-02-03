

class person():
    def __init__(self,_emr,_name,_password,_sys,_list):
        self.name=_name
        self.passw=_password
        self.emr=_emr
        self.into_sys=_sys
        self.user_list=_list

    def data_base(self):
        self.user_list.append(self.name) 
        return self.user_list  
    def get_name(self):
        if self.emr==1:
            return self.name


    def password(self):
        if self.emr==1:
            return self.passw


    def yoxla(self):
        if self.name in self.user_list:
            print(f'{self.name} siz daha once qeydiyyatdan kecmisiz')
        else:
            print(f'{self.name} siz ilk defedirki qeydiyyatdan kecirsiz')

    def get_sys(self):
        if self.into_sys==2:
            print(f'{self.name} xos gelmisiz.Siz artiq sisteme daxil olmusuz.')
            

user_name=person(int(input('qeydiyyatdan kecmek ucun [1] yazin:')),input('-istifadeci adiniz:'),input('parolunuz:'),int(input('sisteme daxil olmaq ucun [2] yazin:')),[])

user_name.get_name()
user_name.data_base()
user_name.yoxla()
user_name.password()
user_name.get_sys()



