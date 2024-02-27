class Kimlik {
    constructor(name = "guest", year = 2000){
        this.name = name;
        this.year = year;
    }
    calculateAge(){
        return new Date().getFullYear() - this.year;
    }

    greeting(text) {
        return `${text}, my name is ${this.name}.`;
    }
}

class Personel extends Kimlik {
    constructor(name, year, number){
        super(name,year);
        this.number = number;
    }
    greeting(text) {
        let str = super.greeting(text);
        return str + ` numarası : ${this.number}`;
    }
}

const k1 = new Kimlik("hasan",2000);
console.log(k1.greeting("hello"));
console.log(k1.calculateAge());


const p1 = new Personel("rıfat",2010,1234);
console.log(p1.greeting("hi"));
console.log(p1.calculateAge());
console.log(p1.number);