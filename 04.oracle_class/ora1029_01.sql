-- f9 = 컨트롤 enter
-- drop은 사용 후, 주석처리
--drop table member;
--drop table date_tab;
--drop table no_tab;
--drop table students;

-- create : 테이블 생성 / alter : 테이블 수정 / drop : 테이블 삭제
create table member(
 no number(4),
 id varchar2(20),
 pw varchar2(20),
 name varchar2(20),
 phone varchar2(20),
 mdate date
);

-- insert : 데이터 입력 (''로 분리), 임시저장소에 저장
insert into member values(
 1,'aaa','1111','홍길동','010-1111-1111','2024-10-29'
);

insert into member values(
2,'bbb','1111','유관순','010-2222-2222','2024-09-20'
);

-- select : 데이터 검색 / update : 데이터 수정 / delete : 데이터 삭제
select * from member;

-- commit : 임시저장소에 있던 데이터가 원본에 저장이 됨.
commit;
-- rollback : 다시 되돌아감
rollback;

-- delete : 삭제 ( 사용 후, 주석처리)
--delete member where no=2;
--delete member;

-- update : 수정
update member set name='홍길자' where no=1;
update member set name='김구'; -- where절이 없으면 전부다 바뀜

select * from member;


-- create 테이블 생성
create table students(
stuno number(4),
name varchar(20),
kor number(3),
eng number(3),
total number(3),
sdate date
);

-- sysdate : 현재날짜, 시간 저장
insert into students values(
1,'홍길동',100,100,100+100,sysdate
);

commit;

-- * : 모든 컬럼 검색
select * from students;

-- 특정컬럼을 입력하면, 컬럼만 보여줌.
select name, date from students

-- 특정컬럼만 입력하면, 컬럼 입력
insert into students (stuno,name) values(
2,'유관순'
);



-------------
select * from employees;
select count(*) from employees;

-------------
-- 테이블을 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;
select * from emp2;
select count(*) from emp2;  -- count : 데이터 개수

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1=2;
select * from emp3;

-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1=2;
insert into member2 select * from member;

-- 테이블 컬럼
-- 컬럼데이터 타입의 길이 변경
-- alter변경 member테이블 no컬럼의 타입길이를 변경
alter table member modify no number(10);

-- alter변경, 컬럼의 이름을 변경
alter table member rename column no to memberNo;
desc member;

-- 대소문자 구분x
--SELECT * FROM MEMBER;
--select * from member;
--select memberno from member;
--SELECT MEMBERNO FROM MEMBER;
--SELECT memberNo from member;
select * from member;
select * from member where id='aaa';  -- 가능
--SELECT * FROM MEMBER WHERE ID='AAA';  -- 내용부분은 대소문자 구분해야함.


-- 다른 타입으로 변경시
update member set no = '';
select * from member;
commit;
alter table member modify no varchar2(10);

select * from member;
desc  member;

-- 테이블 구조
desc employees; 


-- employees 테이블에서 사원번호(employee_id), 사원이름(emp_name), 입사일hire_date
select employee_id,emp_name,hire_date from employees; 
select * from employees;


create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);

select * from member;



create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);

select * from students;
commit;


-- 연산자 : 산술연산자 : +,-,*,/
select kor,eng,(kor+eng) from students;
select kor,eng,(kor+eng),abs(kor-eng) from students;

select * from employees;

-- 문자 더하기 불가능
--select emp_name+email from employees;  -- 불가능

-- concat 명령어, ||
select concat(employee_id,emp_name) from employees;
select employee_id || emp_name from employees;

-- 달러환산 *1384
select salary from employees;
select salary*1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary*1384,'999,999,999') from employees;

select emp_name,salary,salary*1384 from employees;


-- null : 무한대의 의미(미확정, 알수없는 값 의미) / 연산,할당,비교 불가 / 빈공백 아님
create table stu(
no number(4),
name varchar2(20),
kor number(3)
);

insert into stu values(1,'홍길동',100);
insert into stu values(2,'유관순',99);

commit;

insert into stu values(3,'',0);
insert into stu values(4,null,null);

select * from stu;


--select * from stu where name = '';  -- null은 빈공백이 아님
-- null값 검색 : is null
select * from stu where name is null;

-- nul이 아닌 것 출력 : is not null
select commission_pct from employees where commission_pct is not null;

select salary from employees;
-- 연봉계산 * 12
select salary, salary*12 from employess;
select salary,salary*12,salary*12*1384 from employess;

-- 커미션이 없는 사람은 null값이 있는데, null +,-,*,/ null값으로 변경
select salary,salary*12,salary*12+(salary*12)*commission_pct*0.01 from employees;

-- 컬럼명 별칭 사용 : as (" " 넣으면 특수문자, 사이공간까지 있는그대로 컬럼명 사용가능)
select salary,salary*12 as 년봉,salary*12+(salary*12)*nvl(commission_pct,0)*0.01 as "r e a l_yearSalary" from employees;

-- nvl() 함수 : nvl(kor,0) - kor컬럼에 null값이 있으면 0으로 표시
select * from stu;
select no,name,kor,kor+100 from stu;
select no,name,kor,nvl(kor,0)+100 from stu;
 

-- 번호,이름,국어,영어,수학,합계,평균,등수,입력일 컬럼명 별칭을 사용해서 출력하시오.
-- as는 생략가능
select * from students;
select no as 번호,name as 이름,kor as 국어,eng as 영어,math as 수학,total 합계,avg 평균,rank 등수,sdate 입력일 from students;


