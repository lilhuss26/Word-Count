# Word Count Project

This project demonstrates two different approaches to implementing a Word Count application using Python:
1.  **MapReduce Style**: A custom implementation simulating the MapReduce paradigm.
2.  **PySpark**: An implementation using the Apache Spark framework (PySpark).

The goal is to count the frequency of each word in a given text file (`Football Analytics With Python & R Learning Data Science Through the Lens of Sports.txt`).

## Prerequisites

*   **Python 3.x**
*   **PySpark**: Required for running the Spark implementation.
    ```bash
    pip install pyspark
    ```

## Project Structure

*   `MapReduce_WordCount.py`: Python script implementing word count using a custom Mapper and Reducer.
*   `PySpark_WordCount.py`: Python script implementing word count using PySpark DataFrames.
*   `Football Analytics With Python & R Learning Data Science Through the Lens of Sports.txt`: The input text file used for analysis.

## Usage

### Running the MapReduce Implementation

This script reads the text file, cleans the data, maps words to counts, groups them, and then reduces them to find the total count for each word. It prints the top 10 most frequent words.

```bash
python MapReduce_WordCount.py
```

### Running the PySpark Implementation

This script uses Spark functionality to read the file, split lines into words, explode the arrays, and group by word to count occurrences. It displays the top 10 most frequent words.

```bash
python PySpark_WordCount.py
```
