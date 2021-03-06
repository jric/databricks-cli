# Databricks CLI
# Copyright 2017 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"), except
# that the use of services to which certain application programming
# interfaces (each, an "API") connect requires that the user first obtain
# a license for the use of the APIs from Databricks, Inc. ("Databricks"),
# by creating an account at www.databricks.com and agreeing to either (a)
# the Community Edition Terms of Service, (b) the Databricks Terms of
# Service, or (c) another written agreement between Licensee and Databricks
# for the use of the APIs.
#
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from databricks_cli.configure.config import get_jobs_client


def create_job(json):
    return get_jobs_client().client.perform_query('POST', '/jobs/create', data=json)


def list_jobs():
    return get_jobs_client().list_jobs()


def delete_job(job_id):
    return get_jobs_client().delete_job(job_id)


def get_job(job_id):
    return get_jobs_client().get_job(job_id)


def reset_job(json):
    return get_jobs_client().client.perform_query('POST', '/jobs/reset', data=json)


def run_now(job_id, jar_params, notebook_params, python_params, spark_submit_params):
    return get_jobs_client().run_now(job_id, jar_params, notebook_params, python_params,
                                     spark_submit_params)
