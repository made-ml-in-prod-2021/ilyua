from airflow.models import DagBag
import unittest

class TestNewDataDag(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
       cls.dagbag = DagBag('../dags')

   def test_dag_loaded(self):
       dag = self.dagbag.get_dag(dag_id='new_data')
       assert self.dagbag.import_errors == {}
       assert dag is not None
       assert len(dag.tasks) == 1


if __name__ == '__main__':
    unittest.main()
