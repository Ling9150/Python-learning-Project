# AI Dependency Security Scanner

小規模チーム向けのAI支援型 依存関係セキュリティスキャナー。依存関係ファイルを読み込み、OSV脆弱性データベースに問い合わせ、結果をローカルにキャッシュして、分かりやすいリスク解説と修正提案を生成します。

## 機能
* Python依存関係ファイルの解析
* OSV脆弱性データベースへの問い合わせ
* SQLiteを使用した脆弱性結果のキャッシュ
* Richテーブルを用いたCLI上でのスキャン結果表示
* Markdownレポートの自動生成
* AIによる修正アドバイスの提供
* StreamlitによるWebインターフェースの提供
* DockerおよびGitHub Actions連携のサポート

## 技術スタック
* Python
* requests
* sqlite3
* Rich
* Streamlit
* OSV API
* SiliconFlow / OpenAI互換 API

## インストール

```bash
pip install -r requirements.txt
```

## APIキーの設定

AIアドバイス機能は、環境変数からAPIキーを読み込みます。

Windows PowerShell:
```powershell
$env:SILICONFLOW_API_KEY="your_api_key_here"
```

Windows CMD:
```cmd
set SILICONFLOW_API_KEY=your_api_key_here
```

macOS / Linux:
```bash
export SILICONFLOW_API_KEY="your_api_key_here"
```

※ APIキーが設定されていない場合、スキャナーはAIアドバイスの生成をスキップします。

## CLIでの使用方法

基本スキャン：
```bash
python scan.py -f test_files/sample_requirements.txt
```

カスタムレポートの生成：
```bash
python scan.py -f test_files/sample_requirements.txt --output report.md
```

スキャン時にAIアドバイスを無効化：
```bash
python scan.py -f test_files/sample_requirements.txt --ai-limit 0
```

## Streamlitでの使用方法

```bash
streamlit run app.py
```
起動後、requirements ファイルをアップロードして「Scan」をクリックしてください。

## Dockerでの使用方法

イメージのビルド：
```bash
docker build -t dep-security-scanner .
```

Streamlitアプリの実行：
```bash
docker run --rm -p 8501:8501 dep-security-scanner
```

CLIスキャンの実行：
```bash
docker run --rm dep-security-scanner python scan.py -f test_files/sample_requirements.txt --ai-limit 0
```

## レポート出力

スキャナーは以下の内容を含むMarkdownレポートを生成します：

* スキャン対象ファイル
* スキャン日時
* スキャンされた依存関係の数
* 脆弱性の概要
* 脆弱性の詳細
* 深刻度（Severity）
* AIによる修正アドバイス（有効な場合）

## プロジェクトの価値 

本プロジェクトは、小規模チームが本番環境で問題が発生する前に依存関係のセキュリティリスクを発見するのを支援します。OSVからの構造化された脆弱性データとAIによる解説を組み合わせることで、セキュリティ診断結果の理解と迅速な対策の実施を可能にします。