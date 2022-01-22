from konlpy.tag import Okt

okt = Okt()
# result = okt.pos("이런 것도 분석으로 해주낰ㅋㅋㅋㅋ ")
result = okt.nouns("아무 문장이나 넣어보세요 ㅎㅎ")
print(result)