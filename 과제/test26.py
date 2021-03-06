'''
[문제] toString()에 데이터를 전송한후, 결과를 튜플로 리턴 받아 온후 출력하시오
            조건1) 출력은 fommater를 이용해서 하시오
            조건2) 인원수는 함수를 이용해서 구하시오


[출력화면]
인원수 : 3명    총합: 220   평균: 73.33
'''


def toString(t) -> tuple:
    return len(t), sum(t), sum(t)/len(t)


re = toString((95, 55, 70))
print("인원수: {0:d}명  총합: {1:d}  평균: {2:.2f}".format(*re))

