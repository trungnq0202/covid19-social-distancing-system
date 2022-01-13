import React, { useState, useEffect } from "react";
import axios from "../../axios-request";
import Layout from "../../hoc/Layout/Layout";
import {
  ThermometerHalf,
  DropletHalf,
  Moisture,
  PeopleFill,
  PersonCheckFill,
  PersonDashFill,
} from "react-bootstrap-icons";

import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";

const RoomMonitor = (props) => {
  const [enviData, setEnviData] = useState({});
  // const [flag3, setFlag3] = useState(false);
  // const [flag4, setFlag4] = useState(false);
  const [peopleData, setPeopleData] = useState({});

  // Fetch people data
  const fetchPeopleVariables = async () => {
    const res = await axios.get("/humanEntryAndExit/get/people");
    setPeopleData(res.data);
  };

  /*
  Flow: 
  When there is a detect of violation the rule, the flag will be set to true in the system,

  The front end will check the status of the flag, if it is true, the dialog will be opened

  When the dialog is close, the flag will be set to false by api
  */
  // const handleClose3 = () => {
  //   setFlag3(false)
  //   setAlertFlagTask3(false)
  // };

  // const handleClose4 = () => {
  //   console.log("close 4");
  //   setFlag4(false)
  //   setAlertFlagTask4(false)
  // };

  // const getAlertFlagTask3 = async () => {
  //   const res = await axios.get("/roomMonitor/getTask3Flag");
  //   if (res.data != flag3){
  //     setFlag3(res.data);
  //   }
  // };

  // const setAlertFlagTask3 = async (flag) => {
  //   console.log("close 3");
  //   const res = await axios.post("/roomMonitor/setTask3Flag/" + String(flag));
  //   setFlag3(res.data);
  // };

  // const getAlertFlagTask4 = async () => {
  //   const res = await axios.get("/roomMonitor/getTask4Flag");
  //   setFlag4(res.data);
  // };

  // const setAlertFlagTask4 = async (flag) => {
  //   console.log("close 4");
  //   const res = await axios.post("/roomMonitor/setTask4Flag/" + String(flag));
  //   // setFlag4(res.data);
  //   if (res.data != flag4){
  //     setFlag4(res.data);
  //   }
  // };

  // Fetch env variable
  const fetchEnvVariables = async () => {
    const res = await axios.get("/envimonitor/get");
    setEnviData(res.data[res.data.length - 1]);
  };

  useEffect(() => {
    setInterval(() => {
      if (window.location.href == "http://localhost:3000/room-monitor") {
        fetchEnvVariables();
        // getAlertFlagTask3();
        // getAlertFlagTask4();
        fetchPeopleVariables();
      }

    }, 10000);
  }, []);

  return (
    <Layout>
      <div className="container-roomMonitor" style={{ height: "100vh" }}>
        <h1 class="text-center" style={{ paddingTop: "30px" }}>
          Room Monitor
        </h1>
        <div className="row justify-content-center">
          <div className="col-md-4 text-center">
            <div class="col-md" style={{ padding: "30px" }}>
              <ThermometerHalf size={70} />
              <br />
              <h4> Temperature </h4>
              <h4>{enviData.temp}</h4>
            </div>

            <div class="col-md" style={{ padding: "30px" }}>
              <DropletHalf size={70} />
              <br />
              <h4> Humidity </h4>
              <h4>{enviData.humi}</h4>
            </div>

            <div class="col-md" style={{ padding: "30px" }}>
              <PeopleFill size={70} />
              <br />
              <h4> Number of people in the room </h4>
              <h4> {peopleData.current_num} </h4>
            </div>
          </div>
          <div
            className="col text-center"
            style={{ paddingTop: "40px", paddingRight: "100px" }}
          >
            <div className="video">
              <img
                src="http://0.0.0.0:8003/"
                class="img-fluid"
                alt=" "
                width="90%"
              />
            </div>
          </div>
        </div>
      </div>

      {/* ****************************** DIAGLOG ****************************** */}
      {/* <Dialog
        open={flag3}
        onClose={(e) => handleClose3()}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">WARNING</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            There are some groups of 2 people who violate social distance rule of 1.5m. PLEASE TAKE ACTION IMMEDIATELY!!!
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={(e) => handleClose3()} autoFocus>
            OK
          </Button>
        </DialogActions>
      </Dialog>

      <Dialog
        open={flag4}
        onClose={(e) => handleClose4()}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">WARNING</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            There is a group of 3 people gathering. PLEASE TAKE ACTION IMMEDIATELY!!!
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={(e) => handleClose4()} autoFocus>
            OK
          </Button>
        </DialogActions>
      </Dialog> */}
    </Layout>
  );
};

export default RoomMonitor;
