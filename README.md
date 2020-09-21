<h1>GOGetter 3000</h1>

Reads hosts and values from .csv file and calculates min, max, avg, sum for each host.

## How to use GOGetter:


`python main.py` &rarr; Reads `input.csv` and saves output in `output.csv`

Optional arguments for speifying input/output path example:
```
python main.py -i %input_path% -o %output_path%
```
Valid rows (Only valid rows are processed):

* have same number of elements in both columns
* each value in row is greater than 0
* each host name in the row match the pattern XXXX.XXXX

Tested on Python 3.7 with love
