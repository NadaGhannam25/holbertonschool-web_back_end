#!/usr/bin/env python3
"""Provides statistics about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats():
    """Print statistics about Nginx logs."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    logs = collection.count_documents({})
    print(f"{logs} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    log_stats()
