#!/bin/bash
setsid ollama serve & 
sleep 1
mv models/* /root/.ollama/models/
gunicorn -b 0.0.0.0:8081 --workers 1 --threads 4 --timeout 12000  app:app
