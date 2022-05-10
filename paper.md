---
title: 'seifa: Tools to Use the Australian Socio-Economic Index Data for Areas (SEIFA)'
tags:
  - Python
  - economics
  - socio-economic advantage
authors:
  - name: Jonathan Garber^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0001-6754-4748
    affiliation: 1
  - name: Robert Turnbull^[co-first author] # note this makes a footnote saying 'co-first author'
    orcid: 0000-0003-1274-6750
    affiliation: 1
affiliations:
 - name: Melbourne Data Analytics Platform, University of Melbourne
   index: 1
date: 10 May 2021
bibliography: paper.bib

---

# Summary

The Australian Bureau of Statistics (ABS) publishes a variety of indexes for the Australian
economic environment. These include the Consumer Price Index (CPI) used for calculating inflation
and various indexes designed to measure socio-economic advantage. `ausdex` makes these data
available in a convenient Python package with a simple programatic and command-line interfaces. 


# Statement of need

`ausdex` is a Python package for querying data produced by the ABS and returning them in a convenient format. Currently ABS data is typically housed in Microsoft Excel spreadsheets linked from the data catalogue. This package interfaces with a subset of the the data to provide an Application Programming Interface (API) to derived economic metrics. For example, we expose the Australian consumer price index data to create an inflation calculator similar to the [cpi](https://github.com/palewire/cpi) Python package for adjusting US dollars. In addition, we bring API access to ABS Socio-Economic Index Data for Areas (SEIFA) aggregated at the suburb level in Victoria. This allows for quick assessment of the socio-economic history of a suburb in Victoria from historical census data. These datasets are housed in different online repositories and are aggregated to different spatial extents since statistical geographic boundaries are redrawn from every census dataset. The `ausdex.seifa_vic` submodule eliminates the need for downloading and combining datasets from different data sources, and allows for time series comparisons tied to the current suburb geographic boundaries. 

# Socio-economic indexes aggregated from census data for Victoria
Since 1986 (see table 1), the ABS has generated "Socio-Economic Indexes For Areas" (SEIFA) following each census [@seifa2016]. These indexes are aggregations of socio-economic inputs from the census forms (i.e. household income, rental/mortgage price, educational level) at the "census district level" or "mesh level" (2006–current). Census districts, or mesh levels, are geographic areas statistically defined from the census data to be the largest scale (smallest) geographic building blocks of demographic and socio-economic data based on population distribution. These statistical geographies are redrawn after each census. The ABS aggregates these to other statistical "levels" of geographic area from the Australian Statistical Geography Standard (ASGS) ([Statistical Areas Levels 1–4](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026)) suburbs [@abs_2016_sa1_shape] and local government areas in their "Data Cube" outputs. 

<!-- 
Since the 1986 census, the Australian Bureau of statistics (ABS) has generated "Socio Economic Indexes For Areas" (SEIFA) following each census. Information on the calculation of these indexes can be found here: [@abs_2016_seifa_tp; @abs_2011_seifa_tp; @abs_2001_seifa_tp].
-->

<!-- @abs_2006_seifa_tp; @abs_2001_seifa_tp; @abs_1996_seifa_tp] -->

<!-- 
These indexes are aggregations of socio economic inputs from the census forms (ie household income, rental/mortgage price, educational level) at the "census district level" or "mesh level" (2006–current). census districts, or mesh levels, geographic areas statistically defined from the census data to be the largest scale (smallest) geographic building blocks of demographic and socioeconomic data based on population distribution. These statistical geographies are redrawn after every census. The Australian Bureau of statistics does aggregate these to other statistical "levels" of geographic area from the Australian Statistical Geography Standard (ASGS) ([Statistical Areas levels 1 - 4](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026)) [@abs_2016_sa1_shape] suburbs and local government areas in their "Data Cube" outputs. 
-->

However, there have been several new suburbs created during the SEIFA program, and datasets aggregated by suburb are not readily available for census data before 2006.  To address this, we used the current Victorian suburb areal polygons [@vic_suburbs] as the constant spatial areas over which we aggregate all previous census datasets. To overcome suburb names that are repeated, the suburb polygons were also overlaid with local government areas [@vic_lga] to distinguish duplicate suburbs.

For an example, fig. 1 shows the Index of Economic Resources (IER) scores in 2015 for all suburbs in Victoria.


![Figure 1](paper_images/vic_map2.pdf)
<p align = "center"> Figure 1: A choropleth map of Victorian suburbs representing the interpolated IER scores in 2015.</p>


| Index | Name | Years Published |
| :---- | :------------ | :-------------- |
| IEO | Index of Education and Occupation | 1986, 1991, 1996, 2001, 2006, 2011, 2016 |
| IER | Index of Economic Resources | 1986, 1991, 1996, 2001, 2006, 2011, 2016 |
| IRSD | Index of Relative Socio-economic Disadvantage | 1986, 1991, 1996, 2001, 2006, 2011, 2016 |
| IRSAD | Index of Relative Socio-economic Advantage and Disadvantage | 2001, 2006, 2011, 2016 |
| UIRSA | Urban Index of Relative Socio-economic Advantage | 1991, 1996 |
| RIRSA | Rural Index of Relative Socio-economic Advantage | 1991, 1996 |

<p align = "center"> Table 1: The SEIFA indexes and the years published.</p>


## Spatially aggregating the 1986–2006 datasets

For the SEIFA datasets from 1986 to 2006, we collected census district polygons from AURIN [@aurin_portal] and the ABS data repository (2006), together with associated aggregated SIEFA scores. A list of the data sources is shown in table 2. These census district level SEIFA scores were aggregated to the current suburb GIS datasets [@vic_suburbs] using the following steps:

