#!/usr/bin/env python3
"""
this module provides advanced stats about Nginx logs stored in MongoDB.
it calculates total logs, method counts, status checks, and the top 10 IPs.
"""
from pymongo import MongoClient


def log_stats():
    """
    calculates and prints statistics about the Nginx logs,
    including the top 10 most active IP addresses.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # total logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # status check
    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    # top 10 IPs (New Feature)
    print("IPs:")

    # the aggregation Pipeline
    pipeline = [
        # step A: group by IP and count occurrences
        {
            "$group": {
                "_id": "$ip",  # group by the 'ip' field
                "count": {"$sum": 1}  # add 1 for every document in the group
            }
        },
        # step B: Sort by count (Descending)
        {
            "$sort": {"count": -1}
        },
        # step C: Limit to top 10
        {
            "$limit": 10
        }
    ]

    # execute the pipeline
    top_ips = nginx_collection.aggregate(pipeline)

    # print the results
    for ip_data in top_ips:
        ip = ip_data["_id"]
        count = ip_data["count"]
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    log_stats()
