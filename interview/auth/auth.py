import bcrypt
from hashlib import md5

password = 'qwerty'

# hashed_pwd = md5(password.encode())

# d8578edf8458ce06fbc5bb76a58c5ca4

salt = bcrypt.gensalt()
# b'$2b$12$Z4.A/NPIHiYL.RFTrgGY4.'

hashed_pwd = bcrypt.hashpw(password.encode(), salt)
# b'$2b$12$Z4.A/NPIHiYL.RFTrgGY4.7ZM8vFXjqfR4NUlOYb01Xx6gY1maR3G'

salt = bcrypt.gensalt()
# b'$2b$12$wwCHJ2pgj2mMRMf/RHe4Hu'

hashed_pwd2 = bcrypt.hashpw(password.encode(), salt)
# b'$2b$12$wwCHJ2pgj2mMRMf/RHe4HuSdVngTXx8vUh0dCPVqgoPVm0IUDIdj2'

check_1 = bcrypt.checkpw(password.encode(), hashed_pwd)
check_2 = bcrypt.checkpw(password.encode(), hashed_pwd2)


class A:

    def __init__(self):
        pass

    def hello(self):
        self.__hello()

    def __hello(self):
        print('hi')

a = A()

for _ in range(10):
    print(_)

a.hello()

b = [[]]*5

b[0].append(1)

b