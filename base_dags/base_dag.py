from datetime import datetime
from airflow.models import DAG

class BaseDAG(DAG):

    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime.today(),
        'retries': 0
    }

    def __init__(self, dag_name, scheduler, limit=1000, tags=[]):

        self.dag_name = dag_name
        self.scheduler = scheduler
        self.limit = limit
        self.tags = tags

        super().__init__(
            dag_id=self.dag_name,
            default_args=BaseDAG.default_args,
            max_active_runs=1,
            schedule_interval=self.scheduler,
            catchup=False,
            tags=self.tags
        )
