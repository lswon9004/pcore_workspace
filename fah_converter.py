def covert_c_to_f(celcius_value):
    return celcius_value * 9.0 / 5 + 32
# 다른 문서에서 모듈로서 실행되는 것이 아니라
# 현재 문서가 main으로 실행될 때만 수행
if __name__ == '__main__':
    print(covert_c_to_f(10))