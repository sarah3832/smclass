drop table emp02;
drop table mem2;

select * from mem;

create table emp02(
empno number(4) not null,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);
-- null
insert into emp02 values(
2,'유관순',null,null
);
insert into emp02 values(
3,'이순신',null,null
);

drop table emp02;


create table emp02(
empno number(4) primary key,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp02 values(
1,'홍길동','clerk',2
);
insert into emp02 values(
2,'유관순',null,null
);
insert into emp02 values(
3,'이순신',null,null
);
insert into emp02 values(
null,'강감찬',null,null
);
-- unique : 중복불가(에러)
insert into emp02 values(
2,'김구',null,null
);

select * from emp02;

delete emp02 where empno is null;
commit;

-- alter : 제약조건 변경
alter table emp02 modify empno not null;
alter table emp02 modify empno;

-- not null, pk_emp02_empno 별칭
alter table emp02 add constraint pk_emp02_empno primary key(empno);
alter table emp02 drop constraint pk_emp02_empno;

drop table mem;

-------------------------

create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(100) default '무명',
gender varchar2(6) check (gender in ('Male','Female')) -- 대소문자 구분
);

insert into mem values(
'aaa','1111','홍길동','Male'
);
insert into mem values(
'bbb','1111','유관순','Female'  -- female 에러
);

commit;

create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
id varchar2(30),
constraint fk_board2_id foreign key(id) references mem(id) 
);

select * from mem;

delete mem where id='aaa';

insert into board2 values(
1,'제목1','aaa'
);
insert into board2 values(
2,'제목2','bbb'
);
insert into board2 values(
3,'제목3','aaa'
);
-- 외래키로 등록시 부모키에 해당 값이 없을시 에러
insert into board2 values(
4,'제목4','bbb'
);

-- 외래키 삭제
alter table board2 drop constraint fk_board2_id;

-- 부모키 삭제시, 외래키로 등록된 값들을 모두 삭제
alter table board2 
add constraint fk_board2_id foreign key (id)
references mem(id) on delete cascade;  -- on delete set null
 
-- default : on delete restricted : 부모키 삭제시, 외래키에 등록된 값이 있으면 삭제가 되지않음.
-- on delete set null : 부모키 삭제시, 외래키로 등록된 값을 삭제는 하지않고, 해당되는 컬럼 값만 null

-- 부모테이블의 aaa삭제시, 자식테이블의 aaa글이 모두 삭제
delete mem where id='aaa';

select * from mem;
select * from board2;

------------------------------

drop table mem;
drop table board2;

create table mem(
id varchar2(30) primary key,
pw varchar2(100) not null,
name varchar2(100),
deptno number(4)
);

insert into mem values(
'aaa','1111','홍길동',10
);
insert into mem values(
'bbb','1111','유관순',20
);
insert into mem values(
'ccc','1111','이순신',30
);

commit;

select * from mem;

-- 10 '총무부' / 20 '인사부' / 30 '마케팅'

select id,pw,name,deptno,
decode(deptno,
10,'총무부',
20,'인사부',
30,'마케팅'
)
from mem;

select * from employees;

select job_id from employees;

-- clerk 5%, rep 10%, man 15%
-- 1.clerk,rep,man 사람을 출력하시오.
select substr(job_id,4)j_id, salary,
decode(substr(job_id,4),
'CLERK',salary*1.05,
'REP',salary*1.1,
'MAN',salary*1.15
)sal
from employees where substr(job_id,4) in ('CLERK','REP','MAN');

----------------------------

create table lavel_data (
	id VARCHAR2(50) primary key,
	lavel number(1) not null
);

