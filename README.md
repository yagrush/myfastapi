# myfastapi

FastAPIをDockerで実行するテンプレート一式です。
<br />
PythonとFastAPIを使ったRESTAPIサーバがすぐに試せます。

<br />

## 実行環境

Windows, Mac, Linux などに Docker + docker-composeとGitをインストールしてください。

--------

### Windows10

WSLでUbuntuなどのLinux仮想環境を作って、そこにDocker + docker-composeをインストールするのがおすすめです。

* マイクロソフト WSLの公式マニュアル https://docs.microsoft.com/ja-jp/windows/wsl/

* WSL2 Ubuntu 20.04 にDocker, docker-composeを入れる
https://qiita.com/yagrush/items/f12563eef6a1dd77cd4d

--------

### Mac

Docker Desktopなどをインストールしてください。

https://www.docker.com/

<br />

## FastAPI起動

### この一式を、Gitを使ってダウンロードします

```
git clone https://github.com/yagrush/myfastapi.git
```

### ディレクトリの中に入ります

```
cd myfastapi
```

### Dockerコンテナを起動しましょう


```
docker-compose up --build -d
```

## pytest実行


（編集中）