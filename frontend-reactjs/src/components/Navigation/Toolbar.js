import React, { Component } from "react";
import { NavLink } from "react-router-dom";
import { PersonFill, CaretDown, InfoCircle } from "react-bootstrap-icons";
import classes from "./Toolbar.module.css";

class Toolbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      showDropdownItem: false,
    };
  }

  componentDidMount() {
    window.onclick = (event) => {
      if (event.target.className !== classes.dropbtn) {
        this.setState({
          showDropdownItem: false,
        });
      }
    };
  }

  showDropdownItems = () => {
    this.setState((prevState) => {
      return {
        ...prevState,
        showDropdownItem: !prevState.showDropdownItem,
      };
    });
  };

  render() {
    let showDropdownItemClass = [classes.dropdownContent];

    if (this.state.showDropdownItem) {
      showDropdownItemClass = [classes.dropdownContent, classes.show];
    }

    return (
      <header className={classes.Toolbar}>
        <nav>
          <InfoCircle />
          <h4>{this.props.title}</h4>
        </nav>

        <NavLink
          to="/home-page"
          style={{
            color: "white",
          }}
          activeStyle={{
            fontWeight: "bold",
            color: "red",
          }}
        >
          Home
        </NavLink>

        <NavLink
          to="/room-monitor"
          style={{
            color: "white",
          }}
          activeStyle={{
            fontWeight: "bold",
            color: "red",
          }}
        >
          Room Monitor
        </NavLink>

        <NavLink
          to="/qr-code-scan"
          style={{
            color: "white",
          }}
          activeStyle={{
            fontWeight: "bold",
            color: "red",
          }}
        >
          QR Code Scan
        </NavLink>

        <nav>
          <div className={classes.dropdown}>
            <button
              onClick={this.showDropdownItems}
              className={classes.dropbtn}
            >
              <PersonFill style={{ marginRight: "5px" }} />
              {this.props.username}
              <CaretDown style={{ marginLeft: "5px" }} />
            </button>
            <div id="myDropdown" className={showDropdownItemClass.join(" ")}>
              <button onClick={this.props.logoutBtnHandler}>Logout</button>
            </div>
          </div>
        </nav>
      </header>
    );
  }
}


export default Toolbar;
