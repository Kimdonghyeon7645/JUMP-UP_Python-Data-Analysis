'''
[문제]가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,
     다음과 같은 결과를 출력하는 프로그램을 작성하십시오
     조건1) 함수의 이름은 maxCheck(*param)로 정의 하고
           호출함수는 maxCheck(3, 5, 4, 1, 8, 10, 2)를 이용하시오
     조건2) maxCheck()함수에서 람다식으로 프로그램을 완성하시오


[출력화면]
max(3, 5, 4, 1, 8, 10, 2) => 10
'''
# 문제 이상


def maxCheck(*param):
    print(f'max({param}) => {max(param)}')


maxCheck(3, 5, 4, 1, 8, 10, 2)
