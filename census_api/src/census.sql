-- CREATE DATABASE census;

--USE census;

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
