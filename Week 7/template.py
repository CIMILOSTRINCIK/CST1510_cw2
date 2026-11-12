"""
RECORD CHECK  -  my version
===========================

Name  :  Amal Iliasov
Lane  :  Cyber
Date  :  12.11.2026

Run it:   python template.py
"""
def parse_line(raw_line):
    """Clean and parse one record."""
    line = raw_line.strip()
    fields = {}

    for piece in line.split(","):
        key, value = piece.split("=", 1)
        key = key.strip().lower()
        value = value.strip()
        fields[key] = value

    result = {
        "src": fields["src"],
        "attempts": float(fields["attempts"]),
        "result": fields["result"].upper()
    }
    return result

def status_of(result):
    """Return FLAGGED or OK for a security record."""
    if result == "FAILED":
        return "FLAGGED"
    else:
        return "OK"

record_count = 0
flagged_count = 0

with open("lab7_records.txt") as f:
    for raw_record in f:
        record_count += 1

        try:
            record = parse_line(raw_record)
            status = status_of(record["result"])

            print(record, status)

            if status == "FLAGGED":
                flagged_count += 1

        except ValueError as error:
            print("Could not parse:", raw_record.strip())
            print("Error:", error)

print(f"Records: {record_count} | Flagged: {flagged_count}")