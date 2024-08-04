# AWS Data Engineering with Alpha Vantage Data API

## Project Overview

This project demonstrates data engineering techniques on AWS, leveraging financial market data from Alpha Vantage and Finnhub APIs. The primary objective is to create a robust, automated ETL pipeline for analyzing options maturity walls within the US stock market, enabling more informed trading decisions and improved position management.

## Architecture

The project utilizes a serverless architecture on AWS, incorporating the following services as main components of the pipeline:

1. Amazon S3
2. AWS Lambda (EventBridge Triggered)
3. AWS Glue
4. Amazon Athena

This architecture ensures scalability, cost-effectiveness, and minimal operational overhead.

## Key Features

- **Scheduled Data Ingestion**: Automated collection of stock and options data from Alpha Vantage and Finnhub APIs.
- **Scalable Storage**: Efficient data storage using Amazon S3, providing a durable and cost-effective solution.
- **ETL Workflows**: AWS Glue jobs for sophisticated extract, transform, and load operations.
- **SQL-based Analysis**: Amazon Athena for running complex SQL queries on the processed data.
- **Options Maturity Wall Analysis**: Custom analytics to identify and analyze options maturity trends.

## Benefits

- **Enhanced Trading Strategies**: Gain deeper insights into options maturity patterns for more strategic trade placements.
- **Improved Risk Management**: Better understanding of market dynamics to manage trading positions effectively.

## Disclaimer

This project is for educational purposes only. It is not financial advice. Always conduct your own research and consult with a qualified financial advisor before making investment decisions.