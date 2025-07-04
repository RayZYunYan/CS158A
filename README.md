# CS158A – Computer Networks (Summer 2025)

This repository contains programming assignments for the CS158A Computer Networks course at San Jose State University, Summer 2025.

## 📁 Assignment 1: Variable-Length Message

A TCP-based client-server application where the client sends a variable-length message with a 2-byte length prefix, and the server responds with the same message in uppercase.

> See [`a1/README.md`](a1/README.md) for usage instructions and example output.

## 📁 Assignment 2: Chat Server with Multiple Clients

A multithreaded TCP chat server that allows multiple clients to join, exchange messages, and exit independently. The server relays messages from each client to all others, using the format `<client_port>: <message>`.

> See [`a2/README.md`](a2/README.md) for detailed instructions and sample terminal outputs.

## 📁 Assignment 3: Ring-Based Leader Election

An asynchronous leader election protocol using sockets and threading in a ring topology. Each node (process) generates a unique UUID and communicates with its neighbors over TCP to determine the leader.

> See [`a3/README.md`](a3/README.md) for configuration, run instructions, and election log output.
