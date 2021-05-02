DELETE FROM DEPARTMENT;
DELETE FROM EMPLOYEE;
DELETE FROM PROJECT;
DELETE FROM WORKSON;
INSERT INTO Department (deptNo, deptName) VALUES (1, 'deptName#1');
INSERT INTO Department (deptNo, deptName) VALUES (2, 'deptName#2');
INSERT INTO Department (deptNo, deptName) VALUES (3, 'deptName#3');
INSERT INTO Department (deptNo, deptName) VALUES (4, 'deptName#4');
INSERT INTO Department (deptNo, deptName) VALUES (5, 'deptName#5');

INSERT INTO Employee VALUES (1, 'Millie', 'Robben', 'adress#1', '19/02/1991', 'M', 'position#1', 2);
INSERT INTO Employee VALUES (2, 'Michale', 'Maucher', 'adress#2', '01/12/1976', 'F', 'position#2', 1);
INSERT INTO Employee VALUES (3, 'Jenniffer', 'Odel', 'adress#3', '28/03/1982', 'F', 'position#3', 2);
INSERT INTO Employee VALUES (4, 'Maximo', 'Noller', 'adress#4', '15/04/1976', 'M', 'position#4', 3);
INSERT INTO Employee VALUES (5, 'Georgina', 'Stiehr', 'adress#5', '02/02/1989', 'F', 'position#5', 3);

UPDATE department SET mgrEmpNo =1 WHERE deptNo = 2;
UPDATE department SET mgrEmpNo =2 WHERE deptNo = 1;
UPDATE department SET mgrEmpNo =3 WHERE deptNo = 2;
UPDATE department SET mgrEmpNo =4 WHERE deptNo = 3;
UPDATE department SET mgrEmpNo =5 WHERE deptNo = 3;

INSERT INTO Project VALUES (1, 'superCreativeName#1', 3);
INSERT INTO Project VALUES (2, 'superCreativeName#2', 5);
INSERT INTO Project VALUES (3, 'superCreativeName#3', 3);
INSERT INTO Project VALUES (4, 'superCreativeName#4', 4);
INSERT INTO Project VALUES (5, 'superCreativeName#5', 2);

INSERT INTO WorksOn VALUES (5, 3, '12/05/1988', 492);
INSERT INTO WorksOn VALUES (3, 2, '16/01/1992', 228);
INSERT INTO WorksOn VALUES (2, 1, '04/11/1980', 209);
INSERT INTO WorksOn VALUES (2, 5, '28/08/2000', 24);
INSERT INTO WorksOn VALUES (3, 3, '18/12/1987', 260);
