# FNZ_ATOM – AI Business Design Backend

This project is a FastAPI-based backend that generates business designs, schemas, and SQL using AI.

---

## 1. Create Virtual Environment

From the project root directory, run:

### Windows

    python -m venv venv
    venv\Scripts\activate

### macOS / Linux

    python3 -m venv venv
    source venv/bin/activate

After activation, you should see:

    (venv)

in your terminal.

---

## 2. Setup Environment Variables

This project uses environment variables for API keys.

A template file is provided:

    .env.test

### Step 1: Create .env File

Copy `.env.test` and create a new file called `.env`:

    copy .env.test .env        (Windows)
    cp .env.test .env          (macOS/Linux)

### Step 2: Add Your API Key

Open `.env` and update the values.

Example:

    GEMINI_API_KEY=your_api_key_here

Make sure the file is saved.

---

## 3. Install Dependencies

Install all required packages using:

    pip install -r requirements.txt

Wait until installation completes.

---

## 4. Run the Server

From the project root, start the FastAPI server:

    python -m uvicorn app.main:app --reload

If successful, you will see:

    Uvicorn running on http://127.0.0.1:8000

---

## 5. Test Using Postman (WebSocket)

This project uses WebSocket for chat communication.

### WebSocket Endpoint

    ws://127.0.0.1:8000/ws/chat

---

### Using Postman

1. Open Postman
2. Click **New**
3. Select **WebSocket Request**
4. Enter the URL:

       ws://127.0.0.1:8000/ws/chat

5. Click **Connect**
6. Send messages in JSON or text format

Example:

    {
      "message": "Design a complaint tracking system"
    }

---

## 6. API Documentation (Optional)

FastAPI provides automatic API documentation.

After starting the server, open:

    http://127.0.0.1:8000/docs

---

## Project Structure (Simplified)

    FNZ_ATOM/
    ├── app/
    │   ├── main.py
    │   ├── api/
    │   └── services/
    ├── venv/
    ├── .env
    ├── .env.test
    ├── requirements.txt
    └── README.md

---

## Notes

- Always activate the virtual environment before running the server
- Never commit `.env` files to public repositories
- Update `requirements.txt` when new packages are added

---

## Quick Start Summary

    python -m venv venv
    venv\Scripts\activate
    copy .env.test .env
    pip install -r requirements.txt
    python -m uvicorn app.main:app --reload

Then connect using Postman:

    ws://127.0.0.1:8000/ws/chat
