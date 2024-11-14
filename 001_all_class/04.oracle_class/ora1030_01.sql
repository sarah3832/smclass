select sysdate from dual;

-- 날짜는 +,- 가능
select sysdate-30,sysdate,sysdate+30 from dual;

-- employees테이블에서 hire_date 컬럼 데이터 뽑아옴
select hire_date-1,hire_date,hire_date+1 from employees;

-- 날짜 범위 검색가능, 정렬 : order by / asc:순차정렬(생략o) / desc:역순정렬
select emp_name,hire_date from employees where hire_date >= '02/01/01' and hire_date <= '04/12/31' order by hire_date desc;

select emp_name,hire_date from employees where hire_date between '02/01/01' and '04/12/31' order by hire_date;

-------------------------

-- like
select emp_name from employees where emp_name like '___a%';

select emp_name from employees where emp_name like '%a_';

-------------------------

-- 정렬 desc : null값이 제일 위쪽 / asc : 제일 아래쪽
select department_id from employees order by department_id desc;

-- 월급 역순정렬
select emp_name,salary from employees order by salary desc;

-- students테이블에서 total 역순정렬
select no,name,total from students order by total desc;

-- hire_date 기준으로 순차정렬
select emp_name,hire_date from employees order by hire_date;

-- kor가 기준점, 동일한 값이 있을때 eng로 넘어감 (두개 다 정렬이 되는건x)
select name,kor,eng,math from students order by kor desc, eng desc;

-- 한국어 순차정렬 : ㄱ,ㄴ,ㄷ.. / 역순정렬 : ㅎ,ㅌ,ㅍ..
select name from students order by name;

-- 입사일이 빠른 순으로 정렬, 이름은 역순으로 정렬하시오.
select emp_name,hire_date from employees order by hire_date,emp_name desc;

-------------------------

-- abs : 절대값
select -10 val,abs(-10) as abs from dual;
select kor,kor-eng,abs(kor-eng) abs from students order by abs desc;

-------------------------

-- floor : 소수점 이하는 버림
select 3.141592, floor(3.141592) from dual;

-- trunc : 버림, 자리수 지정
select 34.5678, trunc(34.5678,2) from dual;
select 34.5678, trunc(34.5678,-1) from dual;

-- ceil : 소수점 이하 올림
select 3.14592, ceil(3.14592) from dual;

-------------------------

-- round : 반올림, 자리수 범위지정
-- 소수점 첫째자리 반올림
select 34.5678, round(34.5678) from dual;

-- 소수점 셋째자리에서 반올림 / 둘째자리까지 출력
select 34.5678, round(34.5678,2) from dual;

-- 양수 첫째자리에서 반올림 / 소수점 자리수에서 앞쪽으로 한칸위치 반올림
select 34.5678, round(35.5678,-1) from dual;

-------------------------

-- mod : 나머지
select 27/2, mod(27,2) from dual;
select 30/3, mod(31,7) from dual;

-- 사원번호가 홀수인 사원을 출력하시오.
select emp_name,employee_id from employees where mod(employee_id,2) = 1 order by employee_id;


-- 최종연봉 : 월급*12+(월급*12)*커미션, 소수점은 둘째자리 반올림(첫째자리로 만들기)
-- 환율 1381.86
select emp_name, salary, round(salary*12+((salary*12)*nvl(commission_pct,0))*1381.86795,1) 최종연봉 from employees;

-------------------------

select * from students;

-- 시퀀스 : 자동으로 번호부여
create sequence stu_seq 
start with 1 increment by 1 
minvalue 1 maxvalue 9999 
nocycle nocache;

-- 시퀀스에서 번호생성
select stu_seq.nextval from dual;

select stu_seq.currval from dual;

-- 게시판 테이블 생성
create table board(
bno number(4),
btitle varchar2(100),
bcontent varchar2(4000),  -- varchar2 : 최대값 4000
id varchar2(30),
bhit number(10),
bdate date
);

insert into board values(
1,'제목입니다.','내용입니다.','aaa',1,sysdate
);
insert into board values(
2,'제목입니다.2','내용입니다.2','aaa',1,sysdate
);
insert into board values(
stu_seq.nextval,'제목입니다.2','내용입니다.2','aaa',1,sysdate
);

select * from board;
commit;

-------------------------

select * from board;

create sequence board_seq
start with 15  -- 시작번호
increment by 1 -- 증감숫자
minvalue 1     -- 최소값
maxvalue 9999  -- 최대값
nocycle        -- 1~9999 이상이되면, 다시 1
nocache        -- 메모리에 시퀀스값 미리 할당
;

desc board;

insert into board values(
board_seq.nextval,'제목15','내용15','aaa',1,sysdate
);

select * from board;

update board set btitle = '제목을 다시 변경' where bno = 16;

commit;

-------------------------

--drop table board;

create table board(
bno number(4),
btitle varchar2(100),
bcontent clob,  -- clob = varchar2무제한 (대용량 글자타입)
id varchar2(20),
bgroup number(4),  -- 답변달기 그룹핑
bstep number(4),   -- 답변달기 경우 순서정의
bindent number(4), -- 답변달기 들여쓰기
bint number(10),   -- 조회수
bdate date         -- 등록일
);

select board_seq.currval from dual;

insert into board values(
board_seq.nextval,'제목1','내용1','aaa',board_seq.currval,0,0,1,sysdate
);

select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students테이블 100 -> 101
-- 101,'홍길순',99,99,90,total,avg,rank,날짜
-- 1명을 입력하시오.

insert into students values(
students_seq.nextval,'홍길순',99,99,99,99+99+90,(99+99+90)/3,0,sysdate
);

select * from students;

commit;

select no,name,kor,eng,math,total,round(avg,2),rank,sdate from students;

select round(avg,2) from students;

select s.*,round(avg,2) from students s;  -- table에도 별칭줄 수 있음

-------------------------

select dept_seq.nextval from dual;

-- s_seq 만들기
-- 시작 1, 증분 1, 최대값 99999
create sequence s_seq
start with 1
increment by 1
minvalue 1     
maxvalue 99999
nocycle       
nocache        
;
-- 시퀀스 생성, nextval: 다음 시퀀스번호 생성 / currval: 현재 시퀀스번호 보여줌
select s_seq.nextval from dual;
select emp_seq.nextval from dual;
select emp_seq.currval from dual;

-------------------------

-- 타입 : 문자형, 숫자형, 날짜형

-- 문자형 : char,varchar2,nchar,nvarchar2/ long,clob(대용량)
-- char,varchar2 : 한글문자 입력시, 3byte 사용
-- varchar2(6) : 한글 2글자 입력
-- nvarchar2(5) : 한글 5자리까지 입력가능, 2byte

-- 숫자형 : number
-- 날짜형 : date(초까지 입력) / timestamp(밀리세컨드까지 입력)


select '홍길동' from dual;
-- length : 문자길이
select length('홍길동') from dual;

-- 이름의 길이로 역순정렬
select name,length(name) n from students order by n desc;

-- lengthb : byte 크기
select lengthb('홍길동') from dual;

-------------------------

-- 합계가 200이상, 번호가 10이상 50이하, 이름 2번째자리 e가 들어가있는 학생출력
select * from students;
select * from students where total >= 200 and no >= 10 and no <= 50 and name like '_e%';

select * from students where total >= 200;

-- select * from 테이블
-- 이중쿼리
select * from (
select * from students where total >= 200
) where name like '_e%' and no >= 30;

rollback;

select * from students;

select no,name,total,rank from students;

-- 등수함수 : rank() over(기준점) 입력, no는 중복없음(유일키,기본키,프라이머리 키(primary key)
select no,rank() over(order by total desc) ranks from students;
select ranks from (select no,rank() over(order by total desc) ranks from students);

select * from students;

select no,name,total,rank from students order by total desc;

-- 수정 : update
update students a
set rank = (
select ranks from (select no,rank() over(order by total desc) ranks from students) b
where a.no = b.no
);

update students a
set rank = 1
where a.no = 101;

select * from students order by rank;

rollback;

select no,rank() over(order by total desc)as ranks from students;

update students set rank = 1 where no = 101;
update students set rank = 2 where no = 96;
update students set rank = 3 where no = 64;
update students set rank = 4 where no = 49;
update students set rank = 5 where no = 14;


-- 사원번호가 높은순으로 등수를 생성하시오.
select * from employees;

select employee_id,emp_name,rank() over(order by employee_id desc) ranks from employees;

-- emp2테이블을 그대로 emp2테이블 복사생성
create table emp2 as select * from employees;

select rank() over(order by employee_id desc) from employees;

-- 테이블 컬럼 추가
alter table emp2 add rank number(4);

desc emp2;

select * from emp2;

-- rank() 등수를 rank에 입력
update emp2 e set rank = (
select ranks from (select employee_id,rank()over(order by employee_id desc) ranks from employees)e2
where e.employee_id = e2.employee_id
);

select employee_id, rank from emp2 order by employee_id desc;

select * from emp2;

-- 컬럼의 순서를 변경
-- emp_name 뒤에 rank컬럼을 숨김처리
alter table emp2 modify EMAIL invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify HIRE_DATE  invisible;
alter table emp2 modify SALARY  invisible;
alter table emp2 modify MANAGER_ID  invisible;
alter table emp2 modify COMMISSION_PCT  invisible;
alter table emp2 modify RETIRE_DATE  invisible;
alter table emp2 modify DEPARTMENT_ID  invisible;
alter table emp2 modify JOB_ID  invisible;
alter table emp2 modify CREATE_DATE  invisible;
alter table emp2 modify UPDATE_DATE  invisible;
alter table emp2 modify RANK  invisible;

-- 컬럼을 나타나게함 (숨김처리 후, 나타나게하여 순서변경 가능)
alter table emp2 modify EMAIL visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify HIRE_DATE  visible;
alter table emp2 modify SALARY  visible;
alter table emp2 modify MANAGER_ID  visible;
alter table emp2 modify COMMISSION_PCT  visible;
alter table emp2 modify RETIRE_DATE  visible;
alter table emp2 modify DEPARTMENT_ID  visible;
alter table emp2 modify JOB_ID  visible;
alter table emp2 modify CREATE_DATE  visible;
alter table emp2 modify UPDATE_DATE  visible;
alter table emp2 modify RANK  visible;


-- 컬럼 삭제
desc emp2;

alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column HIRE_DATE;
alter table emp2 drop column SALARY;
alter table emp2 drop column COMMISSION_PCT;
alter table emp2 drop column RETIRE_DATE;
alter table emp2 drop column CREATE_DATE;
alter table emp2 drop column UPDATE_DATE;

select * from emp2;

select * from departments;
desc departments;

alter table emp2 add DEPARTMENT_NAME varchar2(80);

-- 부서명 없음
select * from emp2;

-- 부서명은 departments
select * from departments;

select department_id, department_name from emp2;
select department_id, department_name from departments;
 
-- 부서명 입력
update emp2 e set e.department_name = (
select d from(select department_id, department_name d from departments) e2
where e.department_id = e2.department_id
);
 
-------------------------

-- 테이블 복사
create table stu as select * from students;

desc stu;
--alter table stu drop column TOTAL;

select * from stu;

-- total컬럼, avg컬럼 추가하시오.
alter table stu add total number(3);
alter table stu add avg number(3);
alter table stu add rank number(3);

alter table stu modify sdate invisible;
alter table stu modify sdate visible;

-- 합계
update stu set total = kor+eng+math, avg = (kor+eng+math)/3;

-- rank 입력
select * from stu;
select no,total,rank() over(order by total desc) ranks from stu;

update stu s set rank = (
select ranks from (select no,rank()over(order by total desc)ranks from stu)s2
where s.no = s2.no
);

commit;


-------------------------

-- 날짜함수
-- 현재날짜 : sysdate
select sysdate from dual;
select sysdate -1 from dual;
select sysdate +30 from dual;

create table datetable(
no number(4),
predate date,
today date,
nextdate date
);

-- 회원가입 1달치, 6개월치, 1년치
insert into datetable values(
1,sysdate-30, sysdate, sysdate+180
);

select no,predate,today 가입일, nextdate 만료일 from datetable;

select * from member;

select id,name,mdate,sysdate,round(sysdate-mdate) from member
where sysdate >= mdate+180;

-- 입사일 기준으로 현재날짜와 입사일 몇일 지났는지 출력하시오.
select hire_date from employees;
select emp_name,hire_date 입사일,sysdate 현재, round(sysdate-hire_date) from employees;

-- 'month'단위로 출력
-- 15일 이상이면 1달을 올림 / 15일 미만이면 일을 초기화
select hire_date, round(hire_date,'month') from employees;

-- trunc : 일의 숫자를 1로 초기화
select hire_date, trunc(hire_date,'month') from employees;


-- 입사일, 현재일 기준의 달수
select hire_date, sysdate, months_between(sysdate,hire_date) from employees;

-- months_between : 두 일자 가운데 지나간 달수를 알려줌.
select hire_date, sysdate, round(months_between(sysdate,hire_date))달수, round(sysdate-hire_date)일수 from employees;

-- add_months : 3개월 추가
select hire_date, add_months(hire_date,3) from employees;

-- next_day : 다음주 수요일 날짜를 알려줌
select sysdate,next_day(sysdate,'수요일') from dual;

select sysdate, next_day(sysdate,'토요일') from dual;

-- last_day : 그 달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_Date) from employees;

select sysdate,last_day(sysdate) from dual;

-------------------------

-- 형변환 함수 : to_char / to_date / to_number
-- to_char : 날짜,숫자 -> 문자
-- to_date : 문자 -> 날짜
-- to_number : 문자 -> 숫자

select sysdate from dual;
select to_char(sysdate,'yy/mm/dd hh24:mi:ss') from dual;

select hire_date from employees;
select to_char(hire_date,'yyyy-mm-dd') from employees;

select to_char(to_date('24/01/01'),'yyyy/mm/dd hh:24:mi:ss') from dual;

select to_char('24/01/01','yyyy-mm-dd') from dual;

select to_char(to_date('24/01/01'),'yyyy-mm-dd') from dual;


select * from member where id = 'aaa' and pw = '1111';
select * from member;

update member set id = 'abc', pw = '1111', name = '유니', email = 'sarah3832@naver.com', gender = 'Female'
where id = 'Trineman';

commit;

select * from member where id='eee';

desc member;

alter table member drop column PW;
alter table member add PW varchar2(8);

alter table member modify NAME invisible;
alter table member modify EMAIL invisible;
alter table member modify PHONE invisible;
alter table member modify GENDER invisible;
alter table member modify HOBBY invisible;
alter table member modify MDATE invisible;

alter table member modify NAME visible;
alter table member modify EMAIL visible;
alter table member modify PHONE visible;
alter table member modify GENDER visible;
alter table member modify HOBBY visible;
alter table member modify MDATE visible;
