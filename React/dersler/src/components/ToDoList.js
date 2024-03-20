import React from "react";

export default class ToDoList extends React.Component{
    constructor (props){
        super(props);
        this.clearItems = this.clearItems.bind(this);//this e yeniden sahip olmak için
        this.degerDegistir = this.degerDegistir.bind(this);
        this.state = {numara : this.props.numberList[0]};
    }

    componentDidMount(){
        const json = localStorage.getItem("numara");
        const numara = JSON.parse(json);
        numara && this.setState({numara: numara});
    }
    componentDidUpdate(prevProps,precState){
        if(precState.numara !== this.state.numara){
            const json = JSON.stringify(this.state.numara);
            localStorage.setItem('numara',json);
        }
    }

    degerDegistir(){
        //this.state.numara = "11"; 
        // bunun yerine html de değişsin diye
        // state olmak zorunda
        this.setState ({
            numara: this.state.numara + 1
        });
        console.log(this.state.numara);
    }

    clearItems(){
        this.setState ({
            numara: 0
        });
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