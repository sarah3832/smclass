select * from member;

--update member set id='abc',pw='1111',name='유니',email='sarah3832@naver.com' where id='Trineman;

update member set id='abc', pw='1111',name='유니',email='sarah3832@naver.com' where id ='Trineman';
update member set pw='1111' where id='Towell';
update member set pw='1111' where id='abc';

commit;

----------------------

select sysdate-1,sysdate,sysdate+1 from dual;

select hire_date,round(hire_date,'Month') from employees;  -- 월 기준으로 15이상 올림,이하는 내림

select hire_date,trunc(hire_date,'month') from employees;  -- 월 기준으로 무조건 버림

select trunc(sysdate,'month') from dual;

select add_months(trunc(sysdate,'month'),1) from dual;

-- vip요금제로 변경을 하면 다음달 1일부터 혜택
select sysdate,add_months(trunc(sysdate,'month'),1)혜택일 from dual;  -- 1달후 1일

-- 입사일 기준 다음달 1일부터 혜택
select hire_date 입사일,add_months(trunc(hire_date,'month'),1) 혜택일 from employees;

-- 입사일 기준 1년이 지난날짜 출력
select hire_date 입사일,add_months(hire_date,12) from employees;
select hire_date,hire_date+365 from employees;


select hire_date, last_day(hire_date) from employees;  -- 달의 마지막날 출력

-- 입사일 기준 1년후 날짜, 1년후 마지막 그달의 날짜 출력
select hire_date 입사일,hire_date+365 다음해,last_day(hire_date+365)다음해마지막날짜 from employees; 

-----------------------------

select sdate from students
where sdate ='24/01/19';

select sdate from students;

-- 입력일 기준, 1년후 마지막 날짜 24,25년 8/31,9/30,10/31인 학생들을 모두 출력하시오.
select name,sdate,last_day(sdate+365) sdate2 from students
where last_day(sdate+365) in ('24/08/31','24/09/30','24/10/31','25/08/31','25/09/30','25/10/31') order by sdate2;

select sdate,extract(month from sdate) from students 
where extract(month from last_day(sdate+365)) in (8,11,12); 


-- extract함수 : 년,월,일,시,분,초만 분리해서 가져오는 함수
-- sysdate : 년,월,일 까지만 분리 가능
select sysdate from dual;
select extract(year from sysdate) from dual;  -- 년도
select extract(month from sysdate) from dual;  -- 달
select extract(day from sysdate) from dual;  -- 일

-- systimestamp : 년,월,일,시,분,초 분리 가능
select systimestamp from dual;
select extract(hour from systimestamp) from dual;  --  시간
select extract(minute from systimestamp) from dual;  -- 분
select extract(second from systimestamp) from dual;  -- 초

-- substr함수 : 문자에서 (시작위치, 가져올 개수)
select sysdate,substr(sysdate,4,2) from dual;

select sdate,last_day(sdate+365)sdate2 from students
where substr(last_day(sdate+365),4,2) in (8,11,12)
order by sdate2;

----------------------

-- to_char : 날짜 -> 문자       # 날짜포맷
-- to_char : 숫자 -> 문자       # 천단위, 숫자앞에 0을표시, 통화표시
-- to_date : 문자 -> 날짜       # 날짜 사칙연산
-- to_number : 문자 -> 숫자     # 천단위 표시 , 천단위 삭제해서 사칙연산

-- 날짜 형변환해서 날짜포맷을 변경
-- date타입 -> char타입으로 변경해서 포맷
select sysdate from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd') from dual;
select sysdate,to_char(sysdate,'yyyy-mm-dd-hh24:mi:ss day') from dual;  -- day:목요일
select sysdate,to_char(sysdate,'yy-mm-dd am hh:mi:ss dy') from dual;  -- dy:목 / am,pm 추가가능
select sysdate,to_char(sysdate,'yy-Mon-dd-hh24:mi:ss') from dual;  -- Mon:10월

select hire_date,to_char(hire_date,'yyyy-mm-dd hh:mi:ss') from employees;

