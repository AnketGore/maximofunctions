import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# PYTHONUNBUFFERED=1;DYLD_LIBRARY_PATH=/Users/carlos.ferreira1ibm.com/ve/new-python3/lib/python3.7/site-packages/clidriver/lib:$DYLD_LIBRARY_PATH;PYTHONPATH=/Users/carlos.ferreira1ibm.com/ws/watson-classifier
import json
from iotfunctions.db import Database
from iotfunctions.ui import UISingle,UIMulti
import os

#os.environ['isICP'] = 'true'
#print(os.environ.get('isICP'))
#print(os.getenv('isICP'))

#os.environ.setdefault("REST_METADATA_URL", "demo.monitor.omenablement.democore.cloud:443")

logger = logging.getLogger(__name__)

#Connect to the service
with open('../credentials_as.json', encoding='utf-8') as F:
    credentials = json.loads(F.read())
db_schema = None
db = Database(credentials=credentials)


#Connect to the service
db = Database(credentials = credentials)

#Define how the constant is represented on the UI using UISingle
max_temp_cf = UISingle(name='max_temp_AGG',
               description='Ensure temperatures does not exceed max_temp_AGG',
               datatype=float)

#Register the constant using the database object
db.register_constants([max_temp_AGG])