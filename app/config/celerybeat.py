from datetime import timedelta
# from celery.schedules import crontab


def __get_empty_schedule() -> dict:
    return {}


def __get_example_schedule() -> dict:
    return {
        'task-example': {
            'task': 'src.tasks.task_example',
            'schedule': timedelta(seconds=5)
        }
    }


def get_celerybeat_schedule(set_names: str) -> dict:
    try:
        tasks = {}
        set_names = set_names.split(",")
        for set_name in set_names:
            if not set_name:
                continue

            tasks.update(
                globals()[f"__get_{set_name}_schedule"]()
            )
        return tasks
    except (KeyError, AttributeError):
        set_name = "empty"
        return globals()[f"__get_{set_name}_schedule"]()
