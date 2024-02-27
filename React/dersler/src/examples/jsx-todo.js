var root = document.getElementById('root');

var list = ['naber','merhaba'];

function onFromSumbmit(event){
    event.preventDefault();
    var a = event.target.elements.isim.value;
    a && list.push(a);
    render();
}
function clearList(){
    list = [];
    render();
}

function listPrint(item,index){
    return <li key={index.toString} > { item}</li>;
}

function render(){
    var template =  <div>
                        <h1 id="he" > naber </h1> 
                        <div>Lorem ipsum dolor sit amet.</div>
                        <ul>
                            {
                                list.map(listPrint)
                            }
                        </ul>
                        <p>{list.length}</p>
                        <button onClick = {clearList}> clear</button>
                        <form onSubmit={onFromSumbmit}>
                            <input type="text" name="isim" />
                            <button type="submit"> add item </button>
                        </form>
                    </div>;
    ReactDOM.render(template, root);

}
render();
