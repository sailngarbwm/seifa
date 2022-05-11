# seifa

![pipline](https://github.com/sailngarbwm/seifa/actions/workflows/coverage.yml/badge.svg)
[<img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/sailngarbwm/49262550cc8b0fb671d46df58de213d4/raw/coverage-badge.json">](<https://sailngarbwm.github.io/seifa/coverage/>)
[<img src="https://github.com/sailngarbwm/seifa/actions/workflows/docs.yml/badge.svg">](<https://sailngarbwm.github.io/seifa/>)
[<img src="https://img.shields.io/badge/code%20style-black-000000.svg">](<https://github.com/psf/black>)
[![status](https://joss.theoj.org/papers/817baa72d2b17b535af8f421a43404b0/status.svg)](https://joss.theoj.org/papers/817baa72d2b17b535af8f421a43404b0)

An interface for several Australian socio-economic indexes for socio-economic advantage.

The Australian Bureau of Statistics (ABS) publishes a variety of indexes for the Australian
economic environment. These include the Consumer Price Index (CPI) used for calculating inflation
and a variety of indexes designed to measure socio-economic advantage. `seifa` makes these data
available in a convenient Python package with a simple programatic and command line interfaces. 

## Installation

You will soon be able to install `seifa` from the Python Package Index (PyPI):

```
pip install seifa
```

## Command Line Usage


You can use the seifa-vic command to interpolate an ABS census derived Socio economic score for a given year, suburb, and SEIFA metric
```
$ seifa seifa-vic 2020 footscray ier_score
$ 861.68

```

## Module Usage

```python
>>> from seifa.seifa_vic import interpolate_vic_suburb_seifa
>>> interpolate_vic_suburb_seifa(2007, 'FOOTSCRAY', 'ier_score')
874.1489807920245
>>> interpolate_vic_suburb_seifa([2007, 2020], 'FOOTSCRAY', 'ier_score', fill_value='extrapolate')
array([874.14898079, 861.68112674])
```

## Data

Data for the socio economic scores by suburbs comes from a variety of sources, and goes between 1986 to 2016 for the index of economic resources, and the index of education and opportunity, other indexes are only available for a subset of census years

When this module is first used, data will be downloaded and preprocessed from several locations. Access to the AURIN API is necessary via this [form](https://aurin.org.au/resources/aurin-apis/sign-up/). You will be prompted to enter the username and password when you first run the submodule. This will be saved in the app user directory for future use. You can also create a config.ini file in the repository folder with the following:

```toml
[aurin]
username = {aurin_api_username}
password = {aurin_api_password}
```

## Contributing

See the guidelines for contributing and our code of conduct in the [documentation](https://sailngarbwm.github.io/seifa/contributing.html).

## License and Disclaimer

`seifa` is released under the Apache 2.0 license.

While every effort has been made by the authors of this package to ensure that the data and calculations used to produce the results are accurate, as is stated in the license, we accept no liability or responsibility for the accuracy or completeness of the calculations. 
We recommend that users exercise their own care and judgment with respect to the use of this package.
 
## Credits

`seifa` was written by [Dr Jonathan Garber](https://findanexpert.unimelb.edu.au/profile/787135-jonathan-garber) and [Dr Robert Turnbull](https://findanexpert.unimelb.edu.au/profile/877006-robert-turnbull) from the [Melbourne Data Analytics Platform](https://mdap.unimelb.edu.au/).

Please cite from the article when it is released. Details to come soon.

## Acknowledgements

This project came about through a research collaboration with [Dr Vidal Paton-Cole](https://findanexpert.unimelb.edu.au/profile/234417-vidal-paton-cole) and [Prof Robert Crawford](https://findanexpert.unimelb.edu.au/profile/174016-robert-crawford). We acknowledge the support of our colleagues at the Melbourne Data Analytics Platform: [Dr Aleksandra Michalewicz](https://findanexpert.unimelb.edu.au/profile/27349-aleks-michalewicz) and [Dr Emily Fitzgerald](https://findanexpert.unimelb.edu.au/profile/196181-emily-fitzgerald).
