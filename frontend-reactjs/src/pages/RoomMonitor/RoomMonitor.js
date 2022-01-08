import React, { useState, useEffect } from "react";
import axios from "../../axios-request";
import Layout from "../../hoc/Layout/Layout";
import {
  ThermometerHalf,
  DropletHalf,
  Moisture,
  PeopleFill,
} from "react-bootstrap-icons";

const RoomMonitor = (props) => {
  //   const [data, setData] = useState({});

  //   useEffect(() => {
  //     setInterval(() => {
  //       fetchEnvVariables();
  //     }, 2000);
  //   }, []);

  //   const fetchEnvVariables = async () => {
  //     const res = await axios.get("/envimonitor/get");
  //     setData(res.data[res.data.length - 1]);
  //   };

  return (
    <Layout>
      <div className="row">
        <div className="col-md-3 text-center ">
          <div class="col-md"  style={{padding: "50px"}}>
            <ThermometerHalf size={70} />
            <br />
            <h4> Temperature </h4>
            <h4>28</h4>
          </div>
          <div class="col-md"   style={{padding: "50px"}}>
            <DropletHalf size={70} />
            <br />
            <h4> Humidity </h4>
            <h4>54</h4>
          </div>
          <div class="col-md" style={{padding: "50px"}}>
            <PeopleFill size={70} />
            <br />
            <h4> Number of people </h4>
            <h4> 10 </h4>
          </div>
        </div>
        <div className="col" style={{paddingTop: "100px"}}>
          <div className="video">
            <img
              src="https://mdbcdn.b-cdn.net/img/new/slides/041.webp"
              class="img-fluid"
              alt="Wild Landscape"
            />
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default RoomMonitor;
