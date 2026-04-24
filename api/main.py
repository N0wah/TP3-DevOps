"""
API FastAPI hybride — MongoDB (posts) + MySQL (utilisateurs)
"""

import json
import os
from datetime import date, datetime

import mysql.connector
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://db_mongo:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client[os.getenv("MONGO_DB", "blog_db")]

MYSQL_CONFIG = {
    "host":     os.getenv("MYSQL_HOST", "db_mysql"),
    "port":     int(os.getenv("MYSQL_PORT", "3306")),
    "user":     os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE"),
}

class _DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def _jsonify(data):
    return json.loads(json.dumps(data, cls=_DateEncoder))


@app.get("/posts")
async def get_posts():
    cursor = db.posts.find({}, {"_id": 0})
    posts = await cursor.to_list(length=100)
    return JSONResponse(content=_jsonify({"source": "mongodb", "count": len(posts), "data": posts}))


@app.get("/users")
def get_users():
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM utilisateurs")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return JSONResponse(content=_jsonify({"source": "mysql", "count": len(users), "data": users}))


@app.get("/health")
async def health():
    errors = []

    try:
        count = await db.posts.count_documents({})
        if count == 0:
            errors.append("MongoDB: collection posts vide")
    except Exception as exc:
        errors.append(f"MongoDB: {exc}")

    try:
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM utilisateurs")
        (count,) = cursor.fetchone()
        cursor.close()
        conn.close()
        if count == 0:
            errors.append("MySQL: table utilisateurs vide")
    except Exception as exc:
        errors.append(f"MySQL: {exc}")

    if errors:
        raise HTTPException(status_code=503, detail={"status": "unhealthy", "errors": errors})

    return {"status": "ok", "databases": ["mongodb", "mysql"]}
