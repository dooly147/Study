// 로그인 버튼 클릭시 checkloginfrm 함수 호출
let loginbtn = document.getElementById('loginbtn');
loginbtn.addEventListener('click', checkloginfrm);

function checkloginfrm() {
   let uid = document.getElementById('userid');
   let pwd = document.getElementById('passwd');

   // 회원정보 입력 여부 확인
   if (uid.value == '') {
      alert('아이디를 입력하세요!');  // 경고창 표시
      uid.focus();                 // 해당 요소에 커서 표시
   } else if (pwd.value == '') {
      alert('비밀번호를 입력하세요!');
      pwd.focus();
   } else {
       let frm = document.getElementById('login');
       frm.method = 'post';   // 폼 전송방식 지정
       frm.submit();          // 폼 데이터를 서버로 전송
   }

}
