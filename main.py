import csv
from postcode import Postcode
from property import Property
from transaction import Transaction
from collections import defaultdict
from datetime import datetime

main_filename=r"CSV files\main.csv"

properties = []
transactions = {}
postcodes = {}

with open(main_filename, 'r') as file:
    reader = csv.reader(file)
    row_count = 0

    for row in reader:
        row_count+=1

        t_transaction_unique_id=row[0]
        t_price=row[1]
        t_transfer_date=row[2]
        t_postcode_code=row[3]
        t_property_type=row[4]
        t_old_new=row[5]
        t_duration=row[6]
        t_paon=row[7]
        t_saon=row[8]
        t_street=row[9]
        t_locality=row[10]
        t_town_city=row[11]
        t_district=row[12]
        t_county=row[13]
        t_ppd_type=row[14]
        t_record_status=row[15]

        t_property=Property(t_property_type, t_old_new, t_paon, t_saon, t_street, t_locality, t_town_city, t_district, t_county, t_postcode_code)
        t_transaction=Transaction(t_property, t_transaction_unique_id, t_price, t_transfer_date, t_duration, t_ppd_type, t_record_status)

        if t_postcode_code in postcodes:
            postcodes[t_postcode_code].add_property(t_property)
        else:
            temp_postcode = Postcode(t_postcode_code)
            temp_postcode.add_property(t_property)
            postcodes[t_postcode_code] = temp_postcode

        properties.append(t_property)
        transactions[t_transaction_unique_id] = (t_transaction)

if len(properties) > len(set(properties)):
    print("All members of the properties array are unique.")
else:
    print("Not all properties are unique (the chosen unique_id isn't unique), or there are no duplicate entries in the provided csv file.")

try:
    num_properties_sold = sum(1 for transaction in transactions.values() if transaction.property.postcode == "ST10 4BS" and transaction.transfer_date.startswith("2019"))
    print("Number of properties sold in the postcode ST10 4BS in 2019:", num_properties_sold)
except KeyError:
    print("The given postcode doesn't exist.")

try:
    print("Requested property: " + transactions["{7C2D0701-0253-4963-E053-6B04A8C07B97}"].property)
except KeyError:
    print("The given transaction ID doesn't appear in the data.")


postcode_transactions = defaultdict(int)
previous_counts = defaultdict(int)

# Calculate the transaction counts for each postcode prefix
for transaction in transactions.values():
    temp_postcode = transaction.property.postcode

    if temp_postcode and " " in temp_postcode:
        postcode_prefix = temp_postcode.split()[0]
        transaction_year = int(transaction.transfer_date[:4])
        current_year = datetime.now().year

        if current_year - transaction_year <= 5:
            postcode_transactions[postcode_prefix] += 1
        else:
            previous_counts[postcode_prefix] += 1


postcode_changes = {prefix: count - previous_counts[prefix] for prefix, count in postcode_transactions.items()}
postcode_changes_prefix_only = {prefix.split()[0]: change for prefix, change in postcode_changes.items()}

sorted_postcodes = sorted(postcode_changes_prefix_only, key=postcode_changes_prefix_only.get, reverse=True)

# Print the postcodes with the highest increase in transactions
for postcode_prefix in sorted_postcodes:
    print(f"Postcode Prefix: {postcode_prefix}, Increase in Transactions: {postcode_changes_prefix_only[postcode_prefix]}")
