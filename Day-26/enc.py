
class ProfileStatus:
    def __init__(self):
        self.__foryou = ''
        self._forconnection = ''
        self.foreveryone = ''
    def get_url(self):
        return self.__foryou

    def set_url(self,url):
        self.__foryou = url

    @property
    def giveaccess(self):
        return self._forconnection

    @giveaccess.setter
    def giveaccess(self,url):
        self._forconnection = url

user = ProfileStatus()

print("Before update:",user.foreveryone)
user.foreveryone = "python.png"
print("After update:",user.foreveryone)

print("Before update:",user.get_url())
user.set_url("Functions.py")
print("After update:",user.get_url())

print("Before update:",user.giveaccess)
user.giveaccess = "java.png"
print("After update:",user.giveaccess)

'''
class Instagram:
    def __init__(self,username,password):
        self.__password =password
        self._post = []
        self.username = username

    def get_password(self):
        return self.__password

    def set_password(self,newpassword):
        self.__password = newpassword

    @property
    def access_post(self):
        return self._post

    @access_post.setter
    def access_post(self,newpost):
        self._post.append(newpost)

swathi = Instagram("swathi123",'s@123')

print("Before update:",swathi.username)
swathi.username = "dhanusree"
print("After update:",swathi.username)

print("Before update:",swathi.get_password())
swathi.set_password("dhanu@123")
print("After update:",swathi.get_password())

print("Before update:",swathi.access_post)
swathi.access_post = "sunrise.png"
swathi.access_post = "sunset.png"
swathi.access_post = "beach.png"
print("After update:",swathi.access_post)
'''