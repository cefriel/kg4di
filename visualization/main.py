from fastapi import FastAPI, Request, HTTPException, Header
from fastapi.responses import HTMLResponse
from typing import List
import csv
import sys
import io
from io import StringIO
from urllib.parse import unquote_plus
import chardet

# Reconfigure stdout/stderr to UTF-8 so print() never raises
# UnicodeEncodeError on Windows consoles (e.g. cp1252 can't encode 'č').
for _s in ('stdout', 'stderr'):
    _stream = getattr(sys, _s)
    if hasattr(_stream, 'reconfigure'):
        _stream.reconfigure(encoding='utf-8', errors='replace')
    elif hasattr(_stream, 'buffer'):
        setattr(sys, _s, io.TextIOWrapper(_stream.buffer, encoding='utf-8', errors='replace'))

app = FastAPI(title="Map Visualization API")
csv_length_limit: int = 300

# Store locations in memory
locations: List[dict] = []


def decode_body(body: bytes) -> str:
    """
    Decode raw bytes to a string, trying UTF-8 (with BOM) first,
    then falling back to chardet auto-detection, then latin-1 as a
    last resort (latin-1 can decode any byte sequence without error).
    """
    # 1. Try UTF-8 / UTF-8-with-BOM
    try:
        return body.decode('utf-8-sig')
    except UnicodeDecodeError:
        pass

    # 2. Let chardet guess the encoding
    detected = chardet.detect(body)
    encoding = detected.get('encoding') or 'latin-1'
    confidence = detected.get('confidence', 0)
    print(f"[DEBUG] chardet detected encoding={encoding} confidence={confidence}")
    try:
        return body.decode(encoding)
    except (UnicodeDecodeError, LookupError):
        pass

    # 3. Final fallback – latin-1 never raises on any byte value
    print("[DEBUG] Falling back to latin-1 decoding")
    return body.decode('latin-1')


def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith('Bearer '):
        raise HTTPException(status_code=401, detail="Unauthorized: Bearer token required")
    token = authorization.split(' ', 1)[1]
    if token != 'tutorial-kg4di':
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid token")


@app.post("/api/location")
async def add_location(request: Request, authorization: str = Header(None)):
    verify_token(authorization)
    """
    Accept a CSV body with lat,lon,label format.
    Can contain multiple points to be added to the map.
    """
    body = await request.body()
    print(f"[DEBUG] Raw bytes (first 200): {body[:200]}")
    print(f"[DEBUG] Content-Type: {request.headers.get('content-type', 'not set')}")

    # Decode with automatic encoding detection (handles UTF-8, latin-1, etc.)
    csv_content = decode_body(body).strip()

    # If URL-encoded (commas appear as %2C), decode it
    if '%' in csv_content:
        csv_content = unquote_plus(csv_content)
        print(f"[DEBUG] URL-decoded content")

    csv_content = csv_content.replace('\r\n', '\n').replace('\r', '\n')
    print(f"[DEBUG] Received CSV data:\n{csv_content}")

    csv_reader = csv.DictReader(StringIO(csv_content), delimiter=',')
    # Force fieldnames to be read before logging
    _ = csv_reader.fieldnames
    print(f"[DEBUG] CSV headers: {csv_reader.fieldnames}")

    added_locations = []
    for row in csv_reader:
        if len(added_locations) >= csv_length_limit:
            print(f"[DEBUG] Reached {csv_length_limit}-row limit, stopping processing")
            break
        print(f"[DEBUG] Processing row: {dict(row)}")
        try:
            location_data = {
                "lat": float(row['lat']),
                "lon": float(row['lon']),
                "label": row.get('label', 'Selected Location').strip(),
                "type": row.get('type', '').strip(),
                "image": row.get('image', '').strip()
            }
            print(f"[DEBUG] Parsed location: {location_data}")
            locations.append(location_data)
            added_locations.append(location_data)
        except (ValueError, KeyError) as e:
            print(f"[DEBUG] Skipped row due to error: {e} | row={dict(row)}")
            continue

    return {
        "status": "success",
        "added_count": len(added_locations),
        "data": added_locations
    }


@app.get("/api/locations")
async def get_locations(authorization: str = Header(None), since: int = 0):
    verify_token(authorization)
    """
    Get stored locations, optionally starting from index `since`.
    Returns only the slice [since:] so the browser never re-fetches
    locations it already has.
    """
    slice_ = locations[since:]
    return {"total": len(locations), "locations": slice_}


@app.get("/", response_class=HTMLResponse)
async def read_root():
    """
    Serve the main HTML page with Leaflet map.
    """
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

