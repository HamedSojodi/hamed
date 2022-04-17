from bucket import bucket
from celery import shared_task


def all_objects_tasks():
    result = bucket.get_objects()
    return result


@shared_task
def delete_obj_bucket_task(key):
    bucket.delete_object(key)


@shared_task
def download_obj_bucket_task(key):
    bucket.download_object(key)
