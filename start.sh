#!/bin/bash
docker build -t groups-server .
docker run --rm -p 5000:5000 groups-server