-- 사원번호,이름,이메일을 합쳐서 출력하시오.
select * from employees;
select employee_id || emp_name || email from employees;
-- concat은 두개까지만 더하기 가능, 더 할려면 concat 또 사용.
select concat(concat(employee_id,emp_name),email) from employees;
select emp_name || 'is a' || job_id from employees;  -- 문자 추가

-- 중복제거 : distinct
select department_id from employees;
select distinct department_id from employees;

-- 순차정렬 : order by / order by + asc(생략가능) / 역순정렬 : order by + desc
select distinct department_id from employees order by department_id desc;


-- job_id 중복을 제거해서 출력하시오.
select distinct job_id from employees;
select job_id from employees;

-- 문자열 자르기 : substr / (0,1) : 2 앞까지 출력
select substr(job_id,0,2) from employees;

-- 4번째 컬럼데이터를 가져와서 중복을 제거
select distinct substr(job_id,4) from employees; -- 끝까지면 뒤에범위x


-- where절 : 조건에 대한 비교연산자 (>,<,>=,<=,=,!=)
select * from employees;
select * from employees where manager_id != 124;
select * from employees where job_id = 'SH_CLERK';
select * from employees where employee_id > 100;  

-- students에서 합계가 250이상만 출력하시오.
select * from students;
select * from students where total >= 250;

-- 합계가 250이상이면서, kor점수가 90점 이상만 출력하시오.
select * from students where total >= 250 and kor >= 90;

-- 영어점수 70이상, 90이하 출력하시오.
select * from students where eng >= 70 and eng <= 90;

-- employees에서 월급이 5000이상, 8000이하 출력하시오.
select * from employees where salary >= 5000 and salary <= 8000;

-- 연산자 우선순위 : 1.(+,-,*,/) 2.(||) 3. 비교연산자

-- 월급이 7000이 아닌것을 모두 출력하시오.
-- 아닌것 : !=, <>, ^=
select * from employees where salary != 7000;
select * from employees where salary <> 7000;
select * from employees where salary ^= 7000;

-- 부서(department_id) 50번 인것만 개수 출력하시오.
-- count : 개수 확인
select count(*) from employees where department_id = 50;
-- 50번 아닌것 개수 출력하시오.
select count(*) from employees where department_id != 50;
-- null값은 count() 포함되지 않음
select count(*) from employees where department_id is null;
select count(employee_id) from employees;  -- 107개
select count(department_id) from employees;  -- 106개 (null값이 1개있어서 106개)

-- 급여 4000이하인 사원번호, 사원명, 급여 컬럼만 출력하시오.
select employee_id 사원번호,emp_name 사원명,salary 급여 from employees where salary <= 4000;
select * from employees;

-- 숫자 비교연산자 가능 / 날짜도 비교연산자 가능
select emp_name,hire_date from employees;
select emp_name,hire_date from employees where hire_date >= '2002/01/01';

-- 1999/12/31 이전에 입사한 사람을 출력하시오.
select emp_name,hire_date from employees where hire_date <= '1999/12/31';

-- 2001/01/01 부터 2004/12/31 까지 출력하시오.
-- 날짜는 '-','','/' 다 가능
select emp_name,hire_date from employees where hire_date >= '20010101' and hire_date <= '2004-12-31';



-- 논리연산자 : and, or, not
-- 국어점수 90점이상 또는 영어점수 90점이상 출력하시오.
select count(*) from students where kor >= 90 or eng >= 90;  -- 41개
select count(*) from students where kor >= 90 and eng >= 90; -- 3개
select count(*) from students where not kor >= 90;


-- 부서번호 80번(department_id)이면서 job_id가 MAN 경우
select * from employees;
select * from employees where department_id = 80 and substr(job_id,4) = 'MAN';
select * from employees where department_id = 80 and job_id = 'SA_MAN';

-- 0.2, 0.3, 0.5
select commission_pct from employees where commission_pct is not null;
-- or 연산자 사용
select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;
-- in 연산자 사용
select commission_pct from employees where commission_pct in (0.2,0.3,0.5);


-- 사원번호(employee_id)가 110,120,130
select * from employees where employee_id in (110,120,130);  -- in 사용
select * from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;  -- or 사용


-- 150~170 사원번호 출력
select * from employees where employee_id >= 150 and employee_id <= 170;
-- between - and : <= 포함이 되어 있는 경우만 해당
select * from employees where employee_id between 150 and 170;


-- 날짜 in
select hire_date from employees where hire_date in ('2004/02/17','2002/06/07');
-- 날짜 between
select hire_date from employees where hire_date between '2002/06/17' and '2004/12/31';


-- job에 MAN 출력하시오
select * from employees where substr(job_id,4) = 'MAN';

-- like연산자 : 포함되어 있는 글자 검색
select * from employees where job_id like '%MAN';  -- MAN으로 끝나는 단어검색
select * from employees where job_id like 'ST%';  -- ST로 시작하되는 단어검색

-- emp_name 에서 a가 들어가있는 이름을 출력
select * from employees where emp_name not like '%a%';  -- % 양쪽에 넣으면 포함된 모두검색


-- 2번째 자리에 t가 들어가있는 이름 출력
select * from employees where emp_name like '_t%';  -- 빈공간은 (_) 
-- 4번째 v가 들어가있는 이름 출력
select * from employees where emp_name like '___v%';
-- 뒤에서 2번째 자리에 l이 들어가있는 이름 출력
select * from employees where emp_name like '%l_';
-- 첫번째에 대문자D 들어가있는 이름 출력
select * from employees where emp_name like 'D%';
