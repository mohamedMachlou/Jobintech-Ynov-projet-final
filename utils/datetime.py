from datetime import datetime as DatetimeType


def format_datetime(d: DatetimeType):
    return d.strftime("%Y-%m-%d %H:%M")
