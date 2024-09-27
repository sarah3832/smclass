// 제이쿼리 선언
$(function(){

  $("#searchBtn").click(function(){
    alert("검색버튼 클릭");
    let surl = "https://apis.data.go.kr/B551011/PhotoGalleryService1/gallerySearchList1?serviceKey=C2duPwoVyzL4a65JGcp9k28ZiHIuugwI%2BPj1H1uIhqNZVM5fv1yho7%2BRyFN%2FxU7mYmWhPyxAqbyNxfqQEJi34w%3D%3D&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json&keyword=";
    let searchWord = $("#search_txt").val();
    surl += searchWord;
    $.ajax({
      url:surl,
      type:"get",
      data:"",
      dataType:"json",
      success:function(data){
        alert("성공");
        console.log(data);

        console.log(data.response.body.items.item.galContentId);
        var item = data.response.body.items.item

        var s_data;
        for(var i=0;i<item.length;i++){
          s_data += `<tr>`
          s_data += `<td>${item[i].galContentId}</td>`
          s_data += `<td>${item[i].galTitle}</td>`
          s_data += `<td>${item[i].galPhotographyMonth}</td>`
          s_data += `<td>${item[i].galModifiedtime}</td>`
          s_data += `<td><img src='${item[i].galWebImageUrl}'</td>`
          s_data += `</tr>`
        }
        $("#tbody").html(s_data);

        
      },
      error:function(){
        alert("실패");
      }
      
      
    }); // ajax
  }) // searchBtn



}); // 제이쿼리