1. Suburbs and census districts were both reprojected to [EPSG:4326](https://spatialreference.org/ref/epsg/wgs-84/).
2. The polygons were unioned together, so the resulting polygon layer had an individual polygon for each overlapping census district and suburb (fig. 2).

3. The merged polygons were reprojected to a UTM projected coordinate system [EPSG:32756](https://epsg.io/32756). Note that this UTM coordinate system does not overlay the state of Victoria perfectly, but we are assuming that locally the measured areas are relatively consistent with each other.

4. The SEIFA scores for all of the census district parts within each suburb were aggregated using a weighted average, using the polygon area as the weight.

![Figure 2](paper_images/paper_output.pdf)
<p align = "center"> Figure 2: Map of three suburb outlines (black lines) for Richmond (left), Burnley (center), and Hawthorn (right) overlaying 1986 Census Districts (colored polygons with white boundaries). The census districts are colored according to the census district code. Note that these districts do not line up with suburb boundaries. The green district in the lower middle section spans parts of Richmond, and Cremorne. Likewise one of the orange and purple census districts spans two suburbs.</p>

## Spatially aggregating the 2011 and 2016 datasets

For the 2011 and 2016 datasets, we used the same procedure set out above, but started with a different statistical geographic dataset. We used Statistical Area Level 1 (SA1) aggregated estimates of the SEIFA variables published as an ABS data cube, and GIS polygons of SA1 boundaries from the ASGS created for 2011 and 2016 to derive suburb aggregated datasets.

## Data sources

| Year | Dataset type | Dataset source |
| :---- | :------------ | :-------------- |
| 1986 | Census district polygons and metrics | [@aurin_portal] wfs id: `AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_1986`| 
| 1991 | Census district polygons and metrics | [@aurin_portal] wfs id: `AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_1991`|
| 1996 | Census district polygons and metrics | [@aurin_portal] wfs id: `AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_1996`|
| 2001 | Census district polygons and metrics | [@aurin_portal] wfs id: `AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_2001`|
| 2006 | ABS census district shapefile|  [[@abs_2006_cd_shape]](https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1259030002_cd06avic_shape.zip&1259.0.30.002&Data%20Cubes&D62E845F621FE8ACCA25795D002439BB&0&2006&06.12.2011&Previous)|
| 2006 | ABS census district SEIFA metrics |   [[@abs_2006_seifa]](https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&2033055001_%20seifa,%20census%20collection%20districts,%20data%20cube%20only,%202006.xls&2033.0.55.001&Data%20Cubes&6EFDD4FA99C28C4ECA2574170011668A&0&2006&26.03.2008&Latest)|
| 2011 | ABS SA1 Polygons |  [[@abs_2011_sa1_shape]](https://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&1270055001_sa1_2011_aust_shape.zip&1270.0.55.001&Data%20Cubes&24A18E7B88E716BDCA257801000D0AF1&0&July%202011&23.12.2010&Latest)|
| 2011 | ABS SA1 SEIFA metrics |  [[@abs_2011_seifa]](https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&2033.0.55.001%20sa1%20indexes.xls&2033.0.55.001&Data%20Cubes&9828E2819C30D96DCA257B43000E923E&0&2011&05.04.2013&Latest)|
| 2016 | ABS SA1 Polygons |   [[@abs_2016_sa1_shape]](https://www.abs.gov.au/AUSSTATS/subscriber.nsf/log?openagent&1270055001_sa1_2016_aust_shape.zip&1270.0.55.001&Data%20Cubes&6F308688D810CEF3CA257FED0013C62D&0&July%202016&12.07.2016&Latest)|
| 2016 | ABS SA1 SEIFA metrics |  [[@abs_2016_seifa]](https://www.abs.gov.au/ausstats/subscriber.nsf/log?openagent&2033055001%20-%20sa1%20indexes.xls&2033.0.55.001&Data%20Cubes&40A0EFDE970A1511CA25825D000F8E8D&0&2016&27.03.2018&Latest)|
| All | VicMap suburb polygons|  [[@vic_suburbs]](https://data.gov.au/geoserver/vic-suburb-locality-boundaries-psma-administrative-boundaries/wfs?request=GetFeature&typeName=ckan_af33dd8c_0534_4e18_9245_fc64440f742e&outputFormat=json)|
| All | VicMap Local Government Area Polygons|   [[@vic_lga]](https://data.gov.au/geoserver/vic-local-government-areas-psma-administrative-boundaries/wfs?request=GetFeature&typeName=ckan_bdf92691_c6fe_42b9_a0e2_a4cd716fa811&outputFormat=json)|

Table 2. A list of data sources for `seifa_vic` submodule. 

# Module Features
The components of the module work both from a simple command-line interface and through the API. The code style adheres to PEP 8 [@pep8] through the use of the [Black](https://black.readthedocs.io/en/stable/) Python code formatter. Automated tests run as part of the CI/CD pipeline and testing coverage is above 96%. The package is thoroughly documented at [https://rbturnbull.github.io/ausdex/](https://rbturnbull.github.io/ausdex/).


# Acknowledgements

This project came about through a research collaboration with Vidal Paton-Cole and Robert Crawford (University of Melbourne). We acknowledge the support of our colleagues Aleksandra Michalewicz and Emily Fitzgerald.

This app uses the NCRIS-enabled Australian Urban Research Infrastructure Network (AURIN) Portal e-Infrastructure to access the following datasets:  

* AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_1986,
* AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_1991, 
* AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_1996,
* AU_Govt_ABS-UoM_AURIN_DB_3_seifa_cd_2001.

# References


