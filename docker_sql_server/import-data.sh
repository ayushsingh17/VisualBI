# wait for the SQL Server to come up
sleep 90s
#script to create the DB and the schema in the DB
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Password1!" -i 01-create-database.sql
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Password1!" -i 02-create-table.sql
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "Password1!" -i 03-insert-data.sql