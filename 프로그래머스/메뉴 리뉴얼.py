#- _ .
#.은 처음과 끝 그리고 연속 불가
#3자이상 15자 이하
import re


def solution(new_id):
    #1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    print(1,new_id)
    #2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    pattern = re.compile("[a-z0-9-_.]")
    new_id="".join(pattern.findall(new_id))
    print(2,new_id)
    #3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    stack = new_id[0]
    for i in range(1, len(new_id)):
        if new_id[i] == "." and stack[-1]==".":
            continue
        stack += new_id[i]
    new_id = stack
    print(3,new_id)
    #4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    new_id = new_id[:-1] if len(new_id)>0 and new_id[-1]=="." else new_id
    new_id = new_id[1:] if len(new_id)>0 and new_id[0]=="." else new_id
    print(4,new_id)
    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    new_id = "a" if new_id=="" else new_id
    print(5,new_id)
    #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #    만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    new_id = new_id[:15] if len(new_id)>=16 else new_id
    new_id = new_id[:-1] if new_id[-1]=="." else new_id
    print(6,new_id)
    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(new_id)<3:
        new_id += new_id[-1]
    print(7,new_id)
    return new_id
    

print("final:", solution("...!@BaT#*..y.abcdefghijklm"))
print("final:", solution("z-+.^."))
print("final:", solution("=.="))
print("final:", solution("123_.def"))
print("final:", solution("abcdefghijklmn.p"))