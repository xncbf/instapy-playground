import os
# import sys

from instapy2 import InstaPy2
from instapy2.types import LikeType


# InstaPy 인스턴스 생성
session = InstaPy2()

# 세션 시작
session.login(username=os.getenv("USERNAME"), password=os.getenv("PASSWORD"))
# 액션 설정

tags = ['아티스트', '아트', '뮤지션', '래퍼', '프로듀서', '예술', '예술가', '아트디렉터', '디자이너', 'art', 'artist', 'musician', 'rapper', 'producer', '가수', '셀럽', '보컬']
session.like(amount=10, iterable=tags, type=LikeType.HASHTAG)
# session.follow_by_list(['tech_guru', 'code_master'])

# 세션 종료
# session.end()