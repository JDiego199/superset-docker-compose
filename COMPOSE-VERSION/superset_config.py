
import os
from datetime import timedelta
from typing import Optional
from cachelib.redis import RedisCache
from superset.superset_typing import CacheConfig
from cachelib.file import FileSystemCache
from datetime import timedelta

from celery.schedules import crontab
  #  from datetime import timedelta
 
def get_env_variable(var_name: str, default: Optional[str] = None) -> str:
    """Get the environment variable or raise exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        else:
            error_msg = "The environment variable {} was missing, abort...".format(
                var_name
            )
            raise EnvironmentError(error_msg) 


REDIS_HOST = get_env_variable("REDIS_HOST")
REDIS_PORT = get_env_variable("REDIS_PORT")
REDIS_CELERY_DB = get_env_variable("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = get_env_variable("REDIS_RESULTS_DB", "1")
RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")
    
SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@db:5432/SupersetDB'
SECRET_KEY = 'soqGt/ST8hIl3JVW2glo82Oa7sQX0OF/5PQLNrfSeLRw1PlQKf+T2yGs'	
FEATURE_FLAGS = {"ALERT_REPORTS": True,
		"DASHBOARD_CROSS_FILTERS":True,
		"HORIZONTAL_FILTER_BAR": True,
		"ENABLE_TEMPLATE_PROCESSING":True,
		"EMBEDDED_SUPERSET": True}

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
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
}
DATA_CACHE_CONFIG = CACHE_CONFIG

EXPLORE_FORM_DATA_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_explore_'
}
# filter_cache_config
FILTER_STATE_CACHE_CONFIG: CacheConfig = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_filter_'
}

class CeleryConfig(object):
    broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    imports = ("superset.sql_lab",)
    result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
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

