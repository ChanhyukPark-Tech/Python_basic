# number
# 901201-1111111

# email
# nadocoding@gmail.com

# car
# 11A 1234
# 123A 1234

# IP address

# 192.168.0.1

import re
# abcd , book ,desk <=== car number
# ca?e 
# care cafe case cave....everything
# caae , cabe  , cace , cade , ..


p = re.compile("ca.e") # . : 하나의 문자를 의미 > care, cafe , case | caffe < 안됌
                       # ^ (^de): 문자열의 시작 de 로 시작하는것은 모두 매칭가능 desk destination  fade(de로시작은아니기떄문에 매칭x)
                       # $ (se$) : 문자열의 끝 > case , base < matching ok face(x)




def print_match(m):
#m = p.match("cafe")
# print(m.group())        # 매치되지 않으면 에러 발생 caffe 면 에러발생 case면 에러 x
    if m:
        print("m.group(): ",  m.group())        #일치하는 문자열
        print("m.string :" , m.string) #입력받은 문자열 careless 받았으면 careless 가찍힌다
        print("m.start() : " , m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : " , m.end()) #일치하는 문자열의 끝 index
        print("m.span() : ", m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print("Matching fail")


# m = p.match("care")     # match의 동작이 주어진 문자열의 처음부터 일치하는지 확인 처음부터 이어나가면서 확인 ,,, careless < match
# print_match(m)          # 뒷부분 다른거 있어도 상관 x 

m = p.search("good care")   # search : 주어진 문자열 중에 일치하는게 있는지확인 .. MATCH 는 처음부터 확인! SEARCH 는 주어진문자열!
print_match(m)

lst = p.findall("careless") # findall 일치하는 모든것을 리스트 형태로 반환
print(lst)