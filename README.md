# SDXXUpdater-API

このプロジェクトは、ゲームプログラムが最新のアップデート情報を取得し、アップデートが必要かどうかを判断するためのAPIを提供します。

## 機能

- クライアントからのリクエストを受け取り、ゲームタイトルと現在のバージョン情報を基にアップデートが必要かどうかを判断します。
- アップデートが必要な場合、最新バージョン情報とアップデートファイルのURLを返します。
- アップデートが不要な場合、その旨を応答します。
- 複数のゲームタイトルとそれぞれの最新バージョン情報を管理します。

## 使用方法

### 必要要件

- Python 3.x
- Flask

### インストール

Flaskをインストールします：

```sh
pip install flask
```

### 設定

`updates.json`ファイルをプロジェクトのルートディレクトリに作成し、以下のような内容で設定します：

```json
{
    "games": {
        "game1": {
            "latest_version": "1.2.3",
            "update_url": "https://example.com/game1/update.zip"
        },
        "game2": {
            "latest_version": "2.3.4",
            "update_url": "https://example.com/game2/update.zip"
        }
    }
}
```

### 実行

以下のコマンドでFlaskサーバーを起動します：

```sh
python api-srv.py
```

### APIエンドポイント

#### チェックアップデート

- **URL**: `/check_update`
- **メソッド**: `POST`
- **リクエストボディ**:
    ```json
    {
        "game_title": "game1",
        "current_version": "1.0.0"
    }
    ```

- **レスポンス例**（アップデートが必要な場合）:
    ```json
    {
        "latest_version": "1.2.3",
        "update_url": "https://example.com/game1/update.zip"
    }
    ```

- **レスポンス例**（アップデートが不要な場合）:
    ```json
    {
        "message": "No update needed"
    }
    ```

- **エラーレスポンス例**（リクエストが不正な場合）:
    ```json
    {
        "error": "game_title and current_version are required"
    }
    ```

- **エラーレスポンス例**（ゲームが見つからない場合）:
    ```json
    {
        "error": "Game not found"
    }
    ```

## ライセンス

このプロジェクトはApache License 2.0の下でライセンスされています。詳細は[LICENSE](./LICENSE)ファイルを参照してください。
