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
  const [open, setOpen] = React.useState(false);
  const [flag, setFlag] = useState({});
  const [peopleData, setPeopleData] = useState({});

  // Fetch env variable
  const fetchEnvVariables = async () => {
    const res = await axios.get("/envimonitor/get");
    setEnviData(res.data[res.data.length - 1]);
  };

  useEffect(() => {
    setInterval(() => {
      fetchEnvVariables();
    }, 10000);
  }, []);

  // Fetch people data
  const fetchPeopleVariables = async () => {
    const res = await axios.get("/humanEntryAndExit/get/people");
    setPeopleData(res.data);
  };

  useEffect(() => {
    setInterval(() => {
      fetchPeopleVariables();
    }, 1000);
  }, []);
  // Dialog function
  /*
  Flow: 
  When there is a detect of violation the rule, the flag will be set to true in the system,

  The front end will check the status of the flag, if it is true, the dialog will be opened

  When the dialog is close, the flag will be set to false by api
  */
  const openDialog = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    setAlertFlag();
  };

  const getAlertFlag = async () => {
    const res = await axios.get("/roomMonitor/getFlag");
    setFlag(res);
  };

  const setAlertFlag = async () => {
    const res = await axios.post("/roomMonitor/setFlag/" + String(!flag));
    setFlag(res);
  };

  useEffect(() => {
    setInterval(() => {
      getAlertFlag();
      if (flag === true) {
        if (window.location.href == "http://localhost:3000/room-monitor")
          openDialog();
      };
    }, 2000);
  }, []);

  // Fetch env variable
  const fetchEnvVariables = async () => {
    const res = await axios.get("/envimonitor/get");
    setEnviData(res.data[res.data.length - 1]);
  };

  useEffect(() => {
    setInterval(() => {
      if (window.location.href == "http://localhost:3000/room-monitor")
        fetchEnvVariables();
    }, 2000);
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
      <Dialog
        open={open}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">WARNING</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            There is a person or group of people in the room violate the social
            distancing rule.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} autoFocus>
            OK
          </Button>
        </DialogActions>
      </Dialog>
    </Layout>
  );
};

export default RoomMonitor;
