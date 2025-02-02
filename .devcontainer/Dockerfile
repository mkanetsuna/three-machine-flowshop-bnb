# Python公式イメージをベースに使用
FROM python:3.13-slim-bullseye

# 必要パッケージインストール
RUN apt-get update && apt-get install -y \
    git \
    curl \
    make \
    unzip \
    build-essential \
    libssl-dev \
    libffi-dev \
    jq \
    libc6 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの設定
WORKDIR /workspace

# ホスト側のファイルをコンテナにコピー
COPY . /workspace

# 必要なパッケージをインストール
RUN pip install --upgrade pip && pip install -r requirements.txt

# コンテナ起動時のデフォルトコマンド
#CMD ["python", "src/entrypoint/main.py"]
