#!/bin/bash

docker run --rm --network host -v "$PWD":/liquibase/changelog liquibase/liquibase:4.17.0 --defaultsFile=/liquibase/changelog/liquibase-local.properties --search-path=/liquibase/changelog update
