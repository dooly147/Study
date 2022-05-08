// 입력완료 버튼 클릭시 checkjoinfrm 함수 호출
let joinbtn = document.getElementById('joinbtn');
joinbtn.addEventListener('click', checkjoinfrm);

function checkjoinfrm() {
   let uid = document.getElementById('userid');
   let pwd = document.getElementById('passwd');
   let repwd = document.getElementById('repasswd');
   let name = document.getElementById('name');
   let email = document.getElementById('email');

   // 회원정보 입력 여부 확인
   if (uid.value == '') {
      alert('아이디를 입력하세요!');  // 경고창 표시
      uid.focus();                 // 해당 요소에 커서 표시
   } else if (pwd.value == '') {
      alert('비밀번호를 입력하세요!');
      pwd.focus();
   } else if (repwd.value == '') {
      alert('비밀번호 확인을 입력하세요!');
      repwd.focus();
   } else if (name.value == '') {
      alert('이름을 입력하세요!');
      name.focus();
   } else if (email.value == '') {
      alert('이메일을 입력하세요!');
      email.focus();
   } else if (pwd.value != repwd.value) {
      alert('비밀번호가 서로 일치하지 않아요!');
      pwd.focus();
   } else {
       let frm = document.getElementById('join');
       frm.method = 'post';   // 폼 전송방식 지정
       frm.submit();          // 폼 데이터를 서버로 전송
   }

}
