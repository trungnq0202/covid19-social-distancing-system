import React, { useEffect, useState } from "react";
import Layout from "../../hoc/Layout/Layout";
import axios from "../../axios-request";
import "./HomePage.css";
import design3map from "./design3map.png";
const HomePage = (props) => {
  return (
    <Layout>
      <div className="container bg-light" style={{ padding: "20px" }}>
        <h1 className="text-center text-danger">Social distancing system</h1>

        <div>
          The project is to design and build an IoT system which would be used
          for Wuhan virus detection in a working environment. The technical
          group consists of six people, from different engineering majors
          (Robotics, Electrics and Softwares), who would implement the IoT
          system to perform certain tasks. The specification of the system is
          limited to the given hardware from RMIT lecturer (sensors, cameras,
          Raspberry Pi).
        </div>
        <div className="text-center" style={{ padding: "20px" }}>
          <img
            src={design3map}
            class="img-thumbnail img-fluid"
            alt="Hollywood Sign on The Hill"
          />
        </div>

        <div className="row" style={{ padding: "20px" }}>
          <div className="col-md-6">
            <h3>Task 1: Human entry and exit detection</h3>
            <p>
              The system of a camera accompanying an ultrasonic Sensor is used
              to detect people entering or exiting the room.
            </p>
          </div>
          <div className="col-md-6">
            <img
              src="https://mdbcdn.b-cdn.net/img/new/standard/city/041.webp"
              class="img-thumbnail img-fluid"
              alt="Hollywood Sign on The Hill"
            />
          </div>
        </div>

        <div className="row" style={{ padding: "20px" }}>
          <div className="col-md-6">
            <img
              src="https://mdbcdn.b-cdn.net/img/new/standard/city/041.webp"
              class="img-thumbnail img-fluid"
              alt="Hollywood Sign on The Hill"
            />
          </div>
          <div className="col-md-6">
            <h3>Task 2: Room Environment Monitor</h3>
            <p>
              The QR scanning system, including a camera and an LCD, should be
              utilized to check via the camera whether a person’s QR code is
              valid to enter a room or not. Then, the information about the
              validation will be displayed on an LCD. The system can also
              monitor the room’s environmental quality, such as temperature,
              humidity and moisture.
            </p>
          </div>
        </div>

        <div className="row" style={{ padding: "20px" }}>
          <div className="col-md-6">
            <h3>Task 3: Safety Social Distance Monitoring</h3>
            <p>
              The acceptable distance between two people in the room is 1.5m.
              The camera is added so that if there is some violation of the
              policy, the notification will be sent to the user interface for
              the security to do something about it.
            </p>
          </div>
          <div className="col-md-6">
            <img
              src="https://mdbcdn.b-cdn.net/img/new/standard/city/041.webp"
              class="img-thumbnail img-fluid"
              alt="Hollywood Sign on The Hill"
            />
          </div>
        </div>

        <div className="row" style={{ padding: "20px" }}>
          <div className="col-md-6">
            <img
              src="https://mdbcdn.b-cdn.net/img/new/standard/city/041.webp"
              class="img-thumbnail img-fluid"
              alt="Hollywood Sign on The Hill"
            />
          </div>
          <div className="col-md-6">
            <h3>Task 4: Detection of People Assembly</h3>
            <p>
              A camera stream is added to detect human people in the room and
              highlight them in the UI. If the number of people gathering is
              higher than the maximum of 3, the notification will be sent to the
              user interface for the security to do something about it.
            </p>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default HomePage;
