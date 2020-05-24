#Tweet Stress

## Requirements
Python 3.6 or later
.net Core 3.1 or later
SQLServer 2017 or later

## Configuration for PythonWorkers
- Run the following command to prepare the folder structure
```bash
python PythonWorkers/create_structure.py
```
### Train model
- Open a a terminal and run the following command to generate raw files
```bash
python PythonWorkers/training.py
```

### Processing tweets
- Open a a terminal and run the following command to generate raw files
```bash
python PythonWorkers/tweet_processing.py
```

### Classify tweets
- Open another terminal and run the following command to analyse the tweets
```bash
python PythonWorkers/data_analysis.py
```

###Configuration for DataVisualization
- Open another terminal and run the following command to analyse the tweets
```bash
dotnet run DataVisualization/DataVisualization.csproj
```

