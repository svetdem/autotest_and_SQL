import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


def get_new_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + f"{configuration.GET_ORDER_BY_TRACK_PATH}?t={track}")