insert into lavel_data (id, lavel) values ('Arlen', 4);
insert into lavel_data (id, lavel) values ('Catie', 4);
insert into lavel_data (id, lavel) values ('Adoree', 5);
insert into lavel_data (id, lavel) values ('Cher', 4);
insert into lavel_data (id, lavel) values ('Dorita', 5);
insert into lavel_data (id, lavel) values ('Zulema', 1);
insert into lavel_data (id, lavel) values ('Richy', 4);
insert into lavel_data (id, lavel) values ('James', 5);
insert into lavel_data (id, lavel) values ('Aeriel', 5);
insert into lavel_data (id, lavel) values ('Reinald', 3);
insert into lavel_data (id, lavel) values ('Bernardina', 1);
insert into lavel_data (id, lavel) values ('Tiertza', 2);
insert into lavel_data (id, lavel) values ('Carolyne', 5);
insert into lavel_data (id, lavel) values ('Jonis', 1);
insert into lavel_data (id, lavel) values ('Abigael', 5);
insert into lavel_data (id, lavel) values ('Pauli', 4);
insert into lavel_data (id, lavel) values ('Sheffie', 2);
insert into lavel_data (id, lavel) values ('Tully', 2);
insert into lavel_data (id, lavel) values ('Ricard', 5);
insert into lavel_data (id, lavel) values ('Jameson', 3);
insert into lavel_data (id, lavel) values ('Thorstein', 1);
insert into lavel_data (id, lavel) values ('Arlyne', 5);
insert into lavel_data (id, lavel) values ('Mela', 5);
insert into lavel_data (id, lavel) values ('Yetta', 3);
insert into lavel_data (id, lavel) values ('Corilla', 4);
insert into lavel_data (id, lavel) values ('Adoree', 1);
insert into lavel_data (id, lavel) values ('Sabine', 3);
insert into lavel_data (id, lavel) values ('Nelson', 3);
insert into lavel_data (id, lavel) values ('Isahella', 5);
insert into lavel_data (id, lavel) values ('Mandel', 5);
insert into lavel_data (id, lavel) values ('Sasha', 4);
insert into lavel_data (id, lavel) values ('Deanne', 1);
insert into lavel_data (id, lavel) values ('Thorny', 1);
insert into lavel_data (id, lavel) values ('Jacki', 3);
insert into lavel_data (id, lavel) values ('Sibby', 2);
insert into lavel_data (id, lavel) values ('Jack', 2);
insert into lavel_data (id, lavel) values ('Chandra', 2);
insert into lavel_data (id, lavel) values ('Cecilla', 5);
insert into lavel_data (id, lavel) values ('Saunder', 1);
insert into lavel_data (id, lavel) values ('Way', 4);
insert into lavel_data (id, lavel) values ('Velma', 3);
insert into lavel_data (id, lavel) values ('Keelia', 1);
insert into lavel_data (id, lavel) values ('Clay', 4);
insert into lavel_data (id, lavel) values ('Grace', 2);
insert into lavel_data (id, lavel) values ('Maura', 5);
insert into lavel_data (id, lavel) values ('Karolina', 4);
insert into lavel_data (id, lavel) values ('Mal', 5);
insert into lavel_data (id, lavel) values ('Annette', 4);
insert into lavel_data (id, lavel) values ('Issy', 2);
insert into lavel_data (id, lavel) values ('Reid', 2);
insert into lavel_data (id, lavel) values ('Dall', 4);
insert into lavel_data (id, lavel) values ('Sukey', 2);
insert into lavel_data (id, lavel) values ('Etty', 5);
insert into lavel_data (id, lavel) values ('Kendall', 5);
insert into lavel_data (id, lavel) values ('Gibby', 4);
insert into lavel_data (id, lavel) values ('Kylila', 2);
insert into lavel_data (id, lavel) values ('Orelia', 2);
insert into lavel_data (id, lavel) values ('Alexei', 4);
insert into lavel_data (id, lavel) values ('Iorgo', 1);
insert into lavel_data (id, lavel) values ('Clive', 1);
insert into lavel_data (id, lavel) values ('Roger', 1);
insert into lavel_data (id, lavel) values ('Halette', 3);
insert into lavel_data (id, lavel) values ('Clyve', 3);
insert into lavel_data (id, lavel) values ('Peadar', 1);
insert into lavel_data (id, lavel) values ('Mose', 4);
insert into lavel_data (id, lavel) values ('Raimundo', 3);
insert into lavel_data (id, lavel) values ('Glori', 1);
insert into lavel_data (id, lavel) values ('Merrel', 2);
insert into lavel_data (id, lavel) values ('Ulberto', 2);
insert into lavel_data (id, lavel) values ('Bren', 4);
insert into lavel_data (id, lavel) values ('Ker', 2);
insert into lavel_data (id, lavel) values ('Rosalinda', 1);
insert into lavel_data (id, lavel) values ('Delphinia', 5);
insert into lavel_data (id, lavel) values ('Johnette', 3);
insert into lavel_data (id, lavel) values ('Marilyn', 3);
insert into lavel_data (id, lavel) values ('Paddy', 2);
insert into lavel_data (id, lavel) values ('Antony', 3);
insert into lavel_data (id, lavel) values ('Kinna', 5);
insert into lavel_data (id, lavel) values ('Rogers', 5);
insert into lavel_data (id, lavel) values ('Zolly', 5);
insert into lavel_data (id, lavel) values ('Lance', 1);
insert into lavel_data (id, lavel) values ('Carroll', 2);
insert into lavel_data (id, lavel) values ('Geralda', 2);
insert into lavel_data (id, lavel) values ('Riobard', 2);
insert into lavel_data (id, lavel) values ('Sunshine', 4);
insert into lavel_data (id, lavel) values ('Betteanne', 2);
insert into lavel_data (id, lavel) values ('Andrea', 1);
insert into lavel_data (id, lavel) values ('Theresina', 3);
insert into lavel_data (id, lavel) values ('Koenraad', 4);
insert into lavel_data (id, lavel) values ('Eydie', 1);
insert into lavel_data (id, lavel) values ('Karolina', 2);
insert into lavel_data (id, lavel) values ('Sutton', 5);
insert into lavel_data (id, lavel) values ('Ikey', 5);
insert into lavel_data (id, lavel) values ('Ugo', 1);
insert into lavel_data (id, lavel) values ('Mallory', 4);
insert into lavel_data (id, lavel) values ('Mariska', 2);
insert into lavel_data (id, lavel) values ('Edmund', 3);
insert into lavel_data (id, lavel) values ('Twyla', 5);
insert into lavel_data (id, lavel) values ('Laney', 5);
insert into lavel_data (id, lavel) values ('Onida', 4);

