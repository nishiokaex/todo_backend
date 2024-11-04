
## インストール

1. 仮想環境の作成と有効化

	```bash
	python -m venv venv
	source venv/bin/activate
	```

2. 依存パッケージのインストール

	```bash
	pip install -r requirements.txt  
	pip install fastapi-cli
	```

## ローカル実行

1. FastAPI サーバの開始

```fastapi dev app/main.py```

2. ブラウザで下記にアクセス

```http://127.0.0.1:8000```
