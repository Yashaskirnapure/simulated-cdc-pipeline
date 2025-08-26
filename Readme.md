# CDC Consumer Project (Work in Progress)

This project demonstrates a **real-time Change Data Capture (CDC) pipeline** using PostgreSQL, Debezium, Redpanda, and a Java Spring Boot consumer.  

## Overview

The pipeline captures changes (insert/update/delete) from the PostgreSQL database and streams them through Redpanda (Kafka-compatible broker). A Java application consumes these events for further processing.  

**Final goal:** Build a dashboard providing actionable insights such as user sign-ups, order revenue trends, and other analytics.  

## Workflow (until now)
![workflow](diagrams/workflow.png)

## Tools & Roles

| Tool                 | Role                                                                 |
|---------------------|----------------------------------------------------------------------|
| **PostgreSQL**      | Source OLTP database with customers, products and orders schemas. |
| **Debezium**        | Captures CDC events from PostgreSQL and publishes to Redpanda.       |
| **Redpanda**        | Kafka-compatible broker to transport CDC events in real-time.        |
| **Java Spring Boot**| Consumes CDC events, processes/logs them, and prepares them for dashboard analytics. |

## Features Implemented

- Captures inserts, updates, and deletes from the tables.  
- Streams events in JSON format to Redpanda.  
- Java consumer prints CDC events in real-time.  

## Work in Progress

- Dashboard for analytics (user sign-ups, order revenue trends, etc.).  
- Advanced filtering, aggregation, and visualization of CDC events.
