import os


def get_config():
    return {
        'STATS_ENDPOINT': os.environ.get('STATS_ENDPOINT', None),
        'POLL_INTERVAL_SECONDS':  os.environ.get('POLL_INTERVAL_SECONDS', 30)
    }
