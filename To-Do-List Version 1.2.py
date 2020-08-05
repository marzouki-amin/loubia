text="""
Welcome Amin hope you're fine ! ☺
This is your To-Do-List app and here's some instructions :
1-Please enter your taches.
2-Time must respect the following format: 'H:M:S' or (H:M:S).
3-Time must be a real number.
4-To finish please make sure to type 0.
Hope you enjoy the experience and have a nice day sir ! ♥
"""
print(text)
class temps():
        def __init__(self, temps):
            if type(temps) == str:
                l=temps.split()
                self.h=int(l[0])
                self.m=int(l[1])
                self.s=int(l[2])
            elif type(temps) == tuple:
                self.h=temps[0]
                self.m=temps[1]
                self.s=temps[2]
            else:
                print('Please enter a valide time type !')
        def __str__(self):
            return(self.h, ':', self.h, ':', self.h)
        def __lt__(self, other):
            if self.h < other.h:
                return True
            elif other.h < self.h:
                return False
            else:
                if self.m < other.m :
                    return True
                elif other.m< self.m :
                    return False
                else:
                    if self.s < other.s :
                        return True
                    else:
                        return False
d={}
def data_entry():
    to_do=input('Please what do you want to do? : ')
    td_time=input('Please when do you want to do it? : ')
    d.setdefault(to_do,td_time)
    while to_do != '0' and td_time != 0:
        to_do=input('Please what do you want to do? : ')
        td_time=input('Please when do you want to do it? : ')
        d.setdefault(to_do,td_time)
    return d