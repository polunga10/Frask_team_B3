from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # ここに自己紹介の情報を入力します
    personal_info = {
        "name": "山田太郎",
        "bio": "Web開発者で、PythonとFlaskが得意です。",
        "projects": ["プロジェクト1", "プロジェクト2", "プロジェクト3"],
        "hobbies": ["読書", "ギター", "ランニング"]
    }
    return render_template('index.html', info=personal_info)

if __name__ == '__main__':
    app.run(debug=True)

    
