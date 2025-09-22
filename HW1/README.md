# 네이버 뉴스 자동 메일러 (Naver News Auto Mailer)

`news_mailer.py`는 네이버 뉴스의 IT/과학 섹션에서 가장 많이 본 뉴스 상위 10개를 스크래핑하여, 지정된 이메일로 매일 아침 8시에 자동으로 발송하는 Python CLI 애플리케이션입니다.

### 사전 준비 (Prerequisites)

스크립트를 실행하기 전에 필요한 Python 라이브러리를 설치해야 합니다.

```bash
pip install requests beautifulsoup4 schedule
```

### 실행 방법 (How to Run)

아래 명령어를 터미널(명령 프롬프트)에 입력하여 스크립트를 실행합니다.

```bash
python "C:\Users\이지수\OneDrive\바탕 화면\HW01\deeplearning\HW1\news_mailer.py" --sender-email "보내는_이메일@gmail.com" --receiver-email "받는_이메일@example.com" --password "앱_비밀번호"
```

#### 인자 설명 (Argument Description)

- `--sender-email`: 발신자(보내는 사람)의 이메일 주소입니다.
- `--receiver-email`: 수신자(받는 사람)의 이메일 주소입니다.
- `--password`: 발신자 이메일 계정의 비밀번호입니다.

### 동작 방식 (How it Works)

1. 스크립트를 실행하면, 먼저 테스트를 위해 즉시 한 번 뉴스 스크래핑 및 이메일 발송을 수행합니다.
2. 이후 스케줄러가 동작하며, 매일 아침 8시에 자동으로 작업을 반복합니다.
3. 자동 실행을 유지하려면 스크립트가 실행 중인 터미널 창을 닫지 않아야 합니다.
```