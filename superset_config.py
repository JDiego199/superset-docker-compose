
import os
from datetime import timedelta
from typing import Optional
from cachelib.redis import RedisCache
from superset.superset_typing import CacheConfig
from cachelib.file import FileSystemCache
from datetime import timedelta

from celery.schedules import crontab
  #  from datetime import timedelta
 

    
SQLALCHEMY_DATABASE_URI = 'postgresql://admin:Passw0rd@127.0.0.1:5432/SupersetDB'

SECRET_KEY = 'soqGt/ST8hIl3JVW2glo82Oa7sQX0OF/5PQLNrfSeLRw1PlQKf+T2yGs'

MAPBOX_API_KEY ='pk.eyJ1IjoiZGllZ28xOTkiLCJhIjoiY2xoZG5jZTVpMG82ZjNvcHhzNWlmYm96NSJ9.Mc8DeBLmfN4gccO-zf76EA'	
FEATURE_FLAGS = {"ALERT_REPORTS": True,
		"DASHBOARD_CROSS_FILTERS":True,
		"HORIZONTAL_FILTER_BAR": True,
		"ENABLE_TEMPLATE_PROCESSING":True,
		"EMBEDDED_SUPERSET": True,
		"DASHBOARD_VIRTUALIZATION":True,
		"DRILL_TO_DETAIL": True,
		"EMBEDDABLE_CHARTS":True,
		}

SESSION_COOKIE_SAMESITE = None
GUEST_ROLE_NAME = "Gamma"
GUEST_TOKEN_JWT_SECRET = "test-guest-secret-change-me"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 5000 
WTF_CSRF_ENABLED = False
	
ENABLE_PROXY_FIX = True
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': ['*']
}

ALERT_REPORTS_NOTIFICATION_DRY_RUN = True

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 86400,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": '127.0.0.1',
    "CACHE_REDIS_PORT": '6379',
   # "CACHE_REDIS_DB": '1',
}
DATA_CACHE_CONFIG = CACHE_CONFIG

EXPLORE_FORM_DATA_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_explore_'
}
# filter_cache_config
FILTER_STATE_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 86400,
    'CACHE_KEY_PREFIX': 'superset_filter_'
}

class CeleryConfig(object):
    broker_url = f"redis://127.0.0.1:6379/0"
    imports = ("superset.sql_lab",)
    result_backend = f"redis://127.0.0.1:6379/1"
    worker_prefetch_multiplier = 1
    task_acks_late = False
    beat_schedule = {
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=10, hour=0),
        },
    }


CELERY_CONFIG = CeleryConfig

# Uncomment to setup Your App name
#APP_NAME = "BaysanSoft BI"

# Specify the App icon
#APP_ICON = "/static/assets/images/XYZ.png"
#APP_ICON_WIDTH = 63

#FAVICONS = [{"href": "/static/assets/images/XYZ.png"}]

