CREATE TABLE Branch (
    branch_id INTEGER PRIMARY KEY,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    postcode TEXT NOT NULL
);



INSERT INTO Branch
(branch_id, street, city, postcode)
VALUES
(1, 'Shaw Lane', 'Leeds', 'LS6 5UL');

INSERT INTO Branch
(branch_id, street, city, postcode)
VALUES
(2, 'Park Row', 'Leeds', 'LS1 5HD');

SELECT * FROM Branch;



CREATE TABLE Staff (
    staff_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT,
    branch INTEGER,
    FOREIGN KEY (branch) REFERENCES Branch(branch_id)
);



INSERT INTO Staff
(staff_id, name, role, branch)
VALUES
(101, 'Tom', NULL, NULL);

INSERT INTO Staff
(staff_id, name, role, branch)
VALUES
(102, 'Sarah', NULL, NULL);

INSERT INTO Staff
(staff_id, name, role, branch)
VALUES
(103, 'James', NULL, NULL);

INSERT INTO Staff
(staff_id, name, role, branch)
VALUES
(104, 'Emily', NULL, NULL);

SELECT * FROM Staff;



UPDATE Staff
SET role = 'Manager',
    branch = 1
WHERE staff_id = 101;

UPDATE Staff
SET role = 'Cashier',
    branch = 1
WHERE staff_id = 102;

UPDATE Staff
SET role = 'Manager',
    branch = 2
WHERE staff_id = 103;

UPDATE Staff
SET role = 'Cashier',
    branch = 2
WHERE staff_id = 104;

SELECT * FROM Staff;



INSERT INTO Branch
VALUES (3, 'City Square', 'Leeds', 'LS1 2ES');

INSERT INTO Staff
VALUES (105, 'David', 'Manager', 3);

INSERT INTO Staff
VALUES (106, 'Lucy', 'Cashier', 3);


INSERT INTO Branch
VALUES (1, 'New Street', 'Leeds', 'LS1 1AA');

INSERT INTO Branch
VALUES (4, 'High Street', NULL, 'LS1 1AA');



SELECT *
FROM Staff
WHERE role = 'Manager';

SELECT *
FROM Staff
WHERE role = 'Cashier';

SELECT *
FROM Staff
WHERE branch = 1;

SELECT
    Staff.staff_id,
    Staff.name,
    Staff.role,
    Branch.street,
    Branch.city,
    Branch.postcode
FROM Staff
JOIN Branch ,
ON Staff.branch = Branch.branch_id;