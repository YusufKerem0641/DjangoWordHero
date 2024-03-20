import React from "react";
import ToDoList from "./ToDoList";

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

export default Header;