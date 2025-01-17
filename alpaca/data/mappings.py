from typing import Dict

BAR_MAPPING: Dict[str, str] = {
    "t": "timestamp",
    "o": "open",
    "h": "high",
    "l": "low",
    "c": "close",
    "v": "volume",
    "n": "trade_count",
    "vw": "vwap",
    "x": "exchange",
}

QUOTE_MAPPING: Dict[str, str] = {
    "t": "timestamp",
    "ax": "ask_exchange",
    "ap": "ask_price",
    "as": "ask_size",
    "bx": "bid_exchange",
    "bp": "bid_price",
    "bs": "bid_size",
    "c": "conditions",
    "z": "tape",
    "x": "exchange",
}

TRADE_MAPPING: Dict[str, str] = {
    "t": "timestamp",
    "p": "price",
    "s": "size",
    "x": "exchange",
    "i": "id",
    "c": "conditions",
    "z": "tape",
}

SNAPSHOT_MAPPING: Dict[str, str] = {
    "latestTrade": "latest_trade",
    "latestQuote": "latest_quote",
    "minuteBar": "minute_bar",
    "dailyBar": "daily_bar",
    "prevDailyBar": "previous_daily_bar",
}

XBBO_MAPPING: Dict[str, str] = {
    "t": "timestamp",
    "ax": "ask_exchange",
    "ap": "ask_price",
    "as": "ask_size",
    "bx": "bid_exchange",
    "bp": "bid_price",
    "bs": "bid_size",
}
