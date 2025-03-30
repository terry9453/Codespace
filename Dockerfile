WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

* `FROM python:3.9-slim`：使用 Python 3.9 的精簡映像作為基礎映像。
* `WORKDIR /app`：設定工作目錄為 `/app`。
* `COPY requirements.txt .`：將 `requirements.txt` 檔案複製到工作目錄。
* `RUN pip install --no-cache-dir -r requirements.txt`：安裝 `requirements.txt` 中列出的相依性。
* `COPY . .`：將專案中的所有檔案複製到工作目錄。
* `CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]`：設定容器啟動時執行的命令。
