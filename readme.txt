PostgreSQL code relies on config.py and database.ini, which had my credentials on them. They will not work
without new credentials.

message_producer.py reads in example_csv.csv, so as to prevent a 1000 line read-in every time. This can be
changed inside the file, line 11.