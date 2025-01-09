# 블록리스트 관리 파일

BLOCKLIST = set()
# 추가
def add_to_blocklist(jti):
    BLOCKLIST.add(jti)
# 삭제
def remove_from_blocklist(jti):
    BLOCKLIST.discard(jti)