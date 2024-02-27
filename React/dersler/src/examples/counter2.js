class Counter extends React.Component{
    constructor (props){
        super(props);
        this.addMinus = this.addMinus.bind(this);//this e yeniden sahip olmak için
        this.state ={number : 0} ;
    }
    addMinus(a)
    {
        this.setState({
            number : this.state.number + a
        });
    }
    render(){
        return(
            <div>
                <p>{this.state.number}</p>
                <button onClick={() => this.addMinus(1)} >+</button>
                <button onClick={() => this.addMinus(-1)} >-</button>
            </div>
        );
    }
}
ReactDOM.render(<Counter/>, document.getElementById('root'));