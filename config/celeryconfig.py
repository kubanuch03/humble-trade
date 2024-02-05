broker_url = "redis://redis:6379/0"
result_backend = "redis://redis:6379/0"
# broker_url = "redis://127.0.0.1:6379/"
# result_backend = "redis://127.0.0.1:6379/"


task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Asia/Bishkek"
enable_utc = False
broker_connection_retry_on_startup = True
