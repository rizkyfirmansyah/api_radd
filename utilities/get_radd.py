"""
:Required packages
    earthengine-api
"""

import ee
import time
from utilities import settings

try:
    ee.Initialize()
except Exception as e:
    ee.Authenticate()
    ee.Initialize()

_init = settings.__init__()

peat = ee.FeatureCollection(_init.PEAT_NO_GO_ZONE)
collection = ee.ImageCollection(_init.RADD_ALERT).filterDate(_init.START_DATE, _init.END_DATE).map(lambda image: image.clip(peat))


# =========== EXPORT ALL IMAGES ===========
image_ids = collection.aggregate_array('system:index').getInfo()
print('Total image: ', len(image_ids))

for i, image_id in enumerate(image_ids):
    image = ee.Image(collection.filter(ee.Filter.eq('system:index', image_id)).first())

    task = ee.batch.Export.image.toCloudStorage(**{
        'image': image,
        'description': _init.EXPORT_DESCRIPTION + i,
        # 'fileNamePrefix': image.id().getInfo(),
        'fileFormat': _init.EXPORT_FORMAT,
        'bucket': _init.EXPORT_BUCKET,
        'path': _init.EXPORT_BUCKET_PATH,
        'scale': _init.EXPORT_SCALE,
        'region': image.geometry().getInfo()['coordinates'],
        'formatOptions': _init.EXPORT_FORMAT_OPTIONS,
        'maxPixels': _init.EXPORT_MAX_PIXELS
    })
    task.start()
    print('Polling for task (id: {}).'.format(i + 1))

tasks = ee.batch.Task.list()
for task in tasks:
  task_id = task.status()['id']
  task_state = task.status()['state']
  print(task_id, task_state)

while task.status()['state'] in ['READY', 'RUNNING']:
    print(task.status())
    time.sleep(10)
else:
    print(task.status())

# REFERENCES
# https://github.com/Yichabod/natural_disaster_pred
