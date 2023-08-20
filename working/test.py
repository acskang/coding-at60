#!/bin/sh python test.py
# from functools import wraps

# def 데코레이터(f):
#     @wraps(f)
#     def inner(*args, **kwargs):
#         return f(*args, **kwargs)
#     return inner

# @데코레이터
# def 매개변수확인(*args, **kwargs):
#     """특수 매개변수 확인용 함수"""
#     print(f"positional arguments are : {args}")
#     print(f"kekword arguments are : {kwargs}")
#     print(f"첫번째 매개변수 : {args[0]}")
#     print(f"두번째 매개변수 : {args[1]}")
#     print(f"세번째 매개변수 : {args[2]}")
#     print(f"이름 : {kwargs['이름']}")    
#     print(f"설명 : {kwargs['설명']}")
    
    
# if __name__ == "__main__":
#     매개변수확인('첫번째', 2, None, 이름="동해", 설명="한국의 동족바다")
#     print(f"함수이름 : {매개변수확인.__name__}")
#     print(f"함수설명 : {매개변수확인.__doc__}")


#
#
#
import pprint
def 복합기(f, m, c):
    def 프린트():
        f(f"{c}를 종이로 인쇄했습니다.")
    def 팩스():
        f(f"사이즈 {m(c)} 바이트의 {c}를 보냈습니다.")
    
    return 팩스() if m else 프린트()

stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']

pp = pprint.PrettyPrinter(indent=4)
복합기(pp.pprint, None, stuff)
복합기(print, len, "양평고속도로 관련 문서")