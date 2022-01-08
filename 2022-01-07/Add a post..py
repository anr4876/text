article1 = {"번호" : 1, "제목" : "소니의 축구교실", "내용" : "소니의 축구 강좌", "작성자" : "sony7"}
article2 = {"번호" : 2, "제목" : "류뚱의 야구교실", "내용" : "류뚱의 야구 강좌", "작성자" : "ryu99"}
article3 = {"번호" : 3, "제목" : "길동의 도술교술", "내용" : "길동의 도술 강좌", "작성자" : "hong123"}

article_list = [article1, article2, article3] # 게시물 저장소

user1 = {"아이디":"hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디":"sony7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디":"ryu99", "비밀번호" : "9999", "이름" : "류현진"}

user_list = [user1, user2, user3]

# 게시판 명령어 입력 : help

# add : 게시물 추가
# list : 게시물 목록 조회

# 게시판 명령어 입력 : list

# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실    작성자 : sony7
# 번호 : 2    제목 : 류뚱의 야구교실    작성자 : ryu99
# 번호 : 3    제목 : 길동의 도술교술    작성자 : hong123
# ================================= 

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : aaa
# 내용을 입력해주세요 : aaa

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : bbb
# 내용을 입력해주세요 : bbb

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : ccc
# 내용을 입력해주세요 : ccc

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : list

# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실
# 번호 : 2    제목 : 류뚱의 야구교실
# 번호 : 3    제목 : 길동의 도술교술
# 번호 : 4    제목 : aaa
# 번호 : 5    제목 : bbb
# 번호 : 6    제목 : ccc
# ================================= 

while True :

  cmd = input("게시판 명령어 입력 : ")

  if cmd == "help" :
    print("add : 게시물추가")
    print("list : 게시물 목록 조회")
    
  elif cmd == "list" :
    print("=============== 게시물 목록 ===============")
    for article in article_list :
      print("번호 : {}   제목 : {}    작성자 : {}".format(article["번호"], article["제목"], article["작성자"]))
    print("==========================================")

  elif cmd == "add" :
    title = input("제목을 입력해주세요 : ")
    body = input("내용을 입력해주세요 : ")
    
    article = {"번호" : 4, "제목" : title, "내용" : body, "작성자" : "익명"}
    article_list.append(article)

