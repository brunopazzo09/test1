-There is no unique identifier for a property in the data. How would you approach this to come up with a column that can be used as a unique id for each property? Would you combine any columns for instance? Can you test your method that it returns unique values? Are there any issues? 

To have an ID for each property and to make sure that it is unique i would combine the following columns: paon, saon, street, locality, town/city, district. In the code, this is done by concatenating the strings together. To test the uniqueness of properties I have created an array with all properties (for testing purposes I have used a smaller CSV file containing the first 5 000 entries of the 2013 csv file and the first 5000 entries of the 2018 csv file) and then I have compared its length to set(array): if the length of the set is smaller than the length of the normal array (non-unique data), it means that some properties in the array are duplicates.


-Once you have defined a property unique id (unfortunately this doesn’t exist in the data so it needs to be defined by you), how would you store the data in your SQL database? What table structure would you use? 

To store the data in an SQL database, I'd structure the table like this:

CREATE TABLE Properties (
    unique_id VARCHAR(255) PRIMARY KEY,
    property_type CHAR(1),
    old_new CHAR(1),
    paon VARCHAR(255),
    saon VARCHAR(255),
    street VARCHAR(255),
    locality VARCHAR(255),
    town_city VARCHAR(255),
    district VARCHAR(255),
    county VARCHAR(255),
    postcode VARCHAR(255)
);


-How would you work on improving the performance of the queries? Would you use primary keys, indexes? 

To improve the performance of the queries, I'd make sure that the queries are well-written, and I'd use the "unique_id" primary key. Moreover, it could be helpful to create an index if it is found that many queries rely on a specific variable, for example "postcode":
CREATE INDEX idx_postcode ON Properties(postcode)


-Can you write a query that returns the transactions that took place in EC1A between 2018-04-01 and 2019-12-31?

Basing the query on this table:

CREATE TABLE Transactions (
    unique_id VARCHAR(255) PRIMARY KEY,
    property_unique_id VARCHAR(255),
    price INT,
    transfer_date DATE,
    duration VARCHAR(1),
    PPD_type VARCHAR(1),
    record_status VARCHAR(1),
    FOREIGN KEY (property_unique_id) REFERENCES Properties(unique_id)
);

The query to return such transactions would be:

SELECT *
FROM Transactions AS t
JOIN Properties AS p ON t.property_unique_id = p.unique_id
WHERE p.postcode = 'EC1A'
    AND t.transfer_date >= '2018-04-01'
    AND t.transfer_date <= '2019-12-31';


-Utilizing the class structure in python you have defined, create methods to return the number of properties that have been sold in a postcode, and which transaction_ids refer to those.
    Test with ST10 4BS. Were there 2 transaction in 2019?
        Testing with ST10 4BS returns:
        "Number of properties sold in the postcode ST10 4BS: 2"
        

    Given a transaction_id, return which property it refers to. Test with {7C2D0701-0253-4963-E053-6B04A8C07B97}. Does it return a property in Cornwall?
        Since I have used a dictionary data type indexed with transaction IDs to store transactions, I find it simpler to use "transactions[id].property" to see the property referred by the transaction ID.
        Testing with the given transaction ID (I had to use the 2018.csv file since this transaction appears only in that file) it prints:
        requested property:
            Property Type: O
            Old/New: N
            PAON: WHEAL SQUIRES, 4
            SAON:
            Street: TREMELLIN LANE
            Locality: ST ERTH
            Town/City: HAYLE
            District: CORNWALL
            Postcode: TR27 6EY
            County: CORNWALL
        
        which is correct.

-Which postcodes have seen the highest increase in transactions during the last 5 years? No need to do the analysis at the full postcode level; the first part is sufficient. Thus instead of e.g. SE13 5HA, consider only SE13.

I do not have sufficient RAM to test this, however I have written the code necessary to do so and it should work, based on my testing with custom CSV files.

-Can you come up with an indication of a ‘migration’ metric in the UK? Perhaps it would be best if you combined the postcode coordinates dataset for this exercise (url #6). Where is the ‘centre of gravity’ in terms of number of transactions of the population moving to every year? Where is the ‘centre of gravity’ in terms of value moving to? For now, consider that the ‘centre of gravity’ is a weighted average function, so for each year determine the weighted average of the coordinates based on number of transactions, or value. 


