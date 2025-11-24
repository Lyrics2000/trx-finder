#!/bin/bash


# Set up signal handlers for graceful shutdown
trap 'send_shutdown_notification; exit 0' SIGTERM SIGINT

# Run the password cracker
echo "Starting password cracker with parameters:"

python trx.py

