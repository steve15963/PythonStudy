def docFun(f=0.0, i=1, s="abcd"):
    """
테스트 문자열이지만 
\"\"\"을 이용하여 다중 행으로 작성되었습니다.
    Keyword arguments:
    f -- float (default 0.0)
    i -- int
    s -- string
    """

#아무것도 출력하지 않습니다.
print("호출시 아무것도 출력하지 않습니다.")
docFun()
print("=" * 20)

# 문서설명 출력
print("문서 출력")
print(docFun.__doc__)

