# CS158A – Assignment 5: Secure HTTP Client

## Overview

This project demonstrates how to establish a secure HTTPS connection using low-level `socket` and `ssl` modules in Python. The script `secureget.py` connects to `www.google.com` over port 443, sends a well-formed HTTP GET request, receives the server’s response, and writes the HTML content to `response.html`.

The implementation focusing on manual socket programming and SSL handshake, without using any third-party libraries.

## Files

secureget.py         # Main Python script to establish secure connection and retrieve HTML  
response.html        # Output HTML body from the HTTPS server  
README.md            # This documentation file

## How to Run

Ensure you have Python 3.7 or later installed.

From the terminal, run the script as follows:

    python secureget.py

On success, a file named `response.html` will be created in the current directory. You can open it in a web browser to view the raw HTML structure of Google’s homepage.

## Example Output

Command:

    $ python secureget.py
    [+] Connected to www.google.com:443 with SSL
    [+] HTML body saved to response.html

Partial contents of `response.html`:

    <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en">
    <head><meta content="Search the world's information, including webpages..." name="description">
    <title>Google</title>
    ...

Note that the page may appear broken if opened in a browser, since no CSS, JavaScript, or images are included—only the raw HTML body is saved.

## Notes

- The script uses `socket.create_connection()` to establish a TCP connection.
- It wraps the socket with SSL using `ssl.create_default_context().wrap_socket()`.
- A manual HTTP GET request is constructed and sent.
- The HTTP response is received in full, and the body is separated from the headers using `\r\n\r\n`.
- Only the HTML content is saved—no additional resources (CSS, JS, images) are fetched.
- This behavior is intentional and satisfies the project’s requirement of retrieving HTML content securely via socket + SSL.

## Author

Ray Zhang  
CS158A - Computer Networks (Summer 2025)  
San Jose State University
