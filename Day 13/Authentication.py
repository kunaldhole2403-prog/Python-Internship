import random 
import time
from abc import ABC,abstractmethod
class Login(ABC):
    @abstractmethod
    def authenication(self):
        pass
class User(Login):
    def getUser(self,username,pwd):
        self.username = username
        self.pwd = pwd
        self.user = input("Enter your Username: ")
        self.p = int(input("Enter Your Password: "))
    def authenication(self):
        if self.username == self.user and self.pwd == self.p:
            print("Username and password is correct, we have sent a otp to verify:")
            self.generate_otp()
            otp_time = time.time()
            self.Userotp = int(input("Enter the recive OTP:"))
            if time.time() > otp_time + 1800:
                print("Try again OTP has expire")
            else:
                self.check_otp(self.Userotp)
        else:
            print("Incorrect Username or password")
    def generate_otp(self):
        self.num = random.randint(1000,9999)
        print("This OTP valid for 30 min",self.num)
    def check_otp(self,Userotp):
        self.Userotp = Userotp
        if self.num == self.Userotp:
            print("Login Successfull")
        else:
            print("Invalid OTP")
User1 = User()
User1.getUser("Kunal@123",4764)
User1.authenication()

