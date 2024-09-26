// 1. ajax 데이터 가져오기
  let count = 1;  // 전역변수 - 회원번호 변수
  let total = 0;  // 전역변수 - 합계 변수
  let avg = 0;    // 전역변수 - 평균 변수
  var id_num;     // 전역변수 - 현재위치 확인 변수
  let temp = 0;   // 전역변수 - 수정버튼 클릭확인 변수 

$(function(){

  $.ajax({
    url:"js/stuDATA.json",
    type:"get",
    data:"",
    dataType:"json",
  success:function(data){
    $(document).on("click","#dataBtn",function(){
      alert("데이터를 가져옵니다.");

    var s_data;

    for(var i=0;i<data.length;i++){
      count++;
      console.log("count : "+count);
      total = data[i].kor + data[i].eng + data[i].math;
      avg = (total/3).toFixed(2);
      s_data += `<tr id='${data[i].no}'>`;
      s_data += `<td>${data[i].no}</td>`
      s_data += `<td>${data[i].name}</td>`
      s_data += `<td>${data[i].kor}</td>`
      s_data += `<td>${data[i].eng}</td>`
      s_data += `<td>${data[i].math}</td>`
      s_data += `<td>${total}</td>`
      s_data += `<td>${avg}</td>`
      s_data += `<td><button class='updateBtn'>수정</buttonm>
                 <button class='delBtn'>삭제</td>`;
      s_data += `</tr>`
    }
    $("#tbody").html(s_data);
    
    // 3.입력 버튼
    $(document).on("click","#create",function(){
      let name = $("#name").val();
      let kor = Number($("#kor").val());
      let eng = Number($("#eng").val());
      let math = Number($("#math").val());
      total = kor+eng+math;
      avg = (total/3).toFixed(2);

      if(name=="" || kor=="" || eng=="" || math==""){
        alert("데이터를 입력하셔야 저장이 가능합니다.");
        return false;
      }
      alert("학생 성적을 확인합니다.");

      // 표를 만들어서 내용추가
      let s_data = "";
      s_data += `<tr id='${count}'>`;
      s_data += `<td>${count}</td>`;
      s_data += `<td>${name}</td>`;
      s_data += `<td>${kor}</td>`;
      s_data += `<td>${eng}</td>`;
      s_data += `<td>${math}</td>`;
      s_data += `<td>${total}</td>`;
      s_data += `<td>${avg}</td>`;
      s_data += `<td><button class='updateBtn'>수정</button>
                 <button class='updateBtn'>삭제</button></td>`;
      s_data += `</tr>`;    
      
      $("#tbody").prepend(s_data);
      $("#name").val("");
      $("#kor").val("");
      $("#eng").val("");
      $("#math").val("");

      count++;
    });

    // 4.수정 버튼
    $(document).on("click",".updateBtn",function(){
      alert("수정을 진행합니다.");
      id_num = $(this).closest("tr").attr("id");

      let u_data = $(this).closest("tr");
      console.log(u_data.children("td:eq(1)").text());
      console.log(u_data.children("td:eq(2)").text());
      console.log(u_data.children("td:eq(3)").text());
      console.log(u_data.children("td:eq(4)").text());

      // 입력창에 값 넣기
      $("#name").val(u_data.children("td:eq(1)").text());
      $("#kor").val(u_data.children("td:eq(2)").text());
      $("#eng").val(u_data.children("td:eq(3)").text());
      $("#math").val(u_data.children("td:eq(4)").text());

      $("#create,#update,#updateCancel").toggle();
    });

    // 5.수정완료 버튼
    $(document).on("click","update",function(){
      let name = $("name").val();
      let kor = Number($("#kor").val());
      let eng = Number($("#eng").val());
      let math = Number($("#math").val());
      total = kor+eng+math;
      avg = (total/3).toFixed(2);

      if($("#name").val().length<1 || $("#kor").val().length<1 || $("#eng").val().length<1 || $("#math").val().length<1){
        alert("데이터를 입력하셔야 저장이 가능합니다.");
        return false;
      }

      let s_data = "";
      s_data += `<td>${id_num}</td>`
      s_data += `<td>${name}</td>`
      s_data += `<td>${kor}</td>`
      s_data += `<td>${eng}</td>`
      s_data += `<td>${math}</td>`
      s_data += `<td>${total}</td>`
      s_data += `<td>${avg}</td>`
      s_data += `<td><button class='updateBtn'>수정</button>
                 <button class='updateBtn'>삭제</button></td>`;
    });
    
    
    
    // 2.삭제 버튼
    $(document).on("click",".delBtn",function(){
      id_num = $(this).closest("tr").attr("id");
      if(confirm(id_num + "번 학생 성적을 삭제하시겠습니까?")){
    $("#"+id_num).remove();
    alert(id_num + "번 학생 성적이 삭제되었습니다.");
   }
  });
});
},

error:function(){
  alert("실패");
}
}); // ajax 선언
}); // 제이쿼리 선언