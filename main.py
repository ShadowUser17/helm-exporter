import os
import sys
import json
import gzip
import base64
import logging
import traceback

from kubernetes import config as k8s_config
from kubernetes import client as k8s_client

from prometheus_client import Gauge
from prometheus_client import Counter
from prometheus_client import CollectorRegistry
from prometheus_client.exposition import generate_latest


try:
    log_level = logging.DEBUG if os.environ.get("DEBUG_MODE", "") else logging.INFO
    logging.basicConfig(
        format=r'%(levelname)s [%(asctime)s]: "%(message)s"',
        datefmt=r'%Y-%m-%d %H:%M:%S', level=log_level
    )

except Exception:
    logging.error(traceback.format_exc())
    sys.exit(1)
