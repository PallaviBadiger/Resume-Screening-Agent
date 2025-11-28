#!/usr/bin/env python
"""Test script to verify GROQ_API_KEY by making a simple API call."""
import os
from dotenv import load_dotenv
from groq import Groq

# Load .env if present
load_dotenv()

def test_groq_key():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("GROQ_API_KEY not set.")
        return False

    try:
        client = Groq(api_key=api_key)
        # Make a simple test call
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=10
        )
        print("GROQ_API_KEY is valid. Test call successful.")
        return True
    except Exception as e:
        print(f"GROQ_API_KEY is invalid: {e}")
        return False

if __name__ == "__main__":
    test_groq_key()
