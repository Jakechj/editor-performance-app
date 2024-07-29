from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # 실제 데이터 대신 더미 데이터 사용
    data = {
        "notices": [
            {"date": "2024-07-01", "title": "7월 공지사항"},
            {"date": "2024-06-15", "title": "6월 중순 안내"}
        ],
        "editor_guides": [
            {"date": "2024-07-05", "title": "신규 에디터 가이드"},
            {"date": "2024-06-20", "title": "콘텐츠 작성 팁"}
        ],
        "sales": [
            {"date": "2024-07-01", "product": "상품A", "amount": 1000},
            {"date": "2024-07-02", "product": "상품B", "amount": 1500}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
