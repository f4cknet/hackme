import snowflake.client

for _ in range(20):
    print(snowflake.client.get_guid())