commit;

select * from lavel_data;

-- 1:100 포인트, 2:1000 포인트, 3:5000 포인트, 4:10000 포인트, 5:20000 포인트
select id,lavel,
decode(lavel,
1,100, 
2,1000,
3,5000,
4,10000,
5,20000
)||' point' point
from lavel_data;

-- decode : 일치하는 경우에만 사용가능
-- case : decode와 같은 기능이지만, 비교연산자도 사용가능
select id,pw,name,deptno,
case
when deptno = 10 then '총무부'
when deptno = 20 then '인사부'
when deptno = 30 then '마케팅'
end as deptName
from mem;


-- 1,2,3:5000 포인트, 4,5:20000 포인트
select id,lavel,
case 
when lavel >= 1 and lavel <=3 then 5000
when lavel >=4 then 20000
end point
from lavel_data;


select * from students;
-- avg:90점이상 A, 80점이상 B, 70점이상 C, 60점이상 D, 그외 F
-- result 컬럼을 출력
select name,avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end result
from students;

-- 테이블 전체 복사
create table stu as select * from students;

-- 컬럼 추가
select * from stu;

alter table stu add result varchar2(2);

-- result 컬럼에 추가하시오
select name,avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end result
from stu;

update stu set result = (
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
when avg < 60 then 'F'
end);

-- 파이썬에서 if문 구현해서 처리(오라클에서 처리하는게 더나음)

-- rank() over() : 순위를 구현하는 함수
-- rank() over() : 같은 순위일 경우, 중복순위 개수만큼 다음 순값을 증가
select no,name,total,rank() over(order by total desc) from stu order by no;

-- dense_rank() over() : 중복순위가 존재해도 순차적으로 다음순위 표시
select no,name,total,dense_rank() over(order by total desc) re from stu;

-- 순위를 rank컬럼에 추가하시오.
select ranks from(select rank() over(order by total desc)ranks from stu b);

update stu a set rank = (
select ranks from(
select no,rank() over(order by total desc) ranks from stu) b
where b.no = a.no
);

select * from stu;

-- case
-- salary 5000 이하는 월급 15%인상 / 5000~8000 :10% 인상 / 8000이상은 5% 인상
select * from employees;

select emp_name,salary,
case
when salary <= 5000 then salary*1.15
when 5000 < salary and salary < 8000 then salary*1.1
when salary >= 8000 then salary*1.05
end y_salary
from employees;

-- emp_name 대문자 D가 포함되어 있으면 10%인상, M이 포함되어 있으면 5%인상, 그외는 0%인상
select emp_name,salary,
case
when emp_name like '%D%' then salary*1.1
when emp_name like '%M%' then salary*1.05
else salary
end y_salary
from employees;


select * from employees;

