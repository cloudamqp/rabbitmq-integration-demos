# Change Data Capture with  RabbitMQ, Debezium and PostgreSQL

This demo aims to implement a Change Data Capture(CDC) pipeline.

CDC is an achitectural pattern that offers a way to automatically 
identify and capture changes(events) made in a data source(often, a database), 
such as new entries, updates, or deletions, as they happen. 
These events are then propagated in real-time, often through an 
event streaming platform, to downstream components, ranging from 
other databases to consumer applications that process these events.

# The Solution

Our demo will simulate an e-commerce platform's backend with two services:
- Inventory service
- Order management service

At a very high level, this is what the flow of execution would look like:
- Inventory service will connect to the PostgreSQL database and insert 
a new product record every 5 secs.
- Debezium server with a rabbitMQ streams sink connector will capture 
these changes and send them to a stream queue(***products***) in a Rabbitmq cluster.
- Order management service will connect to the Rabbitmq cluster 
and subscribe to the ***products*** queue, logging messages received to the console.