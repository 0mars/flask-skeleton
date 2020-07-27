#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
    alter user postgres createdb;
    CREATE DATABASE skel;
    GRANT ALL PRIVILEGES ON DATABASE skel TO postgres;
EOSQL


psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
    alter user postgres createdb;
    CREATE DATABASE skel_test;
    GRANT ALL PRIVILEGES ON DATABASE skel_test TO postgres;
EOSQL

