import pandas as pd

recent_alerts = pd.DataFrame(
    [
        {
            "Transaction ID": "TX-98745123",
            "Customer": "Roberts, A.",
            "Amount": "$1,574.99",
            "Risk Score": "98%",
            "AI Reason": "Location anomaly",
            "Action": "Review",
        },
        {
            "Transaction ID": "TX-98745089",
            "Customer": "Chen, L.",
            "Amount": "$3,299.00",
            "Risk Score": "95%",
            "AI Reason": "Velocity pattern",
            "Action": "Review",
        },
        {
            "Transaction ID": "TX-98744978",
            "Customer": "Garcia, M.",
            "Amount": "$899.50",
            "Risk Score": "91%",
            "AI Reason": "Biometric mismatch",
            "Action": "Review",
        },
    ]
)
