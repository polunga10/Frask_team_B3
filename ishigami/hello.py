from flask import Flask, render_template_string

app = Flask(__name__)

# HTMLテンプレートを文字列として定義
html_template = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>自己紹介</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        p, li {
            color: #666;
        }
        .bio {
            background-color: #e7e7e7;
            padding: 10px;
            margin-bottom: 20px;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            background-color: #e7e7e7;
            margin-bottom: 10px;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>自己紹介</h1>
        <div class="bio">
            <p>名前: {{ name }}</p>
            <p>自己紹介: {{ bio }}</p>
        </div>
        <h2>プロジェクト:</h2>
        <ul>
            {% for project in projects %}
            <li>{{ project }}</li>
            {% endfor %}
        </ul>
        <h2>趣味:</h2>
        <ul>
            {% for hobby in hobbies %}
            <li>{{ hobby }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # 自己紹介の情報を辞書で定義
    personal_info = {
        "name": "山田太郎",
        "bio": "Web開発者で、PythonとFlaskが得意です。",
        "projects": ["プロジェクト1", "プロジェクト2", "プロジェクト3"],
        "hobbies": ["読書", "ギター", "ランニング"]
    }
    # render_template_stringを使用してHTMLテンプレートをレンダリング
    return render_template_string(html_template, **personal_info)

if __name__ == '__main__':
    app.run(debug=True)
