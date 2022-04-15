from bucket import bucket


def all_objects_tasks():
    result = bucket.get_objects()
    return result

