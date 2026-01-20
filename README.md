# pre-learning-2026
IoT개발자 과정 사전학습 리포지토리

## 1일 차
과정소개


학습 리포지토리 생성

- 마크다운 학습
  1. 제목
      ```markdown
      #  제목1
      ##  제목2
      ###  제목3
      ####  제목4
      #####  제목5
      ######  제목6 (잘 사용 안함)
      <!-- 주석(HTML주석 동일) -->
      ```

  2. 목록
      ```markdown
      - 목록
      * 목록
      1.  숫자목록
      2.  숫자목록
      ```
  3. 링크, 이미지
     ```markdown
     [네이버](https://naver.com)

     ![이미지](이미지URL)

     ## 사이즈 조절 이미지
     src : 이미지URL
     width : 이미지넓이 픽셀단위 지정
     <img src="이미지URL" width="500">
     ```
     - [네이버](https://naver.com)
    
     - ![이미지](https://i.namu.wiki/i/d1A_wD4kuLHmOOFqJdVlOXVt1TWA9NfNt_HA0CS0Y_N0zayUAX8olMuv7odG2FiDLDQZIRBqbPQwBSArXfEJlQ.webp)
       
     - <img src="https://i.namu.wiki/i/d1A_wD4kuLHmOOFqJdVlOXVt1TWA9NfNt_HA0CS0Y_N0zayUAX8olMuv7odG2FiDLDQZIRBqbPQwBSArXfEJlQ.webp" width="500">
     - 이미지와 링크의 차이는 !로 시작하는지 밖에 없음
     
     - <img width="1000" height="667" alt="image" src="https://github.com/user-attachments/assets/a6ad3a70-2e44-4d5f-b90a-12f152136199" />

  4. 가로줄
     ```markdown
     ---
     ```
  ---
  5. 코드블럭
     - 소스코드를 작성할 때 코드하이라이팅, 영역표시 때 사용
     - 백틱(`)을 세번 후 표시언어를 입력 또는 한번(인라인 코드블럭)
     ```python
     print('hello,python!')
     ```
     - 일반적인 문장에서 한 단어를 강조하고 싶을 때 `인라인 코드블럭`을 사용

  6. 강조 및 밑줄
     ```markdown
     *,~,_html u 태그사용, i 이탤릭
     ```
     - 문장을 작성할 시 **강조**, ~~취소선~~, __강조2__, <u>밑줄</u>, <i>이탤릭</i> 을 사용할 수 있습니다.
       

  - 깃허브 로컬리포지토리 생성
    1. git for window 설치
       - https://git-scm.com/ 에서 `install for window` 버튼 클릭
       - git for windows/x64 setup 클릭
       - git 설치 옵션 기본 그대로 사용 가능 ( 변경하지 말 것)
       - cmd 또는 powershell 에서 `git --version`,`git -v` 확인
    3. Github Desktop 설치
       - https://desktop.github.com/download/ 에서 다운로드 클릭, 설치
       - 계정 브라우저 연동
    4. 리포지토리 클론
       -  github desktop 메뉴 clone repository 클릭
       -  gitgub.com 탭에서 저장소 검색, 선택
       -  Local Path 지정 후 클론 버튼 클릭
      
- Visual Studio Code 설치
  1. https://code.visualstudio.com/docs/?dv=win64user 다운로드 클릭
  2. 설치 `C:\DEV\IDE\Microsoft VS Code`에 설치
  3. Extensions > Korean Pack for Visual Studio Code 설치 후 재시작

- 추가 설치 프로그램
  1. Notepad++ 에디터 - https://notepad-plus-plus.org/downloads/
  2. 픽픽 - https://picpick.net/
 
- **파이썬** 개발환경 설정
  1. https://www.python.org/ 에서 Download의 python 3.1x.x 버튼 클릭
  2. Add python.exe to PATH 체크 활성화 후 
  3. Installer > Customize installation 클릭
  4. Documentation 체크 해제, for all users 체크 활성화
  5. advanced options 에서 install python 3.1x for all users 체크
  6. 경로 변경 후 설치
     <img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/58658e01-e204-43fb-b08d-a2eb29fe774e" />
     
  7. setup was successful 에서 disable path length limit 클릭(필수)
     <img width="656" height="415" alt="image" src="https://github.com/user-attachments/assets/ca23c2a1-f417-4ce4-80d5-8f129c7831a7" />
  8. cmd 또는 powershell 오픈, `python --version` 실행
  9. VS Code,Exension에서 python을 검색, 설치
- 프로그램 개발 개념
