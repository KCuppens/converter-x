from datetime import datetime

from apps.convert.services.ConvertAction import ConvertAction
from converterx.celery import app


now = datetime.now()


@app.task(name="convert_action", queue="default")
def convert_action(action_id, conversion_id):
    converted_file = ConvertAction().convert_action(action_id, conversion_id)
    return converted_file.id
