from decimal import Decimal


satellites = [
    # cbers2b source:
    # http://www.cbers.inpe.br/sobre/cameras/cbers1-2-2b.php    
    {
        "name": "CBERS 2B - CCD",
        "bands": [
            {
                "name": "pan",
                "range": [0.51, 0.73]
            },
            {
                "name": "azul",
                "range": [0.45, 0.52]
            },
            {
                "name": "verde",
                "range": [0.52, 0.59]
            },
            {
                "name": "vermelho",
                "range": [0.63, 0.69]
            },
            {
                "name": "infravermelho próximo",
                "range": [0.77, 0.89]
            }
        ]
    },
    {
        "name": "CBERS 2B - WFI",
        "bands": [
            {
                "name": "vermelho",
                "range": [0.63, 0.69]
            },
            {
                "name": "infravermelho próximo",
                "range": [0.77, 0.89]
            }
        ]
    },
    {
        "name": "CBERS 2B - HRC",
        "bands": [
            {
                "name": "pancromática",
                "range": [0.50, 0.80]
            },
        ]
    },
    # cbers4 source:
    # http://www.cbers.inpe.br/sobre/cameras/cbers3-4.php
    {
        "name": "CBERS 4 - MUX",
        "bands": [
            {
                "name": "B05 - B",
                "range": [0.45, 0.52]
            },
            {
                "name": "B06 - G",
                "range": [0.52, 0.59]
            },
            {
                "name": "B07 - R",
                "range": [0.63, 0.69]
            },
            {
                "name": "B08 - NIR",
                "range": [0.77, 0.89]
            }
        ]
    },
    {
        "name": "CBERS 4 - WFI",
        "bands": [
            {
                "name": "B13 - B",
                "range": [0.45, 0.52]
            },
            {
                "name": "B14 - G",
                "range": [0.52, 0.59]
            },
            {
                "name": "B15 - R",
                "range": [0.63, 0.69]
            },
            {
                "name": "B16 - NIR",
                "range": [0.77, 0.89]
            }
        ]
    },
    {
        "name": "CBERS 4 - PAN",
        "bands": [
            {
                "name": "B01 - Pan",
                "range": [0.51, 0.85]
            },
            {
                "name": "B02 - G",
                "range": [0.52, 0.59]
            },
            {
                "name": "B03 - R",
                "range": [0.63, 0.69]
            },
            {
                "name": "B04 - NIR",
                "range": [0.77, 0.89]
            }            
        ]
    },
    # cbers4a source:
    # http://www.cbers.inpe.br/sobre/cameras/cbers04a.php
    {
        "name": "CBERS 04A - MUX",
        "bands": [
            {
                "name": "B05 - B",
                "range": [0.45, 0.52]
            },
            {
                "name": "B06 - G",
                "range": [0.52, 0.59]
            },
            {
                "name": "B07 - R",
                "range": [0.63, 0.69]
            },
            {
                "name": "B08 - NIR",
                "range": [0.77, 0.89]
            }
        ]
    },
    {
        "name": "CBERS 04A - WFI",
        "bands": [
            {
                "name": "B13 - B",
                "range": [0.45, 0.52]
            },
            {
                "name": "B14 - G",
                "range": [0.52, 0.59]
            },
            {
                "name": "B15 - R",
                "range": [0.63, 0.69]
            },
            {
                "name": "B16 - NIR",
                "range": [0.77, 0.89]
            }
        ]
    },
    {
        "name": "CBERS 04A - WPM",
        "bands": [
            {
                "name": "B1 - B",
                "range": [0.45, 0.52]
            },
            {
                "name": "B2 - G",
                "range": [0.52, 0.59]
            },
            {
                "name": "B3 - R",
                "range": [0.63, 0.69]
            },
            {
                "name": "B4 - NIR",
                "range": [0.77, 0.89]
            },
            {
                "name": "P - PAN",
                "range": [0.45, 0.90]
            }
        ]
    },
    # landsat source:
    # https://www.usgs.gov/faqs/what-are-best-landsat-spectral-bands-use-my-research?qt-news_science_products=0#qt-news_science_products
    {
        "name": "Landsat MSS 1, 2, 3",
        "bands": [
            {
                "name": "Band 4 - green",
                "range": [0.5, 0.6]
            },
            {
                "name": "Band 5 - red",
                "range": [0.6, 0.7]
            },
            {
                "name": "Band 6 - Near Infrared",
                "range": [0.7, 0.8]
            },
            {
                "name": "Band 7 - Near Infrared",
                "range": [0.8, 1.1]
            }
        ]
    },
    {
        "name": "Landsat MSS 4, 5",
        "bands": [
            {
                "name": "Band 1 - green",
                "range": [0.5, 0.6]
            },
            {
                "name": "Band 2 - red",
                "range": [0.6, 0.7]
            },
            {
                "name": "Band 3 - Near Infrared",
                "range": [0.7, 0.8]
            },
            {
                "name": "Band 4 - Near Infrared",
                "range": [0.8, 1.1]
            }
        ]
    },
    {
        "name": "Landsat 4-5 TM and Landsat 7 ETM+",
        "bands": [
            {
                "name": "Band 1 - blue",
                "range": [0.45, 0.52]
            },
            {
                "name": "Band 2 - green",
                "range": [0.52, 0.60]
            },
            {
                "name": "Band 3 - red",
                "range": [0.63, 0.69]
            },
            {
                "name": "Band 4 - Near Infrared",
                "range": [0.77, 0.90]
            },
            {
                "name": "Band 5 - Short-wave Infrared",
                "range": [1.55, 1.75]
            },
            {
                "name": "Band 6 - Thermal Infrared",
                "range": [10.40, 12.50]
            },
            {
                "name": "Band 7 - Short-wave Infrared",
                "range": [2.09, 2.35]
            },
            {
                "name": "Band 8 - Panchromatic (Landsat 7 only)",
                "range": [0.52, 0.90]
            }
        ]
    },
    {
        "name": "Landsat 8 OLI and TIRS",
        "bands": [
            {
                "name": "Band 1 - coastal aerosol",
                "range": [0.43, 0.45]
            },
            {
                "name": "Band 2 - blue",
                "range": [0.45, 0.51]
            },
            {
                "name": "Band 3 - green",
                "range": [0.53, 0.59]
            },
            {
                "name": "Band 4 - red",
                "range": [0.64, 0.67]
            },
            {
                "name": "Band 5 - Near Infrared (NIR)",
                "range": [0.85, 0.88]
            },
            {
                "name": "Band 6 - Short-wave Infrared (SWIR) 1",
                "range": [1.57, 1.65]
            },
            {
                "name": "Band 7 - Short-wave Infrared (SWIR) 2",
                "range": [2.11, 2.29]
            },
            {
                "name": "Band 8 - Panchromatic",
                "range": [0.50, 0.68]
            },
            {
                "name": "Band 9 - Cirrus",
                "range": [1.36, 1.38]
            },
            {
                "name": "Band 10 - TIRS 1",
                "range": [10.60, 11.19]
            },
            {
                "name": "Band 11 - TIRS 2",
                "range": [11.50, 12.51]
            }
        ]
    }
]


def calc_fwhm(_min, _max):
    """Calculate full_width_half_max.
    Source: https://github.com/radiantearth/stac-spec/tree/master/extensions/eo#center_wavelength-and-full_width_half_max"""
    return Decimal(str(_max)) - Decimal(str(_min))


def calc_cw(_min, _max):
    """Calculate center_wavelength
    Source: https://github.com/radiantearth/stac-spec/tree/master/extensions/eo#center_wavelength-and-full_width_half_max"""
    return (Decimal(str(_min)) + Decimal(str(_max))) / 2


print('*' * 20)
for satellite in satellites:
    print(f"\nSatellite: {satellite['name']}")

    for band in satellite['bands']:
        print(f"\n- Band: {band['name']} - {band['range']}")
        print(f"calc_cw({band['range'][0]}, {band['range'][1]}): "
              f"{calc_cw(*band['range'])}")
        print(f"calc_fwhm({band['range'][0]}, {band['range'][1]}): "
              f"{calc_fwhm(*band['range'])}")

    print('\n' + ('*' * 20))
