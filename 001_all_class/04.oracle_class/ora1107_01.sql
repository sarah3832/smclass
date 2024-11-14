-- 평균 80점 이상이면서 국어 90점 이상 출력하시오.
select * from students;
select * from students where avg > 80 and kor > 90;

-- 평균 60점 이상 또는 총점 100점 이상
select * from students where avg > 60 or total > 100;


select * from students order by kor desc, eng desc;
