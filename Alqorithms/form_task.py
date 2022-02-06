
from cryptography.fernet import Fernet

users_list=[]
while True:
    print('qeydiyyatdan kecmek ucun [1] yazin\n   -istifadeci adiniz:\n   -password:\nsisteme daxil olmaq ucun [2] yazin:\nana menuya qayitmaq ucun [3] yazin:\nsistemden cixmaq ucun [4] yazin:')
    class emr_1():
        def __init__(self, _emr):
            self.emr = _emr
            self.list = list
    
        def get_name(self):
            global emr
            emr = self.emr
            return emr
        
    get_user_name = emr_1(int(input()))
    get_user_name.get_name()
    if emr != 1:
        print('emri duzgun daxil edin!')
        break

    
    class userAndPass(emr_1):
        def __init__(self,user,pas,list):
            self.user = user
            self.passw = pas
            self.user_list = list


        def data_base(self):
            global users_list
            self.user_list.append(self.user) 
            users_list = self.user_list
            return self.user_list


        def check_user_list(self):
            global users_list
            if self.user in users_list:
                print(f'{self.user} siz daha once qeydiyyatdan kecmisiz')
            else:
                print(f'{self.user} siz ilk defedirki qeydiyyatdan kecirsiz')
  
        
        def password(self):
            return self.passw 

        def enc(self):
            encpass = self.passw
            key = Fernet.generate_key()
            fernet = Fernet(key)
            encpass = fernet.encrypt(encpass.encode())
            return encpass

    user_pass=userAndPass(input('user:'), input('password:'),[])
    user_pass.check_user_list()
    user_pass.data_base()
    user_pass.password() 
    user_pass.enc()
    
    class sys(userAndPass):
        def __init__(self,_sys):
            self.system = _sys
            
        def syst(self):
            global system
            system = self.system
            return system
                                     
    system = sys(int(input('sisteme daxil olmaq ucun [2] yazin:')))
    system.syst()
    if system == 2:
        print('siz sisteme daxil oldunuz.')
    else:
        print('emri duzgun daxil etmediz!')
        break

    class Menu_or_out(sys):
        def __init__(self, menu):
            self.menu = menu

        def menu_in(self):
            global m
            self.menu == 3
            m = self.menu
            return m
        
    anamenu=Menu_or_out(int(input('ana menu:[3]/sistemden cixmaq ucun:[4]--')))
    anamenu.menu_in()
    if m == 3:
        pass
    elif m == 4:
        break
    else:
        print('error')
        break

       
           


            

       