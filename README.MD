# Banned Books Pipeline 📚🚫

Welcome to the **Banned Books Pipeline** repository! This project is an ETL pipeline that scrapes data from PEN America regarding banned books from 2021 to 2024. This document provides a comprehensive overview of the project, including setup instructions, usage guidelines, and contribution details.

![Banned Books](https://img.shields.io/badge/Banned_Books-Pipeline-brightgreen)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Banned Books Pipeline aims to provide a structured approach to collecting and analyzing data on banned books. With the rise of censorship in literature, it is crucial to document and understand the trends and reasons behind these bans. This project uses a combination of technologies to create a seamless ETL (Extract, Transform, Load) process.

## Features

- **Data Scraping**: Automatically scrapes data from PEN America.
- **Data Storage**: Stores the data in a PostgreSQL database.
- **Data Transformation**: Cleans and formats the data for analysis.
- **Data Visualization**: Provides visual insights using Streamlit.
- **Scheduled Runs**: Uses Airflow to schedule and manage ETL tasks.

## Technologies Used

- **Airflow**: For orchestrating the ETL pipeline.
- **Pandas**: For data manipulation and analysis.
- **PostgreSQL**: For storing the scraped data.
- **Streamlit**: For creating interactive data visualizations.
- **Python**: The primary programming language for the project.
- **Neon**: A cloud-native PostgreSQL service for data storage.

## Installation

To set up the Banned Books Pipeline, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/moemen-2003/banned-books-pipeline.git
   cd banned-books-pipeline
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up PostgreSQL**:
   Ensure you have PostgreSQL installed and running. Create a database for the project.

5. **Configure Airflow**:
   Initialize Airflow and set up your DAGs.

6. **Run the Pipeline**:
   Follow the instructions in the `docs` folder to run the ETL pipeline.

## Usage

To use the Banned Books Pipeline, execute the following command:

```bash
airflow dags trigger banned_books_pipeline
```

This command will start the ETL process, scraping data from PEN America and storing it in your PostgreSQL database.

For more details on the data structure and how to query it, refer to the documentation in the `docs` folder.

## Data Sources

The primary data source for this project is PEN America. Their data provides insights into the trends and reasons behind book bans from 2021 to 2024. 

For releases, please visit the [Releases](https://github.com/moemen-2003/banned-books-pipeline/releases) section. Download the necessary files and execute them as needed.

## Contributing

We welcome contributions to the Banned Books Pipeline. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Create a pull request.

Please ensure your code follows the existing style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any questions or suggestions, please reach out:

- **Email**: your.email@example.com
- **GitHub**: [moemen-2003](https://github.com/moemen-2003)

Thank you for your interest in the Banned Books Pipeline! Together, we can make a difference in understanding the impact of censorship on literature. 

For more information and to stay updated, please check the [Releases](https://github.com/moemen-2003/banned-books-pipeline/releases) section.