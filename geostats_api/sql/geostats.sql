-- CREATE DATABASE geostats;

--USE geostats;

CREATE TABLE Regions (
    code INT PRIMARY KEY, 
    name VARCHAR(20) NOT NULL
);

INSERT INTO Regions VALUES 
    (1, 'Northeast Region'),
    (2, 'Midwest Region'),
    (3, 'South Region'),
    (4, 'West Region');

CREATE TABLE Divisions (
    code INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    region INT NOT NULL, 
    FOREIGN KEY (region) REFERENCES Regions (code) 
);

INSERT INTO Divisions VALUES 
    (1, 'New England Division', 1), 
    (2, 'Middle Atlantic Division', 1),
    (3, 'East North Central Division', 2),
    (4, 'West North Central Division', 2),
    (5, 'South Atlantic Division', 3),
    (6, 'East South Central Division', 3),
    (7, 'West South Central Division', 3),
    (8, 'Mountain Division', 4),
    (9, 'Pacific Division', 4);

CREATE TABLE States (
    code INT PRIMARY KEY, 
    name VARCHAR(21) NOT NULL, 
    postal CHAR(2) NOT NULL,
    population INT NOT NULL,  
    division INT NOT NULL, 
    FOREIGN KEY (division) REFERENCES Divisions (code)
);

INSERT INTO states VALUES
    (9, 'Connecticut', 'CT', 3605944, 1), 
    (23, 'Maine', 'ME', 1362359, 1),
    (25, 'Massachusetts', 'MA', 7029917, 1), 
    (33, 'New Hampshire', 'NH', 1377529, 1), 
    (44, 'Rhode Island', 'RI', 1097379, 1), 
    (50, 'Vermont', 'VT', 643077, 1),
    (34, 'New Jersey', 'NJ', 9288994, 2), 
    (36, 'New York', 'NY', 20201249, 2), 
    (42, 'Pennsylvania', 'PA', 13002700, 2), 
    (18, 'Indiana', 'IN', 6785528, 3), 
    (17, 'Illinois', 'IL', 12801989, 3), 
    (26, 'Michigan', 'MI', 10077331, 3), 
    (39, 'Ohio', 'OH', 11799448, 3), 
    (55, 'Wisconsin', 'WI', 5893718, 3),
    (19, 'Iowa', 'IA', 3271616, 4), 
    (20, 'Kansas', 'KS', 2937880, 4), 
    (27, 'Minnesota', 'MN', 5706494, 4), 
    (29, 'Missouri', 'MO', 6154913, 4), 
    (31, 'Nebraska', 'NE', 1961504, 4), 
    (38, 'North Dakota', 'ND', 779094, 4),
    (46, 'South Dakota', 'SD', 886667, 4), 
    (10, 'Delaware', 'DE', 989948, 5), 
    (11, 'District of Columbia', 'DC', 689545, 5), 
    (12, 'Florida', 'FL', 21538187, 5), 
    (13, 'Georgia', 'GA', 10711908, 5), 
    (24, 'Maryland', 'MD', 6177224, 5), 
    (37, 'North Carolina', 'NC', 10439388, 5), 
    (45, 'South Carolina', 'SC', 5118425, 5), 
    (51, 'Virginia', 'VA', 8631393, 5), 
    (54, 'West Virginia', 'WV', 1793716, 5), 
    (1, 'Alabama', 'AL', 5024279, 6), 
    (21, 'Kentucky', 'KY', 4505836, 6), 
    (28, 'Mississippi', 'MS', 2961279, 6), 
    (47, 'Tennessee', 'TN', 6910840, 6), 
    (5, 'Arkansas', 'AR', 3011524, 7),
    (22, 'Louisiana', 'LA', 4657757, 7), 
    (40, 'Oklahoma', 'OK', 3959353, 7), 
    (48, 'Texas', 'TX', 29145505, 7), 
    (4, 'Arizona', 'AZ', 7151502, 8),
    (8, 'Colorado', 'CO', 5773714, 8), 
    (16, 'Idaho', 'ID', 1839106, 8), 
    (35, 'New Mexico', 'NM', 2117522, 8), 
    (30, 'Montana', 'MT', 1084225, 8), 
    (49, 'Utah', 'UT', 3205958, 8), 
    (32, 'Nevada', 'NV', 3104614, 8), 
    (56, 'Wyoming', 'WY', 576851, 8), 
    (2, 'Alaska', 'AK', 733391, 9), 
    (6, 'California', 'CA', 39538223, 9), 
    (15, 'Hawaii', 'HI', 1455271, 9), 
    (41, 'Oregon', 'OR', 4237256, 9), 
    (53, 'Washington', 'WA', 7705281, 9);