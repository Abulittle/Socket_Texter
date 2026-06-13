# Python Group Chat

A simple multi-client group chat application built using Python sockets and threading.

## Features

- Multiple clients can connect simultaneously
- Real-time message broadcasting
- Username/address identification
- Join and leave notifications
- Threaded client handling
- TCP socket communication
- Custom message protocol using headers

## Technologies Used

- Python 3
- socket
- threading
- datetime

## Project Structure

```
project/
│
├── server.py
├── client.py
└── README.md
```

## How It Works

### Server

The server:

1. Creates a TCP socket.
2. Binds to a specified IP address and port.
3. Listens for incoming connections.
4. Creates a new thread for each client.
5. Receives messages from clients.
6. Broadcasts messages to all connected clients.

### Client

The client:

1. Connects to the server.
2. Starts a receive thread for incoming messages.
3. Starts a send thread for user input.
4. Displays incoming messages in real time.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd <repository-name>
```

Make sure Python 3 is installed:

```bash
python3 --version
```

## Running the Server

```bash
python3 server.py
```

Example output:

```text
Starting server...
Listening on 127.0.1.1
```

## Running a Client

Open another terminal:

```bash
python3 client.py
```

Run multiple client instances in separate terminals to test group messaging.

## Usage

Type a message:

```text
>> Hello everyone!
```

Example output:

```text
Alice: Hello everyone!
2:10:20AM
```

To disconnect:


```text
>> /exit
```


## Message Protocol

Messages are sent using a fixed-size header.

Example:

```
[64-byte length header][message body]
```

The server first reads the header to determine the size of the incoming message and then reads the actual message.


## Example Session

Client 1:

```text
>> Hello
```

Client 2:

```text
Client1: Hello
14:30:25
```

Client 2:

```text
>> Hi!
```

Client 1:

```text
Client2: Hi!
14:30:28
```

## Learning Objectives

This project demonstrates:

- TCP networking
- Client-server architecture
- Multithreading
- Socket programming
- Message protocols
- Concurrent communication

## License

MIT License
