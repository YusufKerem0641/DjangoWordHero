import React from "react";
import { createRoot } from 'react-dom/client';

import Header from "./components/Header";

import './styles/main.scss';



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


createRoot(root).render(<ToDoApp/>);



