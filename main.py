from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# 設定資料存放目錄（改成專案內的 data 資料夾，避免權限問題）
DATA_DIR = "./data"
os.makedirs(DATA_DIR, exist_ok=True)  # 確保資料夾存在

# 根路由，當用戶訪問根目錄時顯示歡迎訊息
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Server!"}

# 定義 User 資料模型
class User(BaseModel):
    user_id: str
    name: str
    age: int
    email: str

# 1️⃣ POST: 儲存使用者資料
@app.post("/user/add")
async def add_user(user: User):
    file_path = os.path.join(DATA_DIR, f"{user.user_id}.json")

    # 檢查檔案是否已存在
    if os.path.exists(file_path):
        raise HTTPException(status_code=400, detail="使用者 ID 已存在")

    # 儲存資料
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(user.dict(), f, indent=4)

    return {"message": "使用者已成功儲存", "user_id": user.user_id}

# 2️⃣ GET: 取得所有使用者列表
@app.get("/users")
async def list_users():
    try:
        users = [f.replace(".json", "") for f in os.listdir(DATA_DIR) if f.endswith(".json")]
        return {"users": users}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"讀取使用者列表時發生錯誤: {str(e)}")

# 3️⃣ GET: 取得指定使用者資訊
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    file_path = os.path.join(DATA_DIR, f"{user_id}.json")

    # 檢查檔案是否存在
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="使用者不存在")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            user_data = json.load(f)
        return user_data
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="使用者資料檔案格式錯誤")