-- students테이블 sdate 2024/01/01 포맷 바꿔서 출력
select sdate,to_char(sdate,'yyyy/mm/dd') from students;

select kor from students where kor=70;


-- 숫자타입 -> 문자타입 변경해서 포맷 천단위 표시
select salary*1382.86*12 from employees;

-- 자릿수 채우기 (9 : 빈공백으로 채움 / 0 : 0으로 채움)
-- L : 국가통화기호 표시 / $ : 달러 표시
select to_char(salary*1382.86*12,'L000,999,999') from employees;

select to_char(1,'000') from dual;  -- 001
select 1 from dual;  -- 1

select to_char(123456,'000000000'), to_char(123456,'999,999,999') from dual;

create table chartable2(
no number(4),
kor number(10),
kor_char number(10),
kor_mark number(10)
);

insert into chartable2 values(
3,3000000,3000000,3000000
);

-- 숫자형타입은 숫자앞에 0 있어도 표시가 되지않음.(문자형타입만 가능)
-- , : 천단위 표시는 숫자형타입에 입력이 안됨 (문자형타입만 가능)
insert into chartable2 values(
4,4000000,004000000                                                                                                                          ,004000000
);

rollback;

select * from chartable2;

commit;

-- number,number,str-number 타입을 넣어도 입력
-- 문자형타입에는 숫자형타입 가능
insert into chartable values(
1,10000,to_char(10000,'00000000'),to_char(10000,'0,000,000')
);

select * from chartable;

-- 숫자형타입 + 문자(숫자형)타입 = 두타입 결과값 출력됨.
-- 숫자형타입, 문자형(숫자)타입은 사칙연산 가능
select kor+kor_char from chartable;
-- 숫자형타입과 문자 천단위 표시 숫자타입은 사칙연산 불가능 / 천단위 표시: 문자형타입
select kor+kor_mark from chartable;

desc chartable;  -- number, varchar2
desc chartable2;  -- 모든타입 number

insert into chartable values(
1,10000,10000,10000
);

select * from chartable;

-- 2일 이후의 날짜를 출력하시오.
select '20241031' from dual;
select sysdate,to_date('20241031')+2 이틀뒤 from  dual; 


select to_date(20231031)from dual;

-- 숫자형 타입 -> 날짜형 타입
select sysdate - to_date(20231101) from dual;
-- 문자형 타입 -> 날짜형 타입
select sysdate - to_date('20231101') from dual;

-- 문자형 타입 -> 숫자형 타입
-- 천단위 문자형타입 -> 천단위 제외 숫자형타입
select to_number('20,000','999,999') from dual;

select * from chartable;

-- 천단위 문자형타입 -> 숫자형타입
select kor,to_number(kor_mark,'999,999,999') from chartable;

-- 숫자형타입 이기에 사칙연산 가능
select kor+to_number(kor_mark,'999,999,999') from chartable;


----------------

select department_id from employees;

select department_id from employees
where department_id is null;

select commission_pct from employees
where commission_pct is not null;

desc employees;
-- 월급*커미션을 계산하시오.
select salary+salary*nvl(commission_pct,0) from employees;

-- null 경우 : 0표시
select nvl(department_id,0)from employees;
-- null 경우 : CEO표시, 숫자형 -> 문자형
select nvl(to_char(department_id),'CEO') from employees;

--------------------

-- 그룹 함수
-- sum: 합계 / avg: 평균 / count: 개수 / min: 최소값 / max: 최대값 / median: 중간값

select salary from employees;

select sum(salary) from employees;
select to_char(sum(salary),'999,999') from employees;

select avg(salary) from employees;
-- 소수점 4자리 반올림
select round(avg(salary),4) from employees;
-- 소수점 4자리 내림
select trunc(avg(salary),4) from employees;
-- 최대값,최소값
select max(salary) from employees;
select min(salary) from employees;

-- 평균값보다 월급이 높은 사원을 출력하시오.
select avg(salary) from employees;
select salary from employees where salary > 6461.83;

