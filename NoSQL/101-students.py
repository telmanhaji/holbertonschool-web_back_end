#!/usr/bin/env python3
"""
this module defines a function that returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score.

    args:
        mongo_collection: the pymongo collection object.

    returns:
        list: a list of student dictionaries ordered by averageScore.
    """
    # the pipeline defines the sequence of operations.
    pipeline = [
        {
            "$project": {
                # it keeps the name field
                "name": "$name",
                # it keeps the original topics list
                "topics": "$topics",
                # it creates a new field 'averageScore'
                # $avg calculates the mean of the numeric values in the array
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            "$sort": {
                # sort by the newly created field in descending order (-1)
                "averageScore": -1
            }
        }
    ]

    # execute the aggregation and return the results as a list
    return list(mongo_collection.aggregate(pipeline))
