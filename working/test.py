def 대본(f):
    def wrapper(*args, **kwargs):
        print("대본 가져오기 완료")
        result = f(*args, **kwargs)
        print("대본 표시하기 완료")
        return result

    return wrapper
    
@대본
def 보여주기():
    print("대본을 보여준다")
    
    
# 보기 = 대본(보여주기)
# 보기()

보여주기()