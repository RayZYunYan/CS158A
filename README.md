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

## 📁 Assignment 4: Final Leader Election (Refined Version)

An improved and fully stabilized implementation of the asynchronous ring-based leader election algorithm. This version removes unnecessary locks, improves connection robustness, ensures proper message forwarding without loss, and reduces redundant log outputs. It is suitable for both local multi-process testing and asynchronous startup conditions.

> See [`a4/README.md`](a4/README.md) for configuration files, run instructions, example terminal outputs, and a detailed description of improvements compared to Assignment 3.

## 📁 Assignment 5: Secure HTTP Client

A Python script that establishes a secure TLS connection to `www.google.com` using the `socket` and `ssl` modules. It sends a manually constructed HTTP GET request for the root path `/`, receives the full response, and saves the HTML body content to a local file. 

> See [`a5/README.md`](a5/README.md) for run instructions, example output, and socket + SSL usage notes.