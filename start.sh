#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

docker run --rm -d -p 8080:80 \
  -v ${DIR}/db.json:/data/db.json \
  -v ${DIR}/routes.json:/data/routes.json \
  -v ${DIR}/index.html:/usr/local/lib/node_modules/json-server/lib/server/public/index.html \
  --name ds \
  clue/json-server \
  --routes /data/routes.json

echo 'Visit http://localhost:8080/'

docker logs -f ds
