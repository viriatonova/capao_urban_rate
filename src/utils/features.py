import re


def get_coordinates(geo_dict) -> list:
    return [
        float(re.search(r"\s*\[([-\d.]+),\s*([-\d.]+)\]", geo_dict).group(1)),
        float(re.search(r"\s*\[([-\d.]+),\s*([-\d.]+)\]", geo_dict).group(2)),
    ]


if __name__ == "__main__":
    var = '{"type":"Point","coordinates":[-41.49867380840735,-12.598777086158863]}'
    print(get_coordinates(var))
