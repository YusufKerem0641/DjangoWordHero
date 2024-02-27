class Header extends React.Component{
    render(){
        console.log(this.props.title);// dışardan değişken alamaya yarar htmlden
        return (
            <div>
                <h1>naber</h1>
                <h2>tamam</h2>
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
class ToDo extends React.Component{
    render(){
        return(
          <div>naber</div>
        );
    }
}

class ToDoApp extends React.Component{
    render(){
        const title = "asdf";
        return(
            <div>
                <Header title ={title}/>
                <ToDo/>
            </div>
        );
    }
}// her şeyi buraya koyuyoruz


ReactDOM.render(<ToDoApp/>, document.getElementById('root'));