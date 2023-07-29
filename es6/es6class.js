class Example{
    static sum(a,b){
        console.log(a,b)
    }
}
Example.sum(1,2)

let t = new Example();
console.log("new 一个对象: ",typeof(t))