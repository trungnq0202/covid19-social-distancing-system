import React, { Component } from "react";
import PropTypes from "prop-types";
import { Route, Switch } from "react-router-dom";
import { connect } from "react-redux";
import { ConnectedRouter } from "connected-react-router";
import NotFound from "../../pages/error/NotFound/NotFound";
import RoomEnvironment from "../../pages/RoomEnvironment/RoomEnvironment";
import RoomMonitor from "../../pages/RoomMonitor/RoomMonitor";
import HomePage from "../../pages/HomePage/HomePage";

import QRCodeScan from "../../pages/QRCodeScan/QRCodeScan";

import "./App.css";

class App extends Component {
  static propTypes = {
    history: PropTypes.object,
  };

  // componentWillMount() {
  //   // this.props.autoLoggingIn();
  // }

  render() {
    const routes = (
      <Switch>
          <Route path="/room-environment" exact component={RoomEnvironment} />
          <Route path="/room-monitor" component={RoomMonitor} /> 
          <Route path="/qr-code-scan" component={QRCodeScan} />
          <Route path="/home-page" component={HomePage} />

          <Route path="*" component={NotFound} />
      </Switch>
    );

    return (
      <ConnectedRouter history={this.props.history}>{routes}</ConnectedRouter>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    // isAuthenticated: state.auth.account != null,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    // autoLoggingIn: () => dispatch(tryAutoLoggingIn()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(App);
