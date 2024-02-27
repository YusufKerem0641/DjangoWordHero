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
        this.clearItems = this.clearItems.bind(this);
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
            <button onClick = {this.clearItems}></button>
            </div>
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
            </div>
        );
    }
}// her şeyi buraya koyuyoruz


ReactDOM.render(<ToDoApp/>, document.getElementById('root'));