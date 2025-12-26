
from fastapi import FastAPI, Query, HTTPException
import boto3
import os
from boto3.dynamodb.conditions import Key

# Environment variables for configuration
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
TABLE_NAME = os.getenv("DDB_TABLE_NAME", "ddb-item-table")
PK_NAME = os.getenv("DDB_PARTITION_KEY", "id")

if not TABLE_NAME or not PK_NAME:
    raise RuntimeError("Please set DDB_TABLE_NAME and DDB_PARTITION_KEY environment variables.")

# Initialize DynamoDB resource
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(TABLE_NAME)

app = FastAPI(title="Simple DynamoDB Reader")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/items")
def get_items(pk: str = Query(..., description="Partition key value")):
    try:
        response = table.query(
            KeyConditionExpression=Key(PK_NAME).eq(pk)
        )
        items = response.get("Items", [])
        return {"count": len(items), "items": items}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/items/all")
def get_all_items(limit: int = Query(100, ge=1, le=1000, description="Max items to return")):
    """Get all records (scan) - use limit for testing"""
    try:
        response = table.scan(Limit=limit)
        items = response.get("Items", [])
        return {"count": len(items), "items": items}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
