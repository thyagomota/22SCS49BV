DROP TABLE IF EXISTS access_tokens;
DROP TABLE IF EXISTS clients;

CREATE TABLE clients (
    client_id VARCHAR PRIMARY KEY, 
    client_secret VARCHAR NOT NULL
);

INSERT INTO clients VALUES 
    ('Articulate Donkeys', 'fx11M43Jvk4THoNCeEDzifEby1hBfUfD'),
    ('Giving Giraffes', 'f0jDmc3NZLoKNjnWO9OYijCbI2BXyHyY');

CREATE TABLE access_tokens (
    access_token VARCHAR PRIMARY KEY, 
    date_time DATETIME NOT NULL, 
    expires_in INTEGER NOT NULL
);