has_high_income=True
has_good_credit=True
has_criminal_record=False
print(f"HI={has_high_income} GC={has_good_credit} CR={has_criminal_record}")
print("AND")
if has_high_income and has_good_credit:
    print("Eligible for loan")
print('OR')
if has_high_income or has_good_credit:
    print("Eligible for loan")
print('AND NOT')
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")