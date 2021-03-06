"""
    비밀번호 생성시 의 적합성 체크
    1. 비밀번호의 길이는 6-10
    2. 숫자와 알파벳으로만 구성되어야 함
    3. 대문자와 소문자가 섞여야 함 ( 대문자 1개 이상, 소문자 0개 이상)
    4. 위의 조건에 부합하면 잘못된 상황을 출력하고
       조건을 모두 만족하면 가능한 비밀번호임을 출력한다.
"""

import re
def pwd_check(pwd):
    regAlphabetAndNumber = re.compile("[^a-zA-Z0-9]+")
    regUpperAlphabet = re.compile("[A-Z]+")
    if len(pwd)<6 or len(pwd)>10:
        print("길이 부적합")
        return
    if regAlphabetAndNumber.search(pwd) != None:
        print("숫자와 알파벳으로만 구성되어야 함")
        return
    if regUpperAlphabet.search(pwd) == None:
        print("대문자가 포함되어 있어야 함")
        return
    print("사용 가능한 비밀번호")

pwd_check('abcdE')          # 길이오류
pwd_check('abcdef')         # 대문자 포함하지 않아 오류
pwd_check('Abcdef2')        # 성공
pwd_check('Abcdef_2')       # 특수문자 포함
# print(pwd_check('abcdE'))
# print(pwd_check('abcdef'))
# print(pwd_check('Abcdef2'))
# print(pwd_check('Abcdef_2'))



# 한번에 체크하는 방식
# 전방탐색
# def pwd_check(pwd):
#     p = re.search('^(?=.*[A-Z]).[A-Za-z0-9]{6,10}$',pwd)
#     if p:
#         return print(True)
#     else:
#         return print(False)