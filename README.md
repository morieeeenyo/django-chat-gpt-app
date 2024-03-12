# diango-chatgpt-app
以下の目的で作ったアプリ

- OpenAIのAPIの学習
- OpenAIのAPIを使うアプリを作る際のバックエンドの雛形

# 技術スタック
- Django

# 環境構築手順
リポジトリクローン後、以下の手順に従ってください
1. python3およびpip3のインストール
- ※開発時はpython 3.11系をhomebrew経由でインストールして開発しました
- 使用しているライブラリの関係でpython3.10以上じゃないと動作しません
- ※python2系以下での動作は保証できません

```
python3 -V
```
で使用しているpythonのバージョンを確認してください。


2. 仮想環境の有効化
以下のコマンドを実行して仮想環境に入ります

```
source bin/activate
```

3. 必要なパッケージのインストール
以下のコマンドを実行してください。

```
 pip3 install -r requirements.txt
```

4. DBの作成
ローカルに以下のDBを作成してください(mysqlコマンド、GUIツールなど方法は自由)
django_chat_gpt_app_development
DBの名前は`config/settings.py` に記載しているので、もしローカルのDB名と重複する場合は自由に変更いただいて構いません

5. マイグレーションの実行
以下のコマンドを実行してマイグレーションを実行してください。

```
python3 manage.py migrate
```

6. サーバーの起動
以下のコマンドを実行してサーバーを起動してください。

```
python3 manage.py runserver
```

# エンドポイント
以下のエンドポイントが使えます。

- POST /api/messages


