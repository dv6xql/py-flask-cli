from src.app import create_celery_app
# from src.helpers.app_environment import (
#     is_production, is_testing
# )
from src.helpers.cli_manager import (
    execute_command
)

celery = create_celery_app()


@celery.task()
def task_example() -> None:
    # if not is_production() and not is_testing():
    #     return None

    print('Example task.')
    execute_command("cli example")

    return None
