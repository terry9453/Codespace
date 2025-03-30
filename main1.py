from fastapi import FastAPI, HTTPException
import os
import json

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}


@app.get("/users")
async def get_users():
    try:
        users = []
        # 遍歷 "data" 資料夾中的所有檔案
        for filename in os.listdir("data"):
            # 檢查檔案是否為 user_id.json
            if filename.startswith("user_") and filename.endswith(".json"):
                # 讀取檔案內容
                with open(os.path.join("data", filename), "r") as f:
                    user_data = json.load(f)
                    users.append(user_data)
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
