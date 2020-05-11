import os


def get_config():
    return {
        'LOCUST_URL': os.environ.get('LOCUST_URL', None),
        'POLL_INTERVAL_SECONDS': int(os.environ.get('POLL_INTERVAL_SECONDS', 30))
    }
