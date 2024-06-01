# Write your MySQL query statement below
#self join Concept
select empName as Employee From
(
    select 
e1.id as empid,
e2.name as empName,
e1.salary as empSalary,
e2.managerId as managerId,
e2.salary as managerSalary
from Employee e1 right join Employee e2
on  e2.managerid=e1.id
where
e2.salary>e1.salary
)
as t1


