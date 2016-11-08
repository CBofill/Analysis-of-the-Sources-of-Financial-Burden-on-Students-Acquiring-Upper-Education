# Analysis of the Sources of Financial Burden on Students Acquiring Upper Education
This report analyzes the contributing factors to student financial burden at institutions of higher education in the U.S. using data of varying types aggregated from multiple sources. It implements a Random Forest Regression model of institutions and a permutation based variable importance technique. The report presents the best solution achieved, discusses its strengths and weaknesses, and scope for future work.  This was the capstone project for the Udacity Machine Learning Engineer Nanodegree program.

## Reading the Report
The report itself is provided as a pdf, `Analysis of the Sources of Financial Burden on Students Acquiring Upper Education.pdf`, which presents the problem, process, and solution step by step. 

## Viewing the Work
### iPython Notebook
Most of the code and any work not included in the solution are not included in the report, but can be seen in `capstone_project.ipynb`. Viewing this iPython notebook requires iPython. [iPython installation instructions can be found here.](https://ipython.org/install.html)

### Libraries
The following libraries are used in the notebook:
* Pandas
* Numpy
* SciPy
* SciKit-Learn
* MatPlotLib
* Seaborn  

The easiest way to install these is with the Anaconda distribution of Python. All but Seaborn are included in the default install of Anaconda, available [here](https://www.continuum.io/downloads), and Seaborn can be added once Anaconda is installed with:
```
conda install -c anaconda seaborn=0.7.1
```

### Datasets
Two datasets are drawn from to create the aggregated dataset `MergedDatset.csv`. These are:
* The College Scorecard Dataset, by the Office of Planning, Evalutaion, and Policy Development
  * Available at [https://catalog.data.gov/dataset/college-scorecard](https://catalog.data.gov/dataset/college-scorecard)
* The Delta Cost Project Database, by the Integraded Postsecondary Education Data System
  * Available at [http://nces.ed.gov/ipeds/deltacostproject/](http://nces.ed.gov/ipeds/deltacostproject/)  

The code used to create `MergedDataset.csv` is found in `mergeIPEDSCSC.py`. Running this code requires all of the IPEDS and CSC data to be present.  

#### Note:  
Running the **Data Exploration** portion of the notebook requries the `delta_public_00_12.csv` file from the IPEDS dataset and `MERGED2000_PP.csv` file from the CSC dataset. However, to avoid downloading the original sources of data and just use the provided `MergedDataset.csv`, run the cell that imports the libraries and the cell that declares the IPEDS feature lists and skip ahead to the **Complete Dataset** section.

### Unused Work
The last section of the notebook contains work that is not included in the solution. This code is not guaranteed to run without error, and is merely there as a record.
