import traceback
from datetime import datetime

import connexion
import six

from TimeSeriesIoT.models.inline_response200 import InlineResponse200  # noqa: E501
from TimeSeriesIoT import util

from influxdb import InfluxDBClient


def mean_sensor_id_get(sensor_id, start_date=None, end_date=None):  # noqa: E501
    """Calculer la moyenne d&#39;un capteur entre deux dates

     # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str
    :param start_date: Integer/timestamp of the start date
    :type start_date: int
    :param end_date: Integer/timestamp of the end date
    :type end_date: int

    :rtype: List[int]
    """
    try:
        client = InfluxDBClient('influxdb', 8086, 'user', 'user', 'sensor')
        sensor_id = "laptop_temperature_1"
        str = ""
        if start_date is not None:
            str = f"WHERE time > '{datetime.fromtimestamp(start_date)}'"
        if end_date is not None:
            if len(str) > 0:
                str += " AND "
            else:
                str = "WHERE "
            str += f"time < '{datetime.fromtimestamp(end_date)}'"
        request = f"SELECT mean({sensor_id}) from client1 {str} GROUP BY *;"
        print(request)
        result = client.query(request)
        mean = list(result.get_points())[0]['mean']
    except:
        traceback.print_exc()
        return []
    return [mean]


def value_sensor_id_get(sensor_id):  # noqa: E501
    """Récupérer la dernière valeur d&#39;un capteur

     # noqa: E501

    :param sensor_id: String Id of the sensor to get
    :type sensor_id: str

    :rtype: InlineResponse200
    """
    try:
        client = InfluxDBClient('influxdb', 8086, 'user', 'user', 'sensor')
        result = client.query('SELECT laptop_temperature_1 from client1 GROUP BY * ORDER BY DESC LIMIT 1;')
        date = list(result.get_points())[0]["time"]
        value = list(result.get_points())[0][sensor_id]

    except:
        traceback.print_exc()
        return {"Error": ""}
    return {"date": date, "value": value}
