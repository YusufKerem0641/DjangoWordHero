const kimlik = {
    name : "kerem",
    age : 12,
    family : ["peder","abi"],
    cagirma : function(){
        this.family.forEach((human) => {
            console.log(human);
        });
    }
}
kimlik.cagirma();

const topla = function() {
    let total = 0;
    for(let i = 0; arguments.length > i; i++){
        total += arguments[i];
    }
    return total;
}
console.log(topla(1,2,3,4,5,6));