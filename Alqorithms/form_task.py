
from cgi import test
from re import S
from cryptography.fernet import Fernet



while True:
    print('qeydiyyatdan kecmek ucun [1] yazin\n   -istifadeci adiniz:\n   -password:\nsisteme daxil olmaq ucun [2] yazin:\nana menuya qayitmaq ucun [3] yazin:\nsistemden cixmaq ucun [4] yazin:')
    class person():
        def __init__(self,_emr,_name,passw,list):
            self.emr=_emr
            self.name=_name
            self.passw=passw
            self.list=list
    
        def get_name(self):
            if self.emr==1:
                return self.name

        def password(self):
            if self.emr==1:
                return self.passw 


        def enc(self):
            encpass = self.passw
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encpass = fernet.encrypt(encpass.encode())
            return encpass

        def data_base(self):
            self.list.append(self.name) 
            return self.list  
    
        def check_user_list(self):
            if self.name in self.list:
                print(f'{self.name} siz daha once qeydiyyatdan kecmisiz')
            else:
                print(f'{self.name} siz ilk defedirki qeydiyyatdan kecirsiz')

    user_name=person(int(input()),input('-istifadeci adiniz:'),input('parolunuz:'),[])
    user_name.get_name()
    user_name.check_user_list()
    user_name.data_base()
    user_name.password()
    user_name.enc()


    class sys(person):
        def __init__(self,_sys):
            self.system=_sys
            
        def syst(self):
            self.system=2
            if self.system==2:
                print('xos gelmisiz.siz sisteme daxil olmusuz')               
               
    system=sys(int(input('sisteme daxil olmaq ucun [2] yazin:')))
    system.syst()


    class Menu(sys):
        def __init__(self, menu):
            self.menu=menu


        def menu_in(self):
            global m
            self.menu==3
            m=self.menu
            return m




    anamenu=Menu(int(input('ana menu:')))
    anamenu.menu_in()
    if m!=3:
        break
    



    class out(Menu):
        def __init__(self,outsys):
            self.out_sys=outsys


        def out_system(self):
            global s 
            self.out_sys=4
            s=self.out_sys
            return s

    sys_=out(int(input('sistemden cix:')))

    sys_.out_system()


    if s==4:
        break