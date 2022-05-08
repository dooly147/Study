let tr25s = '';
let result = document.getElementById('result');

for(let i=1; i<=25; ++i) {
   tr25s += '<tr><td>' + i + '</td>' +
         '<td>시간은 금이라구, 친구! 진짜라구 친구! 정말이라구 친구!</td>' +
         '<td>zzyzzy</td><td>2021.10.10</td><td>123</td></tr>';
}

result.innerHTML = tr25s;