-- 평균값을 select해서 입력함.
select count(salary) from employees
where salary >= (select avg(salary) from employees);

-- emp name : 단일함수 / avg : 그룹함수 , 같이 쓸수없음(에러)
select emp_name,avg(salary) from employees;
-- 단일함수, 그룹함수 함께사용x
select department_id, max(salary) from employees;


-- students테이블 모든 학생의 kor점수 합계,평균,최대값,최소값을 구하시오.
select kor from students;
select sum(kor),avg(kor),max(kor),min(kor),median(kor) from students;

-- 부서번호가 50인 사원들의 월급의 합,평균,최대값,최소값
select * from employees;

select sum(salary),avg(salary),max(salary),min(salary) from employees 
where department_id = 50;

-- 부서번호 30
select sum(salary),avg(salary),max(salary),min(salary) from employees 
where department_id = 30;
select sum(salary),avg(salary),max(salary),min(salary) from employees 
where department_id = 10;

-- group by : 단일함수, 그룹함수 같이 사용가능
select department_id,round(avg(salary)),count(salary)
,max(salary),min(salary) from employees
group by department_id order by department_id;

select emp_name,salary from employees;

-- 107명의 평균
select avg(salary) from employees;
select department_id, avg(salary) from employees group by department_id;

-- 평균 월급보다 높은사람 수를 출력하시오.
select count(salary),min(salary),max(salary) from employees
where salary >= (select avg(salary) from employees);

-----------------
-- 수학함수
-- abs:절대값 / ceil:올림 / floor:버림 / round:반올림 / trunc:절사 / mod:나머지 / power:제곱 / sqrt:제곱근

-- 제곱
select power(3,3) from dual;  -- 3의3승 (3*3*3)

-- 문자,숫자형타입 -> 날짜형타입 변경가능
-- 숫자,날짜형타입 -> 문자형타입 변경가능
-- 문자형타입 -> 숫자형타입 변경가능
-- 날짜형타입 -> 숫자형타입 변경 불가능 / 형태를 변경해서 문자형으로 변경 후, 숫자형으로 변경가능
select 20240101,to_date(20240101) from dual;
select '2',to_number('2') from dual;

select '20240101',to_number('20240101') from dual;
select to_date('20240101') from dual;

select sysdate to_number(sysdate) from dual;  -- 불가능

-- 날짜형 -> 문자형 -> 숫자형 변환
select sysdate, to_number(to_char(sysdate,'yyyymmdd')) from dual;

-- 년,월,일 한글 입력방법 : "년","월","일"
-- 날짜형타입 -> 문자형타입 변경시, 년월일 한글과 특수문자 입력방법
select sysdate, to_char(sysdate,'yyyy"년"mm"월"dd"일" day') from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd day') from dual;

---------------------
-- 숫자형 타입 : 사칙연산 계산해서 출력됨.
select kor+eng from students;

-- 문자형 함수
select employee_id, email from employees;

-- 문자형타입 합쳐서 +기호 사용해서 합치려고 하면 에러
select emp_name+email from employess;

-- ||, concat 함수
select emp_name || email from employees;  -- 속도가 좀더빠름
select concat(emp_name,email) from employees;

--------------------

-- lower:소문자 취환 / upper:대문자 취환 / initcap:첫글자 대문자 취환
select * from member where lower(name)='bryan';

select 'joHn',initcap('joHn'),lower('joHn'),upper('joHn') from dual;

-- lpad : 왼쪽 자릿수 채우기
select 'john',lpad('john',10,'#') from dual;

-- rpad : 오른쪽 자릿수 채우기
select 'john',rpad('john',10,'#') from dual;

-- trim : 빈공백 없애기 / ltrim : 왼쪽 공백없애기 / rtrim : 오른쪽 공백없애기
select length('    aaa   '),length(trim('  aaa  ')) from dual;

-- replace : 취환 (대체하기)
select '   a  b c  ',trim('   a  b c  ') from dual;

select length('   a  b c  '),length(trim('   a  b c  ')),length(replace('   a  b c  ',' ','')) from dual;
