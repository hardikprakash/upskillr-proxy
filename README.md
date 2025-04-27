# Upskillr Proxy

A lightweight FastAPI-based proxy server that forwards API requests to a target endpoint with authentication.

## Overview

This proxy server acts as a middleware between clients and an API service. It:
- Verifies API tokens in incoming requests
- Forwards valid requests to the configured backend API
- Returns API responses back to the client

## Setup

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/hardikprakash/upskillr-proxy.git
cd upskillr-proxy
```

2. Install dependencies:
```bash
pip install fastapi uvicorn httpx python-dotenv
```

3. Configure environment variables:
Create a `.env` file in the project root with the following variables:
