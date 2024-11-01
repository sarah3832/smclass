-- 입사일의 마지막 날짜를 출력하시오.
-- 10/1 --> 10/31
select hire_date,last_day(hire_date) from employees; 

-- 가입일
select sdate from students;

select sdate,add_months(sdate,12) from students;
select sdate,add_months(sdate,-6) from students;  -- 마이너스 : 이내에

-- 현재일 기준으로 가입일이 6개월 이내의 회원만 출력
select sdate from students where sdate >= add_months(sysdate,- 6) order by sdate;


-- 그룹함수 : sum,avg,count,min,max,median

-- 년도,월별로 가입인원을 나눠서 출력하시오.
select mdate from member order by mdate;
select substr(last_day(mdate),1,5) md,count(*) from member group by last_day(mdate) order by md; 

-- employees테이블에서 부서별 인원을 출력하시오.
select department_id from employees;
select department_id,count(department_id) from employees group by department_id;

-----------------------------------
-- insert,update,delete
-- commit,rollback

create table emp3 as select * from employees;
select * from emp3;
create table emp4 as select * from employees where 1=2;
select * from emp4;

-- 테이블 구조가 있는 상태에서 모든 데이터를 입력하는 방법
insert into emp4 select * from employees;
rollback;

-- 제약조건을 확인
insert into emp4(employee_id,emp_name,hire_date) select employee_id,emp_name,hire_date from employees;

----------------------------------
-- 테이블
-- create : 생성 / alter : 변경 / drop : 삭제

select * from emp4;
-- alter add : 테이블에 컬럼 추가
alter table emp4 add(hire_date2 date);

desc emp4;

-- 컬럼 변경 : 컬럼 안에 데이터가 있다면 제약조건이 생김 (65길이의 문자가 있을경우, 50으로 변경x)
alter table emp4 modify(email varchar2(70));

alter table emp4 modify(email varchar2(50));

select emp_name from emp4;
desc emp4;
alter table emp4 modify(emp_name varchar2(10));  -- 안의 데이터 글자수가 길면, 변경불가

-- 컬럼의 최대길이 알아보는 방법
select max(length(emp_name)) from employees;
select length(emp_name) em from employees order by em desc;

-- 컬럼 타입 변경 -> 컬럼 안 데이터가 null이면 가능
-- 다른 타입인 경우, 데이터를 null로 변경 후 타입을 변경해야함
select * from emp4;
alter table emp4 modify(email number(6));

alter table emp4 modify emp_name number(20);

desc emp4;

-- employee_id 값을 email컬럼에 복사
update emp4 set email = employee_id;

-- employee_id 값을 phone_number에 입력하시오.
-- phone_number: 문자형타입 / employee_id: 숫자형타입
update emp4 set phone_number = employee_id;
commit;
rollback;

select * from emp4;
update emp4 set phone_number = '198a' where employee_id = 198;

-- 문자형타입을 숫자형타입에 복사
-- 안에있는 데이터가 모두 숫자형이기에 가능
-- 문자가 포함되어 있으면 타입변경 불가
update emp4 set manager_id = phone_number;
select * from emp4;

-- 컬럼이름 변경 : rename column (원래이름) to (변경이름)
desc emp4;
alter table emp4 rename column phone_number to p_number;

-- 속성 변경가능
alter table emp4 modify hire_date date null;
alter table emp4 modify hire_date date not null;

-- 컬럼 삭제
alter table emp4 drop column hire_date2;
desc emp4;

-- 테이블 삭제
drop table emp2;
drop table emp3;

-- 테이블 이름 변경 : rename (원래이름) to (변경이름)
rename emp4 to emp44;

------------------------------

-- primary key : 중복불가, null값 불가
-- unique : 중복 불가, null값 허용
-- not null : 중복 허용, null값 불가
-- default : 값이 입력되지 않았을때 디폴트값 지정

select gender from member;

create table bmember(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) not null,
nicname varchar2(30),
age number(3) default 0,
gender varchar2(6) check(gender in('Male','Female')),
email varchar2(20),
bdate date default sysdate
);

desc bmember;

-- 입력
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values (
'aaa','1111','홍길동','길동스',20,'Male','aaa@aaa.com',sysdate
);
insert into bmember(id,pw,name,nicname,gender,email) values (
'bbb','2222','유관순','관순스','Female','bbb@bbb.com'
);
-- check (Male,Female형태 외에는 입력이 안됨.소문자x)
-- male, MALE, malE 불가능
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values (
'ccc','1111','이순신','순신스',20,'Male','ccc@ccc.com',sysdate
);
-- not null : null허용x(' ' : 빈공백은 가능)
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values (
'ddd',' ','강감찬','감찬스',20,'Male','ddd@ddd.com','2024/01/01'
);
-- primary key : 중복x, nullx
insert into bmember(id,pw,name,nicname,age,gender,email,bdate) values (
'eee',' ','김구','구스',20,'Male','eee@eee.com','2024/02/21'
);
commit;
select * from bmember;


create table emp3(
empno number(4) unique,
ename varchar2(30) not null,
job varchar2(9),
deptno number(2)
);

insert into emp3 values(
1,'홍','01','01'
);
insert into emp3 values(
2,'유','02','02'
);
-- unique : null값은 허용
insert into emp3 (ename,job,deptno) values(
'이','03','03'
);
-- unique : 중복 불가
insert into emp3 values(
2,'강','04','04'
);

select * from emp3;

----------------------------

-- primary key 등록시, null갑 존재하면 안됨, 중복도 존재하면 안됨
-- primary key 추가, 수정
desc member;
-- constraint id_pk : 이름 설정
alter table member add CONSTRAINT id_pk primary key(id);

select * from member;

insert into member values(
'aaa','1111','홍길자','aaa@aaa.com','123-456-7890','Female','golf',sysdate
);

-- primary key 삭제
alter table member drop CONSTRAINT id_pk;

alter table member add constraint id_pk primary key(id);

---------------------------
desc bmember; 
 
create table board(
bno number(4) primary key,
btitle varchar2(100) not null,
bcontent clob,
id varchar2(30),
bgroup number(4),
bstep number(4),
bindent number(4),
bhit number(4),
bdate date,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목2','내용2','bbb',board_seq.currval,0,0,0,sysdate,''
);
insert into board values(
board_seq.nextval,'제목5','내용5','ddd',board_seq.currval,0,0,0,sysdate,''
);
rollback;
select * from board;  -- 개수 5개 (bno,btitle,bcontent,id,bgroup,bstep,bindent,bhit,bdate,bfile
select * from bmember;  -- 개수 5개 (id,pw,name,nicname,age,gender,email,bdate)



-- 관계형db
-- 조인(join)
select bno,btitle,bcontent,nicname,email,bgroup,bstep,bindent,bhit,bfile
from board,bmember
where board.id = bmember.id;  -- memeber id : primary key / board id : foreign key

-- 조인(join)
select employee_id,emp_name,email,salary,employees.department_id,department_name 
from employees,departments
where employees.department_id = departments.department_id;

select department_id,department_name from departments
where department_id = 20;


-- foreign key 추가,변경
desc board;
-- 닉네임 : id_fk / foreign key : id,bmember테이블의 primary key(id) 등록
alter table board add CONSTRAINT id_fk foreign key(id) references bmember(id);

-- 테이블 create할때, foreign key 생성
create table board2(
bno number(4) primary key,
btitle varchar2(1000) not null,
bcontent clob,
id varchar2(30)
constraint fk_board2_id foreign key(id) references bmember(id)
);


-- foreign key 삭제
alter table board drop constraint id_fk;


select * from board;
select * from bmember;  -- aaa,bbb,ccc,ddd,eee

-- abc글을 등록하면, 등록이 안됨
insert into board values(
board_seq.nextval,'제목6','내용6','abc',board_seq.currval,0,0,0,sysdate,' '
);

delete board where bno = 13;

-- [foreign key 등록된 id 삭제방법 ]
-- bmember테이블 id, foreign key로 board,board2에 등록
-- foreign key : 외래키
-- 원본의 primary key에 데이터를 지우려면, 원칙으로는 foreign key의 데이터를 모두 삭제해야 삭제가 됨.
-- foreign key를 해제해야 삭제 가능 
-- primary key : 기본키
delete bmember where id='aaa';
delete board where id='aaa';

select * from bmember;
select * from board;

alter table board drop constraint id_fk;

-- foreign key로 등록이 되면, primary key를 삭제할때 foreign key에 데이터가 있으면 삭제가 안됨.
-- on delete cascade : primary key가 삭제가 되면, foreign key로 등록된 모든 글을 삭제시킴.
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;

--alter table board add constraint fk_board_id foreign key(id) references bmember(id) on update cascade;

-- 1. on delete restricted
-- 기본값 : 입력하지 않을시, 자식데이터가 있을경우, 부모데이터가 삭제가 되지않음. 
alter table board add constraint id_fk foreign key(id) references bmember(id);
-- 자식테이블에 aaa로 쓴 데이트를 삭제해야 id를 삭제할 수 있음
delete bmember where id='aaa';
delete board where bno = 3;


-- 2. on delete cascade
-- 부모데이터 삭제시, 자식데이터 모두 삭제
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete cascade;
-- 부모데이터를 삭제하면, 자식데이터의 모든 글이 삭제
delete bmember where id='aaa';


-- 3. on delete set null
-- 부모데이터 삭제시, 자식데이터에 해당되는 값이 null 표시
alter table board add constraint id_fk foreign key(id) references bmember(id) on delete set null;
-- 부모데이터를 삭제하면 자식데이터의 해당 컬럼만 null변경되고, 데이터는 그대로 존재
delete bmember where id='aaa';
select * from board;


rollback;

-----------------------------
-- check 구문
create table emp01(
empno number(4) primary key,
ename varchar2(30) not null,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female'))
);

-- check가 지정되어 있는 컬럼에 추가
insert into emp01 values(
1,'홍길동',2500,'Male'
);
-- salary 범위를 벗어나면 에러
insert into emp01 values(
2,'유관순',20000,'Female'
);
-- Male,Female 이외 단어 입력시 에러
insert into emp01 values(
3,'이순신',20000,'male'
);

-- default : insert시 값이 입력이 되지 않을시, 문자,숫자,날짜 넣을 수 있음
create table emp02(
empno number(4) primary key,
ename varchar2(30) default '무명',
income number(4) default 0,
salary number(7,2) check(salary between 2000 and 20000),
gender varchar2(10) check(gender in('Male','Female')),
edate date default sysdate
);

insert into emp02 (empno,salary,gender) values(1,5000,'Male');

select * from emp02;
commit;


create table mem(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30) default '무명',
age number(3) default 0,
birth date,
gender varchar2(6) check (gender in ('Male','Female')),
hobby varchar2(50) default 'game',
mdate date default sysdate
);

insert into mem values(
'aaa','1111','홍길동','22','2000/05/05','Male','golf',sysdate
);
insert into mem values(
'bbb','1111','유관순','22','2000/06/25','Female','book',sysdate
);
insert into mem values(
'ccc','1111','이순신','23','2001/12/25','Male','war',sysdate
);
commit;
select * from mem;

select count(*) from mem;

-- 그룹함수
select count(*)person,department_id from employees
where department_id = 50
group by department_id;
-- 부서번호, 부서명
select count(*),a.department_id,department_name
from employees a,departments b
where a.department_id = b.department_id;


-- 부서번호 50번인 부서인원,부서번호,부서명을 가져오시오.
-- 부서별개수, 부서번호, 부서명, 그룹함수
select count(*)no,a.department_id dept,department_name deptname
from employees a,departments b
where a.department_id = b.department_id and a.department_id = 50
group by a.department_id,department_name; 


desc mem;

insert into mem(id,pw,name,age,birth,gender,hobby) values('ddd','1111','강감찬','22','20020312','Male','game');

select * from mem;

rollback;


select * from students;

insert into students(id,pw,name,kor,eng,math) values('ddd','1111','강감찬','22','20020312','Male','game');

--delete students where name = '김유신';

----------------------------------

update mem2 set id='abc',pw='1111',name='유니',email='sarah3832@naver.com'
where id = 'Trineman';

desc member;

select * from member;

delete member;
commit;

insert into member select * from mem2;
select * from member;