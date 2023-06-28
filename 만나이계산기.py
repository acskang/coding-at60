## 만나이 계산기
from datetime import datetime

생년월일 = "2023-6-27"
생년월일_구조 = datetime.strptime(생년월일, '%Y-%m-%d').date()
오늘날짜_구조 = datetime.now().date()
년수 = 오늘날짜_구조.year - 생년월일_구조.year


def 월일비교함수(생년월일_구조, 오늘날짜_구조):
    def 일비교함수():
        # 오늘 날짜가 태어난 날짜보다 작으면
        if 오늘날짜_구조.day < 생년월일_구조.day:
            return 0
        # 오늘 날짜가 태어난 날짜보다 같거나 크면
        return 1
    
    def 월비교함수():
        # 오늘 월이 태어난 월보다 작은 경우
        if 오늘날짜_구조.month < 생년월일_구조.month:
            return 0
        # 오늘 월이 태어난 월보다 큰 경우
        elif 오늘날짜_구조.month > 생년월일_구조.month:
            return 1
        return 일비교함수()
    return 월비교함수()

만나이 = 년수 + 월일비교함수(생년월일_구조, 오늘날짜_구조)
print(만나이)