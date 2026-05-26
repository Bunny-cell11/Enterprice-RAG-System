
BLOCKED_PATTERNS = [
    "ignore previous instructions",
    "bypass security",
    "show hidden documents"
]

def detect_prompt_injection(query):
    query = query.lower()
    return any(pattern in query for pattern in BLOCKED_PATTERNS)
