import schedule
import time
import argparse
from datetime import datetime

# 분리된 모듈에서 함수 임포트
from scraper import scrape_naver_news
from mailer import send_email

def job(args):
    """
    뉴스 스크래핑 및 이메일 발송 작업을 수행하는 메인 함수
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 작업을 시작합니다...")
    headlines = scrape_naver_news()
    
    if headlines:
        print(f"성공: {len(headlines)}개의 뉴스 헤드라인을 가져왔습니다. 이메일 발송을 시작합니다.")
        send_email(
            headlines,
            args.sender_email,
            args.receiver_email,
            args.password,
            args.smtp_server,
            args.smtp_port
        )
    else:
        print("뉴스 스크래핑에 실패하여 이메일을 발송하지 않습니다.")

def main():
    """
    CLI 인자를 파싱하고, 스케줄러를 설정 및 실행합니다.
    """
    parser = argparse.ArgumentParser(
        description="네이버 뉴스 IT/과학 섹션의 헤드라인을 스크래핑하여 이메일로 전송하는 CLI 도구",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument('--sender-email', type=str, required=True, help='발신자 이메일 주소 (Gmail 권장)')
    parser.add_argument('--receiver-email', type=str, required=True, help='수신자 이메일 주소')
    parser.add_argument('--password', type=str, required=True, help="발신자 이메일 계정의 비밀번호.\nGmail의 경우 보안을 위해 '앱 비밀번호'를 사용해야 합니다.")

    parser.add_argument('--smtp-server', type=str, default='smtp.gmail.com', help='SMTP 서버 주소 (기본값: smtp.gmail.com)')
    parser.add_argument('--smtp-port', type=int, default=587, help='SMTP 서버 포트 (기본값: 587)')

    args = parser.parse_args()

    print("="*60)
    print("네이버 뉴스 자동 메일러가 시작되었습니다.")
    print(f"발신자: {args.sender_email}")
    print(f"수신자: {args.receiver_email}")
    print(f"매일 아침 8시에 뉴스 헤드라인을 발송합니다.")
    print("="*60)
    
    print("\n[초기 실행] 지금 바로 뉴스 스크래핑 및 이메일 발송을 시도합니다...")
    job(args)

    schedule.every().day.at("08:00").do(job, args=args)
    
    print("\n[스케줄러 시작] 다음 작업은 내일 아침 8시 정각에 실행됩니다.")
    print("이 창을 닫으면 자동 발송이 중단됩니다. (종료하려면 Ctrl+C를 누르세요)")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()