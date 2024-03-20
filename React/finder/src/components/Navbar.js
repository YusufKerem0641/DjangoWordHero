import React, { Component } from 'react';


export class Navbar extends Component {
  render() {
    const {sr} = this.props;
    return (
      <>
            <i className={sr}></i>
            {sr}
            asdf
      </>
    )
  }
}

Navbar.defaultProps = {
  sr: "fa-brands fa-github"
}
export default Navbar
