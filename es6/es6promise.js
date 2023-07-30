// 异步编程  promise [有三种状态] pending  fulfilled rejected
const p1 = new Promise(function(resolve,reject){
     resolve('success1')
     resolve('success2')

})
const p2= new Promise(function(resolve,reject){
    resolve('success3')
    reject('reject')
})

p1.then(function(value){console.log(value)})
p2.then(function(value){console.log(value)})

// const p4 =new Promise(function(resolve,reject){
//     resolve(1);

// }).then(function(result){
//     p4(result).then(newResult=>p2(newResult))

// }).then(()=>p3());