select department_id,commission_pct from employees
where commission_pct is not null;

-- 커미션이 있는 사원수를 출력하시오.
select count(*) from employees
where commission_pct is not null;

-- 부서별 사원수를 출력하시오.
select department_id,count(*) from employees
group by department_id order by department_id;

-- 부서별 평균 월급을 출력하시오.
select department_id,avg(salary) from employees
group by department_id;

-- having : 그룹함수 비교연산
-- 부서별 평균월급이 7000보다 높은 사람의 인원수를 출력하시오.
select department_id,avg(salary),count(salary) from employees
group by department_id
having avg(salary) >= 7000;

-- 전체 평균월급보다 적게받는 부서별 사원수를 출력하시오.
select avg(salary) from employees
group by department_id;

select department_id,count(*) from employees
where salary < (select avg(salary) from employees)
group by department_id;

- 13000,6000
select salary from employees where department_id = 20;

-- 그룹함수는 having절에 조건문을 사용
-- 부서별 평균 월급이 6000이하인 부서별 인원수를 출력하시오.
select department_id,avg(salary),count(salary) from employees
group by department_id
having avg(salary) > 6000;

-- 부서번호, 부서별 평균월급
select department_id,avg(salary) from employees
group by department_id;

-- 부서번호, 개인별 월급, 인원
select department_id,salary,count(*) from employees
group by depa rtment_id,salary;


-- 부서별 평균 월급보다 적게받는 사원수
select department_id,count(salary) from employees
group by department_id
having salary < avg(salary) ;

-- 부서별 평균 월급보다 적게받는 사원
select department_id,emp_name,salary from employees a
where salary < 
(
select salarys from(
select department_id,avg(salary) salarys from employees
group by department_id 
) b
where a.department_id = b.department_id
);

-- 부서별 평균 월급보다 적게받는 사원 수
select department_id,count(*) from employees a
where salary < 
(
select salarys from(
select department_id,avg(salary) salarys from employees
group by department_id 
) b
where a.department_id = b.department_id
)
group by department_id
order by department_id;


select department_id, emp_name, salary from employees
where department_id = 30;

select avg(salary) from employees
where department_id = 30;

-- 부서의 최대급여와 최소급여를 출력하되, 최대급여가 5000이상인 부서만 출력하시오.
select department_id,max(salary),min(salary) from employees
group by department_id
having max(salary) >= 5000
order by department_id desc;

-------------------------------

-- 학번,이름,전화번호,주소,성별,학년,학기,국어,영어,수학,합계,등수
-- 1001,홍길동,010,서울,남자,1,1,100,100,100,300,1
-- 1001,홍길동,010,서울,남자,1,2,90,90,90,270,8
-- 1001,홍길동,010,서울,남자,1,3,95,95,95,285,15
-- 1001,홍길동,010,서울,남자,1,4,100,100,99,299,2
-- 1001,홍길동,010,서울,남자,2,1,100,100,100,300,1
-- 1001,홍길동,010,서울,남자,2,2,90,90,90,270,8
-- 1001,홍길동,010,서울,남자,2,3,95,95,95,285,15
-- 1001,홍길동,010,서울,남자,2,4,100,100,99,299,2

-- 부서명 departments
select * from departments;

select * from employees;

-- Donald OConnell 의 부서명을 알고싶어요.
select emp_name,department_id from employees
where emp_name = 'Donald OConnell';

select department_id,department_name from departments 
where department_id = 50;

-- join을 사용해야 두개의 쿼리를 1개의 쿼리로 구성이 가능.

-- join
-- 1. cross join
-- 1-1. inner join (equi join, non-equi join)
-- 3. outer join
-- 4. self join

-- cross join : 특별한 키워드없이, 두개의 테이블을 검색한는 것
select * from employees;  -- 107
select * from departments;  -- 107*27 = 2889

select count(*) from employees,departments;  -- 2889
select * from employees,departments;

-- inner join - equi join : 같은 컬럼을 가지고 비교해서 두개의 테이블을 검색
select emp_name,a.department_id,department_name from employees a,departments b
where a.department_id = b.department_id;  -- outer join :(+)쓰는것

select * from member;
select bno,btitle,bcontent,id from board;

select bno,btitle,bcontent,a.id,email,phone,bgroup,bstep,bindent,bhit,bdate,bfile 
from member a,board b
where a.id = b.id;

