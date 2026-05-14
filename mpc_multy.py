
import random
import math
import time

#1.57079632679489
#
def secret_share(x):
    r = random.randint(-2**33, 2**33-1)
    secret_share_of_x_0 = (x - r) % 17179869184**2   #对应乘法得到的最大值的明文空间
    secret_share_of_x_1 = r % 17179869184**2
    return secret_share_of_x_0, secret_share_of_x_1


def multi(x0,x1, y0,y1):

    # a = random.randint(0, 17179869184**2-1)  # 2^17=131072
    # b = random.randint(0, 17179869184**2-1)  # 2^17=131072

    a = random.randint(-2**33, 2**33-1)  # 2^17=131072
    b = random.randint(-2**33, 2**33-1)  # 2^17=131072
    c = a*b

    a0,a1 = secret_share(a)
    b0,b1 = secret_share(b)
    c0,c1 = secret_share(c)

    e0 = (x0 - a0)
    e1 = (x1 - a1)
    f0 = (y0 - b0)
    f1 = (y1 - b1)

    e = (e0 + e1)
    f = (f0 + f1)


    # e0 = (x0 - a0) % (17179869184**2)
    # e1 = (x1 - a1) % (17179869184**2)
    # f0 = (y0 - b0) % (17179869184**2)
    # f1 = (y1 - b1) % (17179869184**2)
    #
    # e = (e0 + e1) % (17179869184**2)
    # f = (f0 + f1) % (17179869184**2)



    secret_share_0 = (c0 + e * b0 + f * a0 + e * f) % (17179869184**2)
    secret_share_1 = (c1 + e * b1 + f * a1) % (17179869184**2)

    return secret_share_0, secret_share_1


if __name__ == "__main__":
    # pi = 4
    # pj = 3
    # fx0,fx1 = multi(pi, pj)
    # print(f"3: fx0+fx1={fx0 + fx1},pi * pj = {pi * pj}")  # multi函数存在较大误差
    start = time.time()
    for i in range(100000):
        pi = random.randint(0, 17179869184-1)
        pj = random.randint(0, 17179869184-1)
        pi_0, pi_1 = secret_share(pi)
        pj_0, pj_1 = secret_share(pj)
        fx0, fx1 = multi(pi_0, pi_1,pj_0, pj_1)
        print(f"3: fx0+fx1={(fx0 + fx1) % 17179869184**2},pi * pj = {pi * pj}")  # multi函数存在较大误差
        if (fx0 + fx1) % 17179869184**2 != pi * pj:
            print("ERROR")
            print(fx0, fx1,pi ,pj)
    end = time.time()
    print(end - start)




