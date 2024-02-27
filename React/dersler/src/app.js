class Header extends React.Component{
    render(){
        console.log(this.props.title);// dışardan değişken alamaya yarar htmlden
        console.log(this.props.numberList);
        return (
            <div>
                <h1>{this.props.title}</h1>
                <ToDoList numberList = {this.props.numberList}/>
            </div>
        );
    }
}//yeni bir tag gibi düşünebilirsin


/*function Header(props){
    console.log(props.title);
        return (
            <div>
                <h1>`${props.title}`</h1>
                <h2>tamam</h2>
            </div>
        );
    } // burda htmlden değişken almaya yarar
*/
class ToDoList extends React.Component{
    constructor (props){
        super(props);
        this.clearItems = this.clearItems.bind(this);//this e yeniden sahip olmak için
        this.degerDegistir = this.degerDegistir.bind(this);
        this.state = {numara : this.props.numberList[0]};
    }
    degerDegistir(){
        //this.state.numara = "11"; 
        // bunun yerine html de değişsin diye
        // state olmak zorunda
        this.setState (
            {numara: "1"}
        );
    }

    clearItems(){
        console.log(this.props);
    }
    render(){
        console.log(this.props.numberList);
        
        return(
            <div>
            {this.props.numberList.map( (item,index) => {
                return <li key={index} > { item}</li>;
            })}
            <button onClick = {this.clearItems}> temizle </button>
            <button onClick = {this.degerDegistir}> degistir </button>
            <p>{this.state.numara}</p>
            </div>
        );
    }
}

class Action extends React.Component{
    onFromSumbmit(event){
        event.preventDefault();
        let a = event.target.elements.isim.value;
        console.log(a);
    }
    render(){
        return(
            <form onSubmit={this.onFromSumbmit}>
                <input type="text" name="isim" />
                <button type="submit"> add item </button>
            </form>
        );
    }
}

class ToDoApp extends React.Component{
    
    
    render(){
        
        this.naber = "a";
        var numberList = ["10","20","30","40"]; 
        const title = "asdf";
        
        
        return(
            <div>
                <Header title ={title} numberList={numberList}/>
                <Action/>
            </div>
        );
    }
}// her şeyi buraya koyuyoruz


ReactDOM.render(<ToDoApp/>, document.getElementById('root'));