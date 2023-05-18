import requests

url = 'http://hocalhost:5000/data'  # Flask 애플리케이션의 엔드포인트 URL
data = {'key': 'value'}  # 전송할 데이터

response = requests.post(url, json=data)  # POST 요청 보내기
print(response.text)  # 응답 출력