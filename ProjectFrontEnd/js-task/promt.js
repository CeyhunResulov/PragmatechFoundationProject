// 1.cehd--ugursuz
// let username = prompt('username')
// // let password = prompt('password')
// // function sistemegiris(username, password){

// //     if (username == 'admin' && password == '123456') {
// //         return(sistemegiris)
// //     }
// //     // } else if (username != 'admin') {
// //     //     alert('usernme yanlisdir')
// //     // } else (password != '123456')
// //     // alert('password yanlisdir')
// // }------ birinci cehd ugursuz oldu


// 2.cehd--ugursuz
// let username = prompt('username')
// let password = prompt('password')
// if (username == "" || password == "") {
//     alert('deyerler bos ola bilmez!')
// } else if (username == 'admin' && password == '123456') {
//     alert('tebrikler! siz sisteme daxil oldunuz')
// } else if (username != 'admin') {
//     alert('username sehvdir!')
// } else if (password != '123456') {
//     alert('password sehvdir!')
//     }else if(username!='admin' && password!='123456' ){----bu hisse niye islemir
//     alert('her iki deyer yanlisdir!')
// }



// 3.cehd---ugurlu)
// let username = prompt('username')
// let password = prompt('password')
// if (username == "" || password == "") {
//     alert('deyerler bos ola bilmez!')
// } else if (username == 'admin' && password == 123456) {
//     alert('tebrikler! siz sisteme daxil oldunuz')
// } else if (username != 'admin' && password == 123456) {
//     alert('username sehvdir!')
// } else if (username == 'admin' && password != 123456) {
//     alert('password sehvdir!')
// } else if (username != 'admin' && password != 123456) {
//     alert('her iki deyer yanlisdir!')
// }


//4.cehd ---ugurlu)
let username = prompt('username')
let password = prompt('password')
if (username == "" || password == "") {
    alert('deyerler bos ola bilmez!')
} else if (username == 'admin' && password == '123456') {
    alert('tebrikler! siz sisteme daxil oldunuz')
} else if (username != 'admin' && password != '123456') {
    alert('her iki deyer yanlisdir!')
} else if (username != 'admin') {
    alert('username sehvdir!')
} else if (password != '123456') {
    alert('password sehvdir!')
}
