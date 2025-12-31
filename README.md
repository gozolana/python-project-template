# python project template

## 概要

このREADMEは、vscodeのdevcontainer上での開発を想定したPythonプロジェクトのテンプレートに関する情報を提供します。

## 前提

devcontainer拡張機能が有効化されたvscode

## 使い方

### 新規リポジトリ作成

- github でリポジトリを作成する際、本テンプレートを選択する
- ローカル環境へ git clone し、vscode で開く
- devcontainer で開き直すが聞かれるので Yes を選択。または Dev Containers: Reopen in Container を実行する

### プロジェクト名を変更する

- `Ctrl+Shift+H` で全置換メニューを開き、「my_project」を任意のプロジェクト名に全置換する
- src/my_project のディレクトリ名も合わせて置換する

### 基本的な使い方

```
uv run task
```

### 機能の追加

```
uv add <パッケージ名>
または
uv add --dev <開発パッケージ名>
```

## 実行

### イメージ作成
以下の手順で、Dockerイメージを作成します。
```bash
docker image build -t my_project .
```
### コンテナ実行

以下の手順で、Dockerコンテナを起動します。
```bash
docker run my_project
```
