from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "genai_requests_total",
    "Total number of GenAI requests"
)

REQUEST_LATENCY = Histogram(
    "genai_request_latency_seconds",
    "Latency of GenAI requests"
)