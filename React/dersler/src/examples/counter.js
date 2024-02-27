var product = {
    name : "samsaa",
    price : 500,
    description : "baya iyi"
}

function formatPrice(p){
    return p.price + ' TL';
}

function getDescription(description){
    if (description){
        return <p id="product-desc"> desc: {description} </p>;
    }
}

var template2 = <div id= "product-details">
                    <h2 id="product-name"> name: {product.name}</h2>
                    {product.price >0 && <p id="product-price"> price: {formatPrice(product)}</p>} 
                    {getDescription(product.description)}
                </div>;
//yukarda && bu evet dönerse sıradakine döner ve yazdırır

var deger = 0;
var yaz = (a) => {
    deger = deger + a;
    renderApp();
};
function yaz2(a){
    deger = deger + a;
    renderApp();
}
function renderApp(){
    var template3 = <div>
                        <button id="btnPlusOne" className="red" onClick={() => yaz(1)} >{deger}</button>
                        <button id="btnMinuseOne" className="blue" onClick={() => yaz(-1)} >{deger}</button>
                    </div>;
                    ReactDOM.render(template3, root);
                }

//renderApp();
function tick (){
    var element = <h2> time is : {new Date().toLocaleTimeString()}</h2>
    ReactDOM.render(element, root);
}
setInterval(tick,1000);
