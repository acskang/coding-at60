## 중첩함수; Nested Function, Recursive Function
def 아파트함수(*args, **kwargs):
    아파트 = kwargs.get("아파트")
    
    def 동함수(*args, **kwargs):
        동 = kwargs.get("동")
        
        def 호함수(*args, **kwargs):
            호 = kwargs.get("호")
            return f"{아파트} {동} {호}"
        
        return 호함수(*args, **kwargs)
    
    return 동함수(*args, **kwargs)


def 실행(*args):
    아파트 = 아파트함수
    data = {}
    data["아파트"] = args[0]
    data["동"] = args[1]
    data["호"] = args[2]
    return print(아파트(**data))


실행("텔레토비아파트", "329동", "5238호")