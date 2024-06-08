# Write your MySQL query statement below
with maxNameTab as(
    with maxTab as (
select MAX(salary) as msal ,departmentId from Employee
group by departmentId
)

select name,salary,m.departmentId from maxTab m left join Employee e
on m.msal=e.salary and m.departmentId=e.departmentId


)

select d.name as Department,m.name as Employee,Salary from maxNameTab m left join department d
on m.departmentId=d.id


