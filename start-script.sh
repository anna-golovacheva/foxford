#!/bin/bash

# Function to be executed upon receiving SIGINT
cleanup() {
    echo "Caught SIGINT. Cleaning up..."
    kill $server_pid1 $server_pid2  # Terminates both server processes
    exit
}

# Set up the trap
trap cleanup SIGINT

# Start the Uvicorn server in the background
uvicorn src.main:app --reload &
server_pid1=$!
printf $server_pid1
  # Get the process ID of the last backgrounded command

# Start the npm server in the background
cd bot && python3 -m main 8003 &
server_pid2=$!  # Get the process ID of the last backgrounded command
printf $server_pid2

# Wait indefinitely. The cleanup function will handle interruption and cleanup.
wait