select * from jobs;
select * from employees;
select * from departments;

-- inner join : 사원번호, 사원명, job_id, job_title 출력
select employee_id,emp_name,a.job_id,job_title
from employees a, jobs b
where a.job_id = b.job_id and a.job_id = 'SH_CLERK';


-- 사원번호, 사원명, 부서번호, 부서명, job_id, job_title 출력하시오.
select employee_id,emp_name,c.department_id,department_name,a.job_id,job_title
from employees a, jobs b, departments c
where a.job_id = b.job_id and a.department_id = c.department_id;

-- member 이름
-- board 게시글
select * from board;
select * from member;

select bno,btitle,bcontent,a.name,bgroup,bstep,bindent,bhit,bdate,bfile
from member a,board b
where a.id = b.id;


-- 사원번호, 사원명, 월급, 부서번호, 부서명
-- 월급이 평균 월급보다 적은 사원을 출력하시오.
select * from employees;
select * from departments;

select employee_id, emp_name, salary,a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
and salary < (select avg(salary) from employees);


-- 사원번호, 사원명, 월급, 부서번호, 부서명
-- 부서별 평균 월급보다 작은 사원을 출력하시오.
select employee_id, emp_name, salary,a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
and salary < ( 
select salarys from(select department_id,avg(salary) salarys from employees
group by department_id)c
where a.department_id = c.department_id
);

--------------------------
select * from jobs;
select * from departments;
select * from employees;

-- job_id가 CLERK인 사원명, 사원번호, 부서명, 부서번호, 직급번호, 직급명 출력하시오.
select emp_name, employee_id, department_name, b.department_id, a.job_id, job_title
from jobs a,departments b, employees c
where b.department_id = c.department_id and a.job_id = c.job_id
and substr(a.job_id,4) in ('CLERK','MAN');

select * from employees;


select salary from employees order by salary;

--------------------------

-- 2000~4000 E, 4000~6000 D, 6000~8000 C, 8000~10000 B, 10000~100000 A
create table salgrade(
grade varchar2(10),
losal number(6),
hisal number(6)
);

insert into salgrade values(
'E등급',2000,4000
);
insert into salgrade values(
'D등급',4001,6000
);
insert into salgrade values(
'C등급',6001,8000
);
insert into salgrade values(
'B등급',8001,10000
);
insert into salgrade values(
'A등급',10001,100000
);

select * from salgrade;

-- salary 옆에 등급을 넣으려고 함
-- 등급 : salgrade
-- salgrade, employees 같은 컬럼이 없음.
-- non-equi join 사용해서 테이블을 join
select salary from employees;
select * from salgrade;

-- non-equi join : 두 테이블간 같은 컬럼이 없으면서, 두 테이블의 값을 비교해서 출력
select emp_name, salary, grade 
from employees, salgrade  -- 107*5 = 535 
where salary between losal and hisal;

-- non-equi join 활용해서 students avg a,b,c,d,f 등급을 출력
-- 100~90, 89~80, 79~70, 69~60, 60미만
-- 테이블명 : stu_grade / grade,lototal,hitotal

select name,total,avg,grade
from students,stu_grade
where avg between loavg and hiavg;

create table stu_grade(
grade varchar2(10),  -- A등급
loavg number(5,2),  -- 59.99
hiavg number(5,2)
);
select * from stu_grade;
--drop table stu_grade;

insert into stu_grade values('A등급',90,100);
insert into stu_grade values('B등급',80,89.99);
insert into stu_grade values('C등급',70,79.99);
insert into stu_grade values('D등급',60,69.99);
insert into stu_grade values('E등급',0,59.99);

commit;

select * from stu;
update stu set result = '';

-- result 결과값을 non-equi join을 사용해서 입력하시오.
update stu a set result = (
select results from(
select no,grade as results
from stu, stu_grade
where avg between loavg and hiavg) b
where a.no = b.no
);

select name,total,avg,result from stu;
commit;

--rollback;

select name,total,avg,grade
from stu, stu_grade
where avg between loavg and hiavg;


alter table stu modify result varchar2(20);
-- A등급
alter table stu modify result varchar2(10);

-----------------------

-- self join
select employee_id,emp_name,manager_id from employees;

select employee_id, emp_name from employees
where employee_id = 124;

-- self join : 자신의 테이블 2개를 join해서 결과값을 출력
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id and a.manager_id = 124;