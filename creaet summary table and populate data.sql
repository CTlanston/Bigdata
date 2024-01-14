-- create summary table
use bigdata;
CREATE TABLE summary_airbnb_nyc_7 (
Column_name text,
TotalRowCount INT,
TotalCount INT,
NullCount INT,
UniqueCount INT,
MaxColumnValue int,
MinColumnValue int,
AvgValue int
);

-- populate the summary table with data
use bigdata;
INSERT INTO summary_airbnb_nyc_7
SELECT
'availability_365' ,COUNT(*) ,COUNT(availability_365)
,COUNT(*) - COUNT(availability_365) ,COUNT(DISTINCT
availability_365) ,MAX(availability_365)
,MIN(availability_365) ,AVG(CASE WHEN availability_365 IS
NOT NULL THEN availability_365 ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'calculated_host_listings_count', COUNT(*),
COUNT(calculated_host_listings_count), COUNT(*) -
COUNT(calculated_host_listings_count), COUNT(DISTINCT
calculated_host_listings_count),
MAX(calculated_host_listings_count),
MIN(calculated_host_listings_count), AVG(CASE WHEN
calculated_host_listings_count IS NOT NULL THEN
calculated_host_listings_count ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'cancellation_policy', COUNT(*), COUNT(cancellation_policy),
COUNT(*) - COUNT(cancellation_policy), COUNT(DISTINCT
cancellation_policy), NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'construction_year', COUNT(*), COUNT(construction_year),
COUNT(*) - COUNT(construction_year), COUNT(DISTINCT
construction_year), MAX(construction_year),
MIN(construction_year), AVG(CASE WHEN construction_year
IS NOT NULL THEN construction_year ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'host_id', COUNT(*), COUNT(host_id), COUNT(*) -
COUNT(host_id), COUNT(DISTINCT host_id), NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'host_identity_verified', COUNT(*),
COUNT(host_identity_verified), COUNT(*) -
COUNT(host_identity_verified), COUNT(DISTINCT
host_identity_verified), NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'host_name', COUNT(*), COUNT(host_name), COUNT(*) -
COUNT(host_name), COUNT(DISTINCT host_name), NULL, NULL,
NULL
FROM airbnb_nyc
UNION ALL
SELECT
'house_rules', COUNT(*), COUNT(house_rules), COUNT(*) -
COUNT(house_rules), COUNT(DISTINCT house_rules), NULL,
NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'id', COUNT(*), COUNT(id), COUNT(*) - COUNT(id),
COUNT(DISTINCT id), NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'instant_bookable',COUNT(*), COUNT(instant_bookable),
COUNT(*) - COUNT(instant_bookable), COUNT(DISTINCT
instant_bookable), NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'last_review', COUNT(*), COUNT(last_review), COUNT(*) -
COUNT(last_review),COUNT(DISTINCT last_review), NULL,
NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'lat', COUNT(*), COUNT(lat), COUNT(*) - COUNT(lat),
COUNT(DISTINCT lat), MAX(lat), MIN(lat), AVG(CASE WHEN
lat IS NOT NULL THEN lat ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'long', COUNT(*), COUNT(‘long‘), COUNT(*) - COUNT(‘long‘),
COUNT(DISTINCT ‘long‘), MAX(‘long‘), MIN(‘long‘),
AVG(CASE WHEN ‘long‘ IS NOT NULL THEN ‘long‘ ELSE NULL
END)
FROM airbnb_nyc
UNION ALL
SELECT
'minimum_nights', COUNT(*), COUNT(minimum_nights), COUNT(*) -
COUNT(minimum_nights), COUNT(DISTINCT minimum_nights),
MAX(minimum_nights), MIN(minimum_nights), AVG(CASE WHEN
minimum_nights IS NOT NULL THEN minimum_nights ELSE NULL
END)
FROM airbnb_nyc
UNION ALL
SELECT
'name', COUNT(*), COUNT(name), COUNT(*) - COUNT(name),
COUNT(DISTINCT name), NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'neighbourhood', COUNT(*), COUNT(neighbourhood), COUNT(*) -
COUNT(neighbourhood), COUNT(DISTINCT neighbourhood),
NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'neighbourhood_group', COUNT(*), COUNT(neighbourhood_group),
COUNT(*) - COUNT(neighbourhood_group), COUNT(DISTINCT
neighbourhood_group), NULL, NULL, NULL
FROM airbnb_nyc
UNION ALL
SELECT
'number_of_reviews', COUNT(*), COUNT(number_of_reviews),
COUNT(*) - COUNT(number_of_reviews), COUNT(DISTINCT
number_of_reviews), MAX(number_of_reviews),
MIN(number_of_reviews), AVG(CASE WHEN number_of_reviews
IS NOT NULL THEN number_of_reviews ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'price', COUNT(*), COUNT(price), COUNT(*) - COUNT(price),
COUNT(DISTINCT price), MAX(price), MIN(price), AVG(CASE
WHEN price IS NOT NULL THEN price ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'review_rate_number', COUNT(*), COUNT(review_rate_number),
COUNT(*) - COUNT(review_rate_number), COUNT(DISTINCT
review_rate_number), MAX(review_rate_number),
MIN(review_rate_number), AVG(CASE WHEN review_rate_number IS NOT NULL THEN review_rate_number ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'reviews_per_month', COUNT(*), COUNT(reviews_per_month),
COUNT(*) - COUNT(reviews_per_month), COUNT(DISTINCT
reviews_per_month), MAX(reviews_per_month),
MIN(reviews_per_month), AVG(CASE WHEN reviews_per_month
IS NOT NULL THEN reviews_per_month ELSE NULL END)
FROM airbnb_nyc
UNION ALL
SELECT
'room_type', COUNT(*), COUNT(room_type), COUNT(*) -
COUNT(room_type), COUNT(DISTINCT room_type), NULL, NULL,
NULL
FROM airbnb_nyc
UNION ALL
SELECT
'service_fee', COUNT(*), COUNT(service_fee), COUNT(*) -
COUNT(service_fee), COUNT(DISTINCT service_fee),
MAX(service_fee), MIN(service_fee), AVG(CASE WHEN
service_fee IS NOT NULL THEN service_fee ELSE NULL END)
FROM airbnb_nyc;