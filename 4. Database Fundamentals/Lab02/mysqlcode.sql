##############################################
# 	Name  : Ahmed Sharaf 					 #
# 	Lab02 : DB MySql						 #
#	Date  : 13-11-2025						 #
##############################################

use os44_db;
 /* ############################################## 	DQL ############################################## */

/* 1.	Display the employee First name, last name, Salary and Department number in department 30 whose salary from 1000 to 2000 LE monthly */

select Fname, Lname, Salary, Dno from employee where Dno = 30 and Salary between 1000 and 2000;

/* 2.	Display all the projects names, locations and the department number which is managed by it. */

select Pname, Plocation, Dnum
from Project;

/* 
3.	If you know that the company policy is to pay an annual commission for each employee which specific percent equals 10% of his/her annual salary .
Display each employee full name and his annual commission in an ANNUAL COMM column (alias).
*/

select concat(Fname, ' ', Lname) As "Full Name", Salary*12*0.1 as ANNUAL_COMM
from employee;

/* 4.	Display the employees Id, fname who earns more than 10000 LE annually. */

select SSN, Fname
from employee
where  (Salary*12) > 10000;

/* 5.	Display the names and salaries of the female employees */

select concat(Fname, ' ', Lname) As "Full Name", Salary
from employee
where lower(gender) in ('f', 'female');

/* 6.	Display each department id, name which managed by a manager with id equals 968574. */

select Dname, Dnum
from departments
where MGRSSN = 968574;

/* 7.	Display the project id, name and location of  the projects which controlled with department 10 or 20, 
and location of the projects in Cairo or Alex city */

select Pnumber, Pname, Plocation
from project
where (Dnum = 10 or Dnum = 20) and City in ("Alex", "Cairo");

/* 8.	Display the Projects name, locations of the projects with a name starts with "a" letter. */

select Pname, Plocation
from project 
where Pname Like "a%";

/* 
9.	Display the department number and maximum of salary in each department 
Display only departments that has employees, and has number of employees greater to or equal 2 employees
*/

select Dno, max(Salary)
from employee
group by Dno
having count(SSN) >= 2;


 /* ############################################## 	DML ############################################## */
 
 /*
 1.	Insert new employee with your personal data, you will be in department number 30, your SSN = 666666 , salary = 1000 & Superssn = 112233.
 */
 
insert into employee(Dno, SSN, Salary, Superssn)
values (30, 666666, 1000, 112233);

select *
from employee
where SSN = 666666;

/*
2.	Insert another employee with personal data your friend as new employee in department number 30 , SSN = 555555, 
but don’t enter any value for salary or supervisor number of him.
*/

insert into employee(Dno, SSN)
value (30, 555555);

select *
from employee
where SSN = 555555;

/* 
3.	In the department table insert new department called "DEPT IT", with id 100, MgrSSN = 112233 as a manager for this department. 
The start date for this manager is '1/11/2006'
*/

insert into departments
values ("DEPT IT", 100, 112233, "2006-01-11");

select *
from departments
where Dnum = 100;

/*
4.	Do what is required if you know that : Mrs.Noha Mohamed moved to be the manager of the new department (id = 100), 
and they give her position to your friend
 
	100 -> Mrs. Noha Mohmed (SSN = 968574)
    20  -> Mrs. Mariam Adel (SSN = 669955)
    SSN OF (669955) superssn is equal 111111
*/

update departments
set MGRSSN = 669955, MGRStart = '2025-11-13'
where Dnum = 20;

update departments
set MGRSSN = 968574, MGRStart = '2025-11-13'
where Dnum = 100;

insert into employee(Fname, Lname, SSN, gender, Salary)
values ("Ahmed", "Sharaf", 111111, "M", 10000);

update employee
set Superssn = 111111
where SSN = 669955;

select *
from departments
where Dnum = 20 or Dnum = 100;

select *
from employee
where SSN = 669955;


/*
5.	Unfortunately the company ended the contract with Mr.Kamel Mohamed so try to delete his data from your database, 
in case you need, you can be temporary in his position.

Upgrade your salary by 20 percent of its last value.
*/

/* Ineed To Take This Poistion Manager Dnum 10 */

update departments
set MGRSSN = 111111, MGRStart = '2025-11-13'
where Dnum = 10;

/* Ineed To Take all Projects he working it */

update works_for
set ESSn = 111111
where ESSn = 223344;

/* Delete dependent */

delete from dependent
where ESSn = 223344;

/* Must Supervision of employee he is suppervised*/

update employee
set Superssn = 111111
where Superssn = 223344;

/* Delete Info Aboue Mr. Kamel*/

delete from employee
where SSN = 223344;

/* Update My Salary */

update employee
set Salary = Salary + (Salary * 0.2)
where SSN = 111111;

