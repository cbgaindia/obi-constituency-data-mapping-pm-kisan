# PM Kisan Yojna constituency level data

## Background
This repository is a part of the [Open Budgets India](https://openbudgetsindia.org) Phase 2 where we are trying to estimate scheme expenditure data at the Assembly Constituency (AC) and Parliamentary Constituency (PC) levels. It is a collaborative initiative between [Centre for Budget and Governance Accountability (CBGA)](https://www.cbgaindia.org) and [CivicDataLab](https://civicdatalab.in). Currently this data exists only at the administrative boundary level which varies between district, block, gram panchayat or village depending on the scheme.

### Description
This repository explains the process of estimating pay data at the village level scrapped from the government MIS portal to pay estimates at the assembly constituency (AC) and parliamentary constituency (PC) level. It contains state-wise folder for the scheme.

### Directory Structure


    obi-constituency-data-mapping-pm-kisan
    |-- odisha/
    |   |-- data/
    |   |   |-- qgis/
    |   |   |-- raw/
    |   |   |-- updated/  
    |   |-- methodology/                     
    |   |-- results/                   
    |   |-- scripts/               
    |   |-- summary/      
    |   |-- README.md/

### Dependencies
#### Softwares Used

* QGIS v3.18.3 Zurich
* Jupyter Notebook
* Python v3.6+

#### Python Library Used
* openpyxl
* numpy
* pandas

### Run Locally
Clone the project

```
git clone https://github.com/cbgaindia/obi-constituency-data-mapping-pm-kisan.git
```

Go to project Directory

```bash
cd obi-constituency-data-mapping-pm-kisan
```
Install dependencies
```
$ pip install notebook
```

### Issue Reporting

For any new feature or bug reports, please request it in [issues](https://github.com/cbgaindia/obi-constituency-data-mapping-pm-kisan/issues).

### Data License

Unless explicitly stated, all datasets in this repository is shared under AGPL v3 license. Please mention and link to relevant dataset in the attribution.
