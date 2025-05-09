#!/usr/bin/env python
# test_profile.py
import asyncio
from server import get_profile, mcp

async def main():
    try:
        print("Fetching user profile...")
        profile = await get_profile()
        print("Profile retrieved successfully:")
        print(profile)
    except Exception as e:
        print(f"Error fetching profile: {e}")

if __name__ == "__main__":
    asyncio.run(main())
