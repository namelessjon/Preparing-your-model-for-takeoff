# Sketch of an RScript operator for Apache Airflow

import subprocess
import re

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.exceptions import AirflowException


def escape_string(string):
  """escape the weird characters R sometimes outputs"""
  string = repr(string)  # easy escape
  string = re.sub(r"\\n", "\n", string)
  string = re.sub(r"\\t", "\t", string)
  return string


class ROperator(BaseOperator):
  template_fields = ('script', 'arguments', 'cwd')

  @apply_defaults
  def __init__(self, script, arguments=[], cwd=None, **kwargs):
    self.script = script
    self.arguments = arguments
    self.cwd = cwd
    super(ROperator, self).__init__(**kwargs)

  def execute(self, context):
    r_proc = subprocess.Popen(
      ['/usr/bin/Rscript', self.script] + new_args,
      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True,
      cwd = self.cwd)
    (r_stdoutdata, _) = r_proc.communicate()
    self.log.info("Rscript output %s", escape_string(r_stdoutdata))

    if r_proc.returncode != 0:
      raise AirflowException("Rscript {} failed with return code {}".format(self.script, r_proc.returncode))

    return escape_string(r_stdoutdata)
