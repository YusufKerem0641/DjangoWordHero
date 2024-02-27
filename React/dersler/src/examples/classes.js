class Person {
    constructor(name = "guest", year = 2000){
        this.name = name;
        this.year = year;
    }
    calculateAge(){
        return new Date().getFullYear() - this.year;
    }

    greeting(text) {
        return `${text}, my name is ${this.name}`;
    }
}

const p1 = new Person("hasan");
console.log(p1.greeting("hello"));
console.log(p1.calculateAge());