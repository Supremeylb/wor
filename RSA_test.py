# -*- coding:utf8 -*-

"""
p,q
n = pq
e is relatively-prime (p-1)(q-1)
de mod (p-1)(q-1) is 1
"""
from fractions import gcd

P = 3
Q = 11


class RSA_test(object):
    def __init__(self, str_to_send):
        self.n, self.fn = P * Q, (P - 1) * (Q - 1)
        self.e, self.d, self.ku, self.kr = None, None, None, None
        self.str_result, self.digit_after_calcu = [], []
        self.str_to_send = str_to_send
        self.ready = False
        self.calcu()

    def calcu(self):
        for i in range(2, self.fn + 1):
            if not self.e and gcd(self.fn, i) == 1:
                self.e = i
                if not self.d and divmod(self.e ** (-1) * i, self.fn)[1] == 1:
                    self.d = i
                    break
        if self.e and self.d:
            self.ku = (self.e, self.n)
            self.kr = (self.d, self.n)  # for secret key
            self.ready = True
        else:
            print("no ku,kr is available")

    def en_to_digit(self, en):
        return ord(en) - 96 if ord(en) > 96 else ord(en) - 48

    def digit_to_en(self, digit_list):
        str_list = []
        for item in digit_list:
            str_list.append(chr(item))
        return str_list

    def encrypt(self):
        for letter in str(self.str_to_send):
            self.digit_after_calcu.append(divmod(self.en_to_digit(letter) ** self.d, self.n)[1])
        return self.digit_after_calcu

    def jie_encry(self, digit_list):
        for item in digit_list:
            self.str_result.append(divmod(item ** self.d, self.n)[1])
        return self.digit_to_en(self.str_result)

    def main(self):
        if self.ready:
            calcu_result = self.encrypt()
            print(calcu_result)
            self.digit_to_en(calcu_result)
        else:
            print("No ready")


if __name__ == '__main__':
    rsa = RSA_test("Bryan")
    rsa.main()
