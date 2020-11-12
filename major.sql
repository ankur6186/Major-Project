CREATE TABLE Table1 (
 	ID INTEGER PRIMARY KEY AUTOINCREMENT,
 	Mail varchar(320),
 	Meet varchar(255),
 	Location VARCHAR(32),
 	Device VARCHAR(32),
 	Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
 	Latitude FLOAT,
 	longitude FLOAT,
 	Admin BOOLEAN,
 	JorL BOOLEAN
);

-- Test Database
-- insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ivoibs@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Raipur', 'Laptop', datetime('now', 'localtime'), 21.250000, 81.629997, 1, 0);
-- insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ivoibs@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Raipur', 'Laptop', datetime('now', 'localtime'), 21.250000, 76.629997, 1, 0);
-- insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ivoibs@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Raipur', 'Laptop', datetime('now', 'localtime'), 21.250000, 81.629997, 1, 1);
-- insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('blare@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Moga, Punjab', 'iOS', datetime('now', 'localtime'),30.816460,75.171707, 1, 0);
-- insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('alice@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Batala, Punjab', 'Laptop', datetime('now', 'localtime'),31.823462,75.205063, 0, 0);

-- Real Database
insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ivoibs@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Raipur', 'Laptop', datetime('now', 'localtime'), 21.250000, 81.629997, 1, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('rahul@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Mumbai', 'Laptop', datetime('now', 'localtime'), 19.076090 , 72.8774, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ajay@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Lucknow', 'Android', datetime('now', 'localtime'), 26.850000 , 80.949997, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('anmol@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Delhi', 'Laptop', datetime('now', 'localtime'),28.610001 , 77.230003, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('barkha@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Ratnagiri', 'Android', datetime('now', 'localtime'),16.994444 , 73.300003, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ben@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Ratnagiri', 'Android', datetime('now', 'localtime'),16.994444 , 73.300003, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ram@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Gotak, Karnataka', 'iOS', datetime('now', 'localtime'),16.166700 , 74.833298, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ajay@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Lucknow', 'Android', datetime('now', 'localtime'), 26.850000 , 80.949997, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('raj@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Mumbai', 'Laptop', datetime('now', 'localtime'), 19.076090 , 72.8774, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('raj@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Mumbai', 'Laptop', datetime('now', 'localtime'), 19.076090 , 72.8774, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('rakesh@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Raipur', 'Android', datetime('now', 'localtime'), 21.250000, 81.629997, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('riya@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Belgaum, Karnataka', 'Laptop', datetime('now', 'localtime'),15.852792, 74.498703, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ben@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Ratnagiri', 'Android', datetime('now', 'localtime'),16.994444 , 73.300003, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('ranjan@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Barh, Bihar', 'iOS', datetime('now', 'localtime'),25.477585,85.709091, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('nikita@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Roorkee, Uttarakhand', 'iOS', datetime('now', 'localtime'),29.854263,77.888000, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('abha@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', datetime('now', 'localtime'),12.971599,77.594566, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('shreyansh@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', datetime('now', 'localtime'),12.971599,77.594566, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('tushar@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', datetime('now', 'localtime'),12.971599,77.594566, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('abha@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Bengaluru, Karnataka', 'Android', datetime('now', 'localtime'),12.971599,77.594566, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('soha@gmail.com', 'https://meet.google.com/wjw-gkvb-wdi', 'Almora, Uttarakhand', 'Laptop', datetime('now', 'localtime'),29.594189 , 79.653893, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('sohail@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Kharagpur, West Bengal', 'Android', datetime('now', 'localtime'),22.346010,87.231972, 1, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('shivani@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Fatehpur, Rajasthan', 'Android', datetime('now', 'localtime'),27.995020,74.961792, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('shivam@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Siliguri, West Bengal', 'iOS', datetime('now', 'localtime'),26.732311,88.410286, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('shivani@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Fatehpur, Rajasthan', 'Android', datetime('now', 'localtime'),27.995020,74.961792, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('swaraj@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Mangaluru, Karnataka', 'Android', datetime('now', 'localtime'),12.915605,74.855965, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('sitara@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', datetime('now', 'localtime'),23.946800,88.049713, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('sitara@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', datetime('now', 'localtime'),23.946800,88.049713, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('archana@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', datetime('now', 'localtime'),23.946800,88.049713, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('rakshatha@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Mangaluru, Karnataka', 'Android', datetime('now', 'localtime'),12.915605,74.855965, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('shabana@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Vijaypur, Jammu and Kashmir', 'iOS', datetime('now', 'localtime'),32.564522,75.023148, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('archana@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Kandi, West Bengal', 'Laptop', datetime('now', 'localtime'),23.946800,88.049713, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('rihanna@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Rahon, Punjab', 'Android', datetime('now', 'localtime'),31.052128,76.117500, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('gurpreet@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Rahon, Punjab', 'Laptop', datetime('now', 'localtime'),31.052128,76.117500, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('bheem@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Mangaluru, Karnataka', 'Android', datetime('now', 'localtime'),12.915605,74.855965, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('anisha@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Shimoga, Karnataka', 'iOS', datetime('now', 'localtime'),13.929930,75.568100, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('devansh@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Shimoga, Karnataka', 'iOS', datetime('now', 'localtime'),13.929930,75.568100, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('rihanna@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Rahon, Punjab', 'Android', datetime('now', 'localtime'),31.052128,76.117500, 0, 1);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('blare@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Moga, Punjab', 'iOS', datetime('now', 'localtime'),30.816460,75.171707, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('alice@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Batala, Punjab', 'Laptop', datetime('now', 'localtime'),31.823462,75.205063, 0, 0);

insert INTO Table1(Mail, Meet, Location, Device, Timestamp, Latitude, longitude, Admin , JorL) Values ('blare@gmail.com', 'https://meet.google.com/wjw-gkve-abc', 'Moga, Punjab', 'iOS', datetime('now', 'localtime'),30.816460,75.171707, 0, 1);
