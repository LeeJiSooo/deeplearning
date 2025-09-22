import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def send_email(headlines, sender_email, receiver_email, password, smtp_server, smtp_port):
    """
    스크래핑한 뉴스 헤드라인과 링크를 HTML 형식으로 이메일 발송합니다.
    """
    if not headlines:
        print("발송할 뉴스 헤드라인이 없습니다. 이메일을 보내지 않습니다.")
        return

    today_str = datetime.now().strftime('%Y년 %m월 %d일')
    subject = f"[{today_str}] 네이버 IT/과학 뉴스 TOP 10"
    
    body = f"<h2>{today_str} 가장 많이 본 IT/과학 뉴스</h2>"
    body += "<ol>"
    for news in headlines:
        body += f"<li><a href='{news['link']}' target='_blank'>{news['title']}</a></li>"
    body += "</ol>"
    body += "<hr>"
    body += "<p><em>* 이 메일은 Python 자동화 스크립트를 통해 발송되었습니다.</em></p>"

    msg = MIMEText(body, 'html', 'utf-8')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print(f"성공: 이메일이 {receiver_email} 주소로 성공적으로 발송되었습니다.")
    except smtplib.SMTPAuthenticationError:
        print("오류: SMTP 인증에 실패했습니다. 이메일 주소와 비밀번호(앱 비밀번호)를 확인하세요.")
    except Exception as e:
        print(f"오류: 이메일 발송 중 예외가 발생했습니다: {e}")
