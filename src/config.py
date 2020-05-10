import os

def get_config():
    return {
        'STATS_ENDPOINT': os.environ['STATS_ENDPOINT'] if 'STATS_ENDPOINT' in os.environ else None,
        'POLL_INTERVAL_SECONDS': os.environ['POLL_INTERVAL_SECONDS'] if 'POLL_INTERVAL_SECONDS' in os.environ else 30
    }
