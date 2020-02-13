from highcharts import Highchart


def generate_highchart(options: dict, datasets: list) -> Highchart:
    chart = Highchart()
    chart.set_dict_options(options)

    for dataset in datasets:
        if "series_type" not in dataset.keys():
            dataset["series_type"] = options["chart"]["type"]

        if "marker" not in dataset.keys() \
                and "plotOptions" in options \
                and "area" in options["plotOptions"] \
                and "marker" in options["plotOptions"]["area"]:
            dataset["marker"] = options["plotOptions"]["area"]["marker"]
        chart.add_data_set(**dataset)
    return chart
