-- Hosts Table
CREATE TABLE Hosts (
host_id BIGINT ,
host_name varchar(35),
host_identity_verified ENUM('unconfirmed','verified'),
PRIMARY KEY(host_id, host_name),
CHECK(host_identity_verified IS NOT NULL)
);
-- Listings Table
CREATE TABLE Listings (
id BIGINT ,
host_id BIGINT ,
host_name varchar(35),
'name' TEXT,
room_type ENUM('Private␣room','Entire␣home/apt','Shared␣
room','Hotel␣room'),
minimum_nights DOUBLE CHECK (minimum_nights >= 0),
PRIMARY KEY(id),
FOREIGN KEY(host_id, host_name) REFERENCES Hosts(host_id,
host_name)
);
-- Reviews Table
CREATE TABLE Reviews (
id BIGINT ,
host_id BIGINT ,
host_name varchar(35),
last_review TEXT,
number_of_reviews DOUBLE CHECK (number_of_reviews >= 0),
review_rate_number DOUBLE CHECK (review_rate_number BETWEEN 1
AND 5),
reviews_per_month DOUBLE CHECK (reviews_per_month >= 0),
PRIMARY KEY(id, host_id, host_name),
FOREIGN KEY(id) REFERENCES Listings(id),
FOREIGN KEY(host_id, host_name) REFERENCES Hosts(host_id,
host_name)
);
-- Locations Table
CREATE TABLE Locations (
id BIGINT ,lat DOUBLE ,
'long' DOUBLE ,
neighbourhood TEXT,
neighbourhood_group
ENUM('Brooklyn','Manhattan','Queens','Staten␣
Island','Bronx'),
PRIMARY KEY(id),
FOREIGN KEY(id) REFERENCES Listings(id)
);
-- Pricing Table
CREATE TABLE Pricing (
id BIGINT ,
price DOUBLE CHECK (price >= 0),
service_fee DOUBLE CHECK (service_fee >= 0),
cancellation_policy ENUM('Flexible', 'Moderate', 'Strict'),
PRIMARY KEY(id),
FOREIGN KEY(id) REFERENCES Listings(id)
);

-- Index Creation
CREATE INDEX idx\_host ON Hosts(host\_id, host\_name);
CREATE INDEX idx\_listing ON Listings(id);
CREATE INDEX idx\_review ON Reviews(id, host\_id, host\_name);
CREATE INDEX idx\_location ON Locations(id)
