from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 139.58,
    "uptime_pct": 98.843,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 102.69,
    "uptime_pct": 98.431,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 107.44,
    "uptime_pct": 98.503,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 183.23,
    "uptime_pct": 97.124,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 227.56,
    "uptime_pct": 98.635,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 145.47,
    "uptime_pct": 99.432,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 174.45,
    "uptime_pct": 98.109,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 138.46,
    "uptime_pct": 97.969,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 229.54,
    "uptime_pct": 99.059,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 135.65,
    "uptime_pct": 99.43,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 195.41,
    "uptime_pct": 98.037,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 225.49,
    "uptime_pct": 99.089,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 162.62,
    "uptime_pct": 98.494,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 150.66,
    "uptime_pct": 98.275,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 191.73,
    "uptime_pct": 99.174,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 213.4,
    "uptime_pct": 97.282,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 115.94,
    "uptime_pct": 98.58,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 206.23,
    "uptime_pct": 97.815,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 140.31,
    "uptime_pct": 98.416,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 129.31,
    "uptime_pct": 97.824,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 231.79,
    "uptime_pct": 97.81,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 217.82,
    "uptime_pct": 99.104,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 204.9,
    "uptime_pct": 97.944,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 206.24,
    "uptime_pct": 99.418,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 203.15,
    "uptime_pct": 99.267,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 173.66,
    "uptime_pct": 97.257,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 224.45,
    "uptime_pct": 98.194,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 189.12,
    "uptime_pct": 99.18,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 172.58,
    "uptime_pct": 98.754,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 152.82,
    "uptime_pct": 97.975,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 211.58,
    "uptime_pct": 97.471,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 154.8,
    "uptime_pct": 98.602,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 215.42,
    "uptime_pct": 98.063,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 151.09,
    "uptime_pct": 99.489,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 117.69,
    "uptime_pct": 98.31,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 147.78,
    "uptime_pct": 98.552,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
