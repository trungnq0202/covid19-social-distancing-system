import React, { useState, useEffect } from "react";
import axios from "../../axios-request";
import Layout from "../../hoc/Layout/Layout";
import { ThermometerHalf, DropletHalf, Moisture } from "react-bootstrap-icons";

const RoomEnvironment = (props) => {
    const [data, setData] = useState({});

    useEffect(() => {
        setInterval(() => {
            fetchEnvVariables();
        }, 2000);
    }, []);

    const fetchEnvVariables = async () => {
        const res = await axios.get("/envimonitor/get");
        setData(res.data[res.data.length - 1]);
    };

  return (
    <Layout>
      <div className="container">
        <h1 className="text-center">Room Environment Monitor</h1>
        <div class="row mt-5 text-center">
          <div class="col-sm">
            <ThermometerHalf size={70} />
            <br />
            <h4> Temperature </h4>
            <h4>{data.temp}</h4>
          </div>
          <div class="col-sm">
            <DropletHalf size={70} />
            <br />
            <h4> Humidity </h4>
            <h4>{data.humi}</h4>
          </div>
          <div class="col-sm">
            <Moisture size={70} />
            <br />
            <h4> Moisture </h4>
            <h4>{data.mois}</h4>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default RoomEnvironment;
