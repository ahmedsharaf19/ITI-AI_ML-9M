##############################################
# 	Name  : Ahmed Sharaf 					 #
# 	Lab03 : DB MySql						 #
#	Date  : 16-11-2025						 #
##############################################
use os44_db;

/*
1.	Display the Department id, name and its manager id and the name of its manager.
*/
select Dnum, Dname, MGRSSN, concat(Fname, ' ', Lname) as "Full Name"
from departments dep, employee e
where dep.MGRSSN = e.SSN;

/*
2. Display the departments’ name and the project name of the under their control.
*/
select Dname, Pname
from project p, departments d
where p.Dnum = d.Dnum;

/*
3.	Display the dependent name for all the dependence and the name of the employee they depend on him/her.
*/
select dependent_name, concat(Fname, ' ', Lname) as "Full Name"
from dependent d, employee e
where d.ESSn = e.SSN;

/*
4.	Retrieve the fname, pname of all employees work in department 10 
who works more than or equal 10 hours per week on ‘AL Rabwah’ project.
*/
select e.Fname, p.Pname
from employee e, works_for w, project p
where w.ESSn = e.SSN and W.pno = p.Pnumber and  dno = 10 and p.Pname = "AL Rabwah"and w.Hours >= 10;

/*
5.	Find the fname of the employees who directly supervised with ‘Kamel Mohamed’.
*/
select Fname
from employee
where Superssn = (select SSN
				from employee
				where concat(Fname, ' ', Lname) = "Kamel Mohamed");
                
/*
6.	List the last name of all managers who have no dependents.
*/
select Lname
from departments d, employee e
where d.MGRSSN = e.SSN and SSN not in (select ESSN from dependent);

/* 
7.	Display the department name which has the smallest employee ID over all employees' ID.
*/
select Dname
from employee e, departments d
where e.Dno = d.Dnum and SSN = (select Min(SSN) from employee);

/*
8.	For each department, retrieve the department name and the maximum, minimum and average salary of its employees.
*/
select Dname, Max(Salary) as Max, Min(Salary) as Min, avg(Salary) as Average
from departments d, employee e
where d.Dnum = e.Dno
group by Dname;

/*
9.	For each department >>> display department number, department name and number of its employees 
-- if its average salary is less than 1200
*/
select Dnum, Dname, count(SSN)
from employee e, departments d
where e.Dno = d.Dnum
group by Dnum, Dname
having avg(Salary) < 1200;

/*
10.	Retrieve a list of employees (fname) and the projects (project name) they are working on 
ordered by department no, last name, first name.
*/
select e.fname, p.pname
from employee e, works_for w, project p
where e.SSN = w.ESSn and w.pno = p.Pnumber
order by Dnum, Lname, Fname;

/*
11.	Find the project number, the controlling department name, 
the department manager last name, address and birthdate. For each project located in ‘Cairo’ City
*/
select Pnumber, Dname, Lname, Address, Bdate
from project p, departments d, employee e
where p.Dnum = d.Dnum and d.MGRSSN = e.SSN and City = 'Cairo';

