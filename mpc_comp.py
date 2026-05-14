import random
import math


def secret_share_comp(x):
    r = random.randint(0, 17179869183) #2^34=17179869184
    #print(r)
    secret_share_of_x_0 = (x - r) % (17179869184**2)
    secret_share_of_x_1 = r
    return secret_share_of_x_0, secret_share_of_x_1

def secret_share(x):
    r = random.randint(0, 17179869184**2-1) #2^34=17179869184
    #print(r)
    secret_share_of_x_0 = (x - r) % (17179869184**2)
    secret_share_of_x_1 = r
    return secret_share_of_x_0, secret_share_of_x_1


def multi_comp(x0,x1, y0,y1):

    a = random.randint(0, 17179869183)  # 2^17=131072
    b = random.randint(0, 17179869183)  # 2^17=131072
    c = a*b

    a0,a1 = secret_share_comp(a)
    b0,b1 = secret_share_comp(b)
    c0,c1 = secret_share_comp(c)

    e0 = (x0 - a0) % (17179869184**2)
    e1 = (x1 - a1) % (17179869184**2)
    f0 = (y0 - b0) % (17179869184**2)
    f1 = (y1 - b1) % (17179869184**2)

    e = (e0 + e1) % (17179869184**2)
    f = (f0 + f1) % (17179869184**2)

    secret_share_0 = (c0 + e * b0 + f * a0 + e * f) % (17179869184**2)
    secret_share_1 = (c1 + e * b1 + f * a1) % (17179869184**2)

    return secret_share_0, secret_share_1



def secure_compare(x, y):
    #print("x and y", x, y, x + y)
    x0, x1 = secret_share(x)
    y0, y1 = secret_share(y)
    r = random.randint(1, 2**17) # 2^8

    r_sign = random.randint(1, 8)
    if r_sign % 2 == 0:
        r_sign = -1
    else:
        r_sign = 1

    r = r_sign * r

    r_sign_bool_0 =

    #print(f"r={r}")
    r0, r1 = secret_share_comp(r)
    #print("securecompare1:", r0, r1, x0 - y0, x1 - y1)

    r_x_y_0, r_x_y_1 = multi_comp(r0, r1, x0 - y0, x1 - y1)
    #print("securecompare2:", r_x_y_0, r_x_y_1, r_x_y_0 + r_x_y_1)
    r_x_y = (r_x_y_0 + r_x_y_1) % (17179869184**2)
    if r_x_y == 0 or r_x_y >= (17179869184**2/2) :
        return 1  #r*(x-y)为负数/0，x-y<=0，x<=y
    else:
        return 0  #x>y


if __name__ == "__main__":
    for i in range(10000):
        x = random.randint(-17179869183, 17179869183)      #2^34=17179869184
        y = random.randint(-17179869183, 17179869183)
        # x = -17179869183
        # y = 17179869183

        pi = secure_compare(x, y)
        print(f"pi={pi}, x={x},y={y}")
        if x<=y and pi==0:
            print("ERRORCOMP1")
            exit(0)
        if x > y and pi == 1:
            print("ERRORCOMP2")
            exit(0)
        # if  pi_0+pi_1 >= 17179869184:
        #     print("大")

