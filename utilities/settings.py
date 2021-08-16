# =========== COLLECTION SETTINGS ===========

def __init__():
    """
    Static variables for your data and its filter
    """
    PEAT_NO_GO_ZONE = 'users/gis/land_use/no_go_zone_v3'
    RADD_ALERT = 'projects/radar-wur/raddalert/v1'
    START_DATE = '2020-01-01'
    END_DATE = '2020-06-30'
    YEARS = list(range(2019, 2020))
    TEMP_DIR_PATH = './data/'
    # =========== FUNCTIONS ===========

        

    # =========== EXPORT SETTINGS ===========
    """
    Define your variables here to export data into your Google Cloud Platform bucket
    """

    EXPORT_DESCRIPTION = 'RADD_ALERT_EXPORT_'
    EXPORT_TIF = 'radd_alert_peat'
    EXPORT_FORMAT = 'GeoTIFF'
    EXPORT_BUCKET = 'wri-monitoring'
    EXPORT_BUCKET_PATH = 'peat/'
    EXPORT_FORMAT_OPTIONS = { 'cloudOptimized': True }
    EXPORT_PREFIX = 'RADD_ALERT_' + START_DATE + '_' + END_DATE
    EXPORT_FOLDER = 'GEE'
    EXPORT_SCALE = 10
    EXPORT_MAX_PIXELS = 1e10
