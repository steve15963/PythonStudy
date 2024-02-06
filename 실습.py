import re
def password_vaild_check(pwd):
    """ 비밀번호 체크
    args:
        pwd(str) : password 문자열
    return:
        True or False ( boolean ) : 응답
    """
    up = False
    lo = False

    if 6 > len(pwd) or len(pwd) > 12:
        print("길이 조건 미만족")
        return False
    for c in pwd:
        if not c.isnumeric() and not c.isalpha():
            print("특수 문자가 있습니다.")
            return False
        if c.isalpha():
            up = up or c.isupper()
            lo = lo or c.islower()
        if up & lo :
            break
    if not (up & lo):
        print("대소문자 규칙 미만족")
        return False
    

    print("조건에 만족합니다.")
    return True
    

if __name__ == "__main__":
    password_vaild_check("23jke")
    password_vaild_check("432rewvb53")
    password_vaild_check("2@3jke%")
    password_vaild_check("3k39Qle6o0")