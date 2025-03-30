from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

class UserData(BaseModel):
    user_id: int
    username: str
    email: str
    # 其他您需要儲存的資料欄位

@app.post("/user/add/")
async def save_data(data: UserData):
    try:
        # 將資料轉換為 JSON 格式 
        data_json = data.dict()

        # 設定儲存檔案的路徑和名稱
        filename = f"user_{data.user_id}.json"
        filepath = os.path.join("data", filename) # 將檔案儲存到 "data" 資料夾中

        # 檢查資料夾是否存在，如果不存在則建立
        if not os.path.exists("data"):
            os.makedirs("data")

        # 將資料儲存到檔案中
        with open(filepath, "w") as f:
            json.dump(data_json, f)

        return {"message": f"Data saved to {filename